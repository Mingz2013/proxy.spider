# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from scrapy.commands import ScrapyCommand
from proxy_spider.proxy.proxy import DumpProxyItemsValidToProxyItemsBjda


class Command(ScrapyCommand):
    requires_project = True
    default_settings = {'LOG_ENABLED': True}

    def short_desc(self):
        return "valid proxy_items_valid to proxy_items_jd"

    def run(self, args, opts):
        try:
            print "===========mc_dump_to_jd run==================="
            dump_to_bjda = DumpProxyItemsValidToProxyItemsBjda()
            dump_to_bjda.start_threadpool()
            print "===========mc_dump_to_jd over==================="
        except Exception, e:
            print "===========mc_dump_to_jd exception==================="
            print e.message
