# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import pymongo

# MONGO
MONGO_URI = "localhost:27017"
MONGO_PROXY_DB = "proxy"

mongo_client = pymongo.MongoClient(MONGO_URI)
proxy_db = mongo_client[MONGO_PROXY_DB]


def mv_to(from_collection):
    cur = proxy_db[from_collection].find({}, {'_id': 0}).batch_size(50)
    for item in cur:
        print "%s: %s" % (item['ip'], item['port'])
        proxy_db.proxy_items.update({"ip": item['ip'], "port": item['port']}, item, True, True)


collections = [
    "proxy_items_other",
    "proxy_items_qianzhan",
]

if __name__ == "__main__":
    for c in collections:
        mv_to(c)
