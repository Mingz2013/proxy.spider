# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import os

import redis

REDIS_HOST = os.getenv("REDIS_HOST", '127.0.0.1')
REDIS_PORT = os.getenv("REDIS_PORT", 6379)

redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT, db=0)


class RedisClient(object):
    def __init__(self):
        pass

    @staticmethod
    def set_reg_bug_ent_id(reg_bus_ent_id):
        redis_client.hset("qyxy.baic.reg_bug_ent_id", reg_bus_ent_id, True)
        # pass

    @staticmethod
    def get_reg_bug_ent_id(reg_bus_ent_id):
        return redis_client.hexists("qyxy.baic.reg_bug_ent_id", reg_bus_ent_id)
        # return False

    @staticmethod
    def set_search_key(search_key):
        redis_client.hset("qyxy.baic.search_key", search_key, True)
        # pass

    @staticmethod
    def get_search_key(search_key):
        return redis_client.hexists("qyxy.baic.search_key", search_key)
        # return False
