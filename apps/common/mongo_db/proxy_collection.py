# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from bson import ObjectId

from .mongo_client_db import mongo_client_db
from ..utils import model2dict

proxy_collection = mongo_client_db.proxy


class ProxyCollection(object):
    def __init__(self):
        pass

    @staticmethod
    def get_one():
        return proxy_collection.find_one()
