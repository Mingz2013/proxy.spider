# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import urllib2

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
        self.result = ProxyItemDB.get_proxy_items()

    def del_ip(self, record):
        '''delete ip that can not use'''
        ProxyItemDB.remove_proxy_item(record["ip"])
        print record, " was deleted."

    def check_ip(self, record):
        http_url = "http://www.baidu.com/"
        https_url = "https://www.alipay.com/"
        proxy_type = record["type"].lower()
        url = http_url if proxy_type == "http" else https_url
        proxy = "%s:%s" % (record["ip"], record["port"])
        try:
            req = urllib2.Request(url=url)
            req.set_proxy(proxy, proxy_type)
            response = urllib2.urlopen(req, timeout=30)
        except Exception, e:
            print "Request Error:", e
            return False
        else:
            code = response.getcode()
            if 200 <= code < 300:
                print 'Effective proxy', record
                return True
            else:
                print 'Invalide proxy', record
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
        print "Proxy getip was executed."
        http = [h[0:2] for h in self.result if h[2] == "HTTP" and self.judge_ip(h)]
        https = [h[0:2] for h in self.result if h[2] == "HTTPS" and self.judge_ip(h)]
        print "Http: ", len(http), "Https: ", len(https)
        return {"http": http, "https": https}
