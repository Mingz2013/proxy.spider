# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import time
from scrapy.commands import ScrapyCommand
from proxy_spider.proxy.proxy import ValidProxyItemsQichacha


class Command(ScrapyCommand):
    requires_project = True
    default_settings = {'LOG_ENABLED': True}

    def short_desc(self):
        return "valid proxy_items_qichacha"

    def run(self, args, opts):
        try:
            print "===========mc_valid_qichacha run==================="
            valid = ValidProxyItemsQichacha()
            valid.start_threadpool()
            print "===========mc_valid_qichacha over==================="
        except Exception, e:
            print "===========mc_valid_qichacha exception==================="
            print e.message
