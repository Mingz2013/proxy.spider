# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from ..db.mongo import ProxyItemsDB


class ProxyHelper(object):
    def __init__(self):
        self._cur = None

    def refresh_cur(self):
        self._cur = ProxyItemsDB.get_proxy_items()

    def get_one_proxy(self):
        try:
            proxy = self._cur.next()
            return proxy
        except Exception, e:
            self.refresh_cur()
            return self.get_one_proxy()
