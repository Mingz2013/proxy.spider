# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import os

import pymongo

MONGODB_HOST = os.getenv("MONGODB_HOST", '127.0.0.1')
MONGODB_PORT = os.getenv("MONGODB_PORT", 27017)
mongo_client_db = pymongo.MongoClient(MONGODB_HOST, MONGODB_PORT).proxy_services
