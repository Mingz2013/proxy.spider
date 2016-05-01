# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
# import pymongo
from mongo import ProxyItemDB
from proxy import GetIp


# class ProxySpiderPipeline(object):
#     def process_item(self, item, spider):
#         return item

class DuplicatesPipeline(object):
    def __init__(self):
        self.ips_seen = set()

    def process_item(self, item, spider):
        if item['ip'] in self.ips_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ips_seen.add(item['ip'])
            return item


class CheckProxyPipeline(object):
    def process_item(self, item, spider):
        ret = GetIp.check_ip(dict(item))
        if ret:
            return item
        else:
            raise DropItem("bad proxy: %s" % item)


class MongoPipeline(object):

    def process_item(self, item, spider):
        ProxyItemDB.upsert_proxy_item(item["ip"], dict(item))
        return item
