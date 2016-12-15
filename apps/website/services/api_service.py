# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from apps.common.mongo_db.proxy_collection import ProxyCollection
from flask import current_app


class APIService(object):
    def __init__(self):
        pass

    @staticmethod
    def get_one():
        ret = ProxyCollection.get_one()
        current_app.logger.info(ret)
        return ret
