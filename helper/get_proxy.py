# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from mongo import ProxyItemsDB, ProxyItemsTmpDB, ProxyItemsDropDB
import logging
import time


class GetProxy(object):
    def __init__(self, db):
        self._db = db
        self._proxy_cur = self._db.get_proxy_items()
        pass

    def get_proxy(self):
        try:
            item = self._proxy_cur.next()
            return item
        except Exception, e:
            self._proxy_cur = self._db.get_proxy_items()
            if self._proxy_cur.count() == 0:
                logging.info("proxy is empty, sleep 30 * 60s")
                time.sleep(30 * 60)
            return self.get_proxy()
