# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
# import pymongo
from mongo import ProxyItemDB

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


class MongoPipeline(object):

    # collection_name = 'proxy_items'

    # def __init__(self, mongo_uri, mongo_db):
    #     self.mongo_uri = mongo_uri
    #     self.mongo_db = mongo_db

    # @classmethod
    # def from_crawler(cls, crawler):
    #     return cls(
    #         mongo_uri=crawler.settings.get('MONGO_URI', "localhost:27017"),
    #         mongo_db=crawler.settings.get('MONGO_DATABASE', 'proxy')
    #     )
    #
    # def open_spider(self, spider):
    #     self.client = pymongo.MongoClient(self.mongo_uri)
    #     self.db = self.client[self.mongo_db]
    #
    # def close_spider(self, spider):
    #     self.client.close()

    def process_item(self, item, spider):
        # self.db[self.collection_name].insert(dict(item))
        # self.db[self.collection_name].update({"ip": item["ip"]}, dict(item), true, true)
        ProxyItemDB.upsert_proxy_item(item["ip"], dict(item))
        return item


