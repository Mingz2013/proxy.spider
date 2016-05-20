# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import time
from scrapy.commands import ScrapyCommand
from proxy_spider.proxy.proxy import ValidProxyItemsBjda


class Command(ScrapyCommand):
    requires_project = True
    default_settings = {'LOG_ENABLED': True}

    def short_desc(self):
        return "valid proxy_items_jd"

    def run(self, args, opts):
        try:
            print "===========mc_valid_jd run==================="
            valid = ValidProxyItemsBjda()
            valid.start_threadpool()
            print "===========mc_valid_jd over==================="
        except Exception, e:
            print "===========mc_valid_jd exception==================="
            print e.message
