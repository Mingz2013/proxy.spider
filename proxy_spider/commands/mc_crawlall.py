# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from scrapy.commands import ScrapyCommand


class Command(ScrapyCommand):
    requires_project = True
    default_settings = {'LOG_ENABLED': True}

    def short_desc(self):
        return 'Runs all of the spiders'

    def run(self, args, opts):
        spider_loader = self.crawler_process.spider_loader
        for spidername in args or spider_loader.list():
            print "*********cralall spidername************" + spidername
            self.crawler_process.crawl(spidername, **opts.spargs)

        self.crawler_process.start()
