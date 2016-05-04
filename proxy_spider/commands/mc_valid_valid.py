# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from scrapy.commands import ScrapyCommand
from proxy_spider.proxy.proxy import ValidProxyItemsValid


class Command(ScrapyCommand):
    requires_project = True
    default_settings = {'LOG_ENABLED': True}

    def short_desc(self):
        return "valid proxy_items_valid"

    def run(self, args, opts):
        try:
            print "===========mc_valid_valid run==================="
            valid = ValidProxyItemsValid()
            valid.start_threadpool()
            print "===========mc_valid_valid over==================="
        except Exception, e:
            print "===========mc_valid_valid exception==================="
            print e.message
