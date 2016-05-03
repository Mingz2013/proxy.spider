# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import urllib2
import threadpool

from mongo import ProxyItemDB, ProxyItemValidDB


class ProxyHelper(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_valid_items():

        try:
            proxy_items = ProxyItemValidDB.get_proxy_valid_items()
            print "proxy_items.count:=", proxy_items.count()
            http = [h for h in proxy_items if h["type"] == "HTTP"]
            https = [h for h in proxy_items if h["type"] == "HTTPS"]
            print "Http: ", len(http), "Https: ", len(https)
            return {"http": http, "https": https}
        except Exception, e:
            print e.message
            return {}

    @staticmethod
    def check_proxy_items(items=None):
        try:
            if not items: items = ProxyItemDB.get_proxy_items()
            pool = threadpool.ThreadPool(60)
            requests = threadpool.makeRequests(ProxyHelper.judge_proxy_item, items)
            [pool.putRequest(req) for req in requests]
            pool.wait()
            print "check over"
        except Exception, e:
            print e.message

    @staticmethod
    def check_proxy_valid_items(items=None):
        try:
            if not items: items = ProxyItemValidDB.get_proxy_valid_items()
            pool = threadpool.ThreadPool(60)
            requests = threadpool.makeRequests(ProxyHelper.judge_proxy_valid_item, items)
            [pool.putRequest(req) for req in requests]
            pool.wait()
            print "check over"
        except Exception, e:
            print e.message

    @staticmethod
    def check_proxy_item(item):
        http_url = "http://www.baidu.com/"
        https_url = "https://www.alipay.com/"
        proxy_type = item["type"].lower()
        url = http_url if proxy_type == "http" else https_url
        proxy = "%s:%s" % (item["ip"], item["port"])
        try:
            req = urllib2.Request(url=url)
            req.set_proxy(proxy, proxy_type)
            response = urllib2.urlopen(req, timeout=5)
        except Exception, e:
            # print "Request Error:", e
            return False
        else:
            code = response.getcode()
            if 200 <= code < 300:
                print 'Effective proxy', item['ip'], item['port']
                return True
            else:
                # print 'Invalide proxy', record
                return False

    @staticmethod
    def judge_proxy_item(item):
        '''Judge IP can use or not'''
        ret = ProxyHelper.check_proxy_item(item)
        if ret:
            ProxyItemValidDB.upsert_proxy_valid_item(item)
            ProxyItemDB.remove_proxy_item(item)
            return True
        else:
            ProxyItemDB.remove_proxy_item(item)
            return False

    @staticmethod
    def judge_proxy_valid_item(item):
        '''Judge IP can use or not'''
        ret = ProxyHelper.check_proxy_item(item)
        if ret:
            return True
        else:
            ProxyItemValidDB.remove_proxy_valid_item(item)
            return False
