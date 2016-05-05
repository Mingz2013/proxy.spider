# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
from proxy_spider.db.mongo import ProxyItemsDB


# from proxy import ProxyHelper


class ValidParamsPipeline(object):
    def process_item(self, item, spider):
        try:
            if item["ip"] and item["port"] and (0 < int(item['port']) < 65535):
                return item
            raise DropItem("params not Valid: %s:%s" % (item.get("ip"), item.get("port")))
        except Exception, e:
            raise DropItem("params not Valid: %s:%s" % (item.get("ip"), item.get("port")))


class DuplicatesPipeline(object):
    def __init__(self):
        self.ips_seen = set()

    def process_item(self, item, spider):
        if item.get('ip') in self.ips_seen:
            raise DropItem("Duplicate item found: %s:%s" % (item.get("ip"), item.get("port")))
        else:
            self.ips_seen.add(item.get('ip'))
            return item


# class CheckProxyPipeline(object):
#     def process_item(self, item, spider):
#         # print "CheckProxyPipeline"
#         ret = ProxyHelper.check_proxy_item(item)
#         if ret:
#             return item
#         else:
#             raise DropItem("bad proxy: %s" % item)


class MongoPipeline(object):
    def process_item(self, item, spider):
        ProxyItemsDB.upsert_proxy_item(dict(item))
        return item
