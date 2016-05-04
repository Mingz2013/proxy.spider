# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import time
from scrapy.commands import ScrapyCommand
from proxy_spider.proxy.proxy import DumpProxyItemsToProxyItemsValid


class Command(ScrapyCommand):
    requires_project = True
    default_settings = {'LOG_ENABLED': True}

    def short_desc(self):
        return "valid proxy_items to proxy_items_valid"

    def run(self, args, opts):
        try:
            print "===========mc_dump_to_valid run==================="
            dump_to_valid = DumpProxyItemsToProxyItemsValid()
            dump_to_valid.start_threadpool()
            print "===========mc_dump_to_valid over==================="
        except Exception, e:
            print "===========mc_dump_to_valid exception==================="
            print e.message
