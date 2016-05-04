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
            valid = ValidProxyItemsValid()
            valid.start_threadpool()
        except Exception, e:
            print e.message
