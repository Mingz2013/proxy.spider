# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo

# MONGO
MONGO_URI = "localhost:27017"
MONGO_PROXY_DB = "proxy"

mongo_client = pymongo.MongoClient(MONGO_URI)
proxy_db = mongo_client[MONGO_PROXY_DB]


class ProxyItemsDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        return proxy_db.proxy_items_all.find({}, {'_id': 0}).batch_size(50)

    @staticmethod
    def upsert_proxy_item(item):
        proxy_db.proxy_items_all.update({"ip": item['ip'], "port": item['port']}, item, True, True)

    @staticmethod
    def remove_proxy_item(item):
        proxy_db.proxy_items_all.remove({"ip": item['ip'], "port": item['port']})


class ProxyItemsDropDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        return proxy_db.proxy_items_drop.find({}, {'_id': 0}).batch_size(50)

    @staticmethod
    def upsert_proxy_item(item):
        proxy_db.proxy_items_drop.update({"ip": item['ip'], "port": item['port']}, item, True, True)

    @staticmethod
    def remove_proxy_item(item):
        proxy_db.proxy_items_drop.remove({"ip": item['ip'], "port": item['port']})


class ProxyItemsTmpDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        return proxy_db.proxy_items_tmp.find({}, {'_id': 0}).batch_size(50)

    @staticmethod
    def upsert_proxy_item(item):
        proxy_db.proxy_items_tmp.update({"ip": item['ip'], "port": item['port']}, item, True, True)

    @staticmethod
    def remove_proxy_item(item):
        proxy_db.proxy_items_tmp.remove({"ip": item['ip'], "port": item['port']})
