# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import time
from scrapy.commands import ScrapyCommand
from proxy_spider.proxy.proxy import ValidProxyItemsJd


class Command(ScrapyCommand):
    requires_project = True
    default_settings = {'LOG_ENABLED': True}

    def short_desc(self):
        return "valid proxy_items_jd"

    def run(self, args, opts):
        try:
            valid = ValidProxyItemsJd()
            valid.start_threadpool()
        except Exception, e:
            print e.message
