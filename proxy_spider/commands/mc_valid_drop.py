# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from scrapy.commands import ScrapyCommand
from proxy_spider.proxy.proxy import ValidProxyItemsDrop


class Command(ScrapyCommand):
    requires_project = True
    default_settings = {'LOG_ENABLED': True}

    def short_desc(self):
        return "valid proxy_items_drop"

    def run(self, args, opts):
        try:
            print "===========mc_valid_drop run==================="
            valid = ValidProxyItemsDrop()
            valid.start_threadpool()
            print "===========mc_valid_drop over==================="
        except Exception, e:
            print "===========mc_valid_drop exception==================="
            print e.message
