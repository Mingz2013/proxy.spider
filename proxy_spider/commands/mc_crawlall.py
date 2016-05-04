# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from scrapy.commands import ScrapyCommand


class Command(ScrapyCommand):
    requires_project = True
    default_settings = {'LOG_ENABLED': True}

    def short_desc(self):
        return 'Runs all of the spiders'

    def run(self, args, opts):
        try:
            print "===========mc_crawlall run==================="
            spider_loader = self.crawler_process.spider_loader
            for spidername in args or spider_loader.list():
                print "*********mc_crawlall spidername************" + spidername
                self.crawler_process.crawl(spidername, **opts.spargs)
            self.crawler_process.start()
            print "===========mc_crawlall over==================="
        except Exception, e:
            print "===========mc_crawlall exception==================="
            print e.message
