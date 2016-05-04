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
            dump_to_valid = DumpProxyItemsToProxyItemsValid()
            dump_to_valid.start_threadpool()
        except Exception, e:
            print "loop error: ", e.message
