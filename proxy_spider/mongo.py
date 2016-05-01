# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import os
import pymongo
import datetime
import time
import threading

from settings import MONGO_URI, MONGO_DATABASE

mongo_client = pymongo.MongoClient(MONGO_URI)
proxy_db = mongo_client[MONGO_DATABASE]


class ProxyItemDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        pass

    @staticmethod
    def upsert_proxy_item(ip, item):
        pass

    @staticmethod
    def remove_proxy_item(ip):
        pass


