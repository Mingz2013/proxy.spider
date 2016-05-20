# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo

from proxy_spider.settings import MONGO_URI, MONGO_PROXY_DB

mongo_client = pymongo.MongoClient(MONGO_URI)
proxy_db = mongo_client[MONGO_PROXY_DB]


class ProxyItemsDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        return proxy_db.proxy_items.find({}, {'_id': 0})

    @staticmethod
    def upsert_proxy_item(item):
        proxy_db.proxy_items.update({"ip": item['ip'], "port": item['port']}, item, True, True)

    @staticmethod
    def remove_proxy_item(item):
        proxy_db.proxy_items.remove({"ip": item['ip'], "port": item['port']})


class ProxyItemsValidDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        return proxy_db.proxy_items_valid.find({}, {'_id': 0})

    @staticmethod
    def upsert_proxy_item(item):
        proxy_db.proxy_items_valid.update({"ip": item['ip'], "port": item['port']}, item, True, True)

    @staticmethod
    def remove_proxy_item(item):
        proxy_db.proxy_items_valid.remove({"ip": item['ip'], "port": item['port']})


class ProxyItemsDropDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        return proxy_db.proxy_items_drop.find({}, {'_id': 0})

    @staticmethod
    def upsert_proxy_item(item):
        proxy_db.proxy_items_drop.update({"ip": item['ip'], "port": item['port']}, item, True, True)

    @staticmethod
    def remove_proxy_item(item):
        proxy_db.proxy_items_drop.remove({"ip": item['ip'], "port": item['port']})


class ProxyItemsJdDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        return proxy_db.proxy_items_jd.find({}, {'_id': 0})

    @staticmethod
    def upsert_proxy_item(item):
        proxy_db.proxy_items_jd.update({"ip": item['ip'], "port": item['port']}, item, True, True)

    @staticmethod
    def remove_proxy_item(item):
        proxy_db.proxy_items_jd.remove({"ip": item['ip'], "port": item['port']})


class ProxyItemsQixinDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        return proxy_db.proxy_items_qixin.find({}, {'_id': 0})

    @staticmethod
    def upsert_proxy_item(item):
        proxy_db.proxy_items_qixin.update({"ip": item['ip'], "port": item['port']}, item, True, True)

    @staticmethod
    def remove_proxy_item(item):
        proxy_db.proxy_items_qixin.remove({"ip": item['ip'], "port": item['port']})


class ProxyItemsBjdaDB(object):
    def __init__(self):
        pass

    @staticmethod
    def get_proxy_items():
        return proxy_db.proxy_items_bjda.find({}, {'_id': 0})

    @staticmethod
    def upsert_proxy_item(item):
        proxy_db.proxy_items_bjda.update({"ip": item['ip'], "port": item['port']}, item, True, True)

    @staticmethod
    def remove_proxy_item(item):
        proxy_db.proxy_items_bjda.remove({"ip": item['ip'], "port": item['port']})
