# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import urllib2
import threadpool

from mongo import ProxyItemDB


# def counter(start_at=0):
#     '''
#     Function: count number
#     Usage: f=counter(i) print f() #i+1
#     '''
#     count = [start_at]
#
#     def incr():
#         count[0] += 1
#         return count[0]
#
#     return incr


# def use_proxy(browser, proxy, url):
#     '''Open browser with proxy'''
#     # After visited transfer ip
#     profile = browser.profile
#     profile.set_preference('network.proxy.type', 1)
#     profile.set_preference('network.proxy.http', proxy[0])
#     profile.set_preference('network.proxy.http_port', int(proxy[1]))
#     profile.set_preference('permissions.default.image', 2)
#     profile.update_preferences()
#     browser.profile = profile
#     browser.get(url)
#     browser.implicitly_wait(30)
#     return browser


class Singleton(object):
    '''Signal instance example.'''

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance


class GetIp(Singleton):
    def __init__(self):
        # print "getIP init"
        self.result = ProxyItemDB.get_proxy_items()
        # print "self.result: ", self.result

    def del_ip(self, record):
        # print "del ip"
        ProxyItemDB.remove_proxy_item(record["ip"])
        # print record, " was deleted."

    def check_ip(self, record):
        http_url = "http://www.baidu.com/"
        https_url = "https://www.alipay.com/"
        proxy_type = record["type"].lower()
        # print "proxy_type:=", proxy_type
        url = http_url if proxy_type == "http" else https_url
        proxy = "%s:%s" % (record["ip"], record["port"])
        # print "proxy:=", proxy
        try:
            req = urllib2.Request(url=url)
            req.set_proxy(proxy, proxy_type)
            response = urllib2.urlopen(req, timeout=15)
        except Exception, e:
            # print "Request Error:", e
            return False
        else:
            code = response.getcode()
            if 200 <= code < 300:
                print 'Effective proxy', record
                return True
            else:
                # print 'Invalide proxy', record
                return False

    def judge_ip(self, record):
        '''Judge IP can use or not'''
        ret = self.check_ip(record)
        if ret:
            return True
        else:
            self.del_ip(record)
            return False

    def get_ips(self):
        try:
            print "get_ips"
            pool = threadpool.ThreadPool(60)
            requests = threadpool.makeRequests(self.judge_ip, self.result)
            [pool.putRequest(req) for req in requests]
            pool.wait()
            print "pool wait"
            # print "Proxy getip was executed."
            self.result = ProxyItemDB.get_proxy_items()
            http = [h for h in self.result if h["type"] == "HTTP"]
            https = [h for h in self.result if h["type"] == "HTTPS"]
            print "Http: ", len(http), "Https: ", len(https)
            return {"http": http, "https": https}
        except Exception, e:
            print e
            return {}

# if __name__ == "__main__":
#     GetIp.get_ips()