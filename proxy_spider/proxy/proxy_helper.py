# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from proxy_spider.db.mongo import ProxyItemsDB, ProxyItemsValidDB, ProxyItemsJdDB


class ProxyHelper(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items_valid():
        try:
            proxy_items = ProxyItemsValidDB.get_proxy_items()
            print "proxy_items.count:=", proxy_items.count()
            http = [h for h in proxy_items if h["type"] == "HTTP"]
            https = [h for h in proxy_items if h["type"] == "HTTPS"]
            print "Http: ", len(http), "Https: ", len(https)
            return {"http": http, "https": https}
        except Exception, e:
            print e.message
            return {}
