# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from proxy_spider.db.mongo import ProxyItemsDB, ProxyItemsValidDB, ProxyItemsJdDB


class ProxyHelper(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items_valid_type_http():
        try:
            proxy_items = ProxyItemsValidDB.get_proxy_items()
            print "proxy_items.count:=", proxy_items.count()
            http = [h for h in proxy_items if h["type"].lower().find("http") > 0]
            print "Https: ", len(http)
            return http
        except Exception, e:
            print e.message
            return []

    @staticmethod
    def get_proxy_items_valid_type_https():
        try:
            proxy_items = ProxyItemsValidDB.get_proxy_items()
            print "proxy_items.count:=", proxy_items.count()
            https = [h for h in proxy_items if h["type"].lower().find("https") > 0]
            print "Https: ", len(https)
            return https
        except Exception, e:
            print e.message
            return []
