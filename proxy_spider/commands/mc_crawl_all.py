# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from scrapy.commands import ScrapyCommand
from scrapy.crawler import CrawlerRunner
from scrapy.utils.conf import arglist_to_dict
from scrapy.exceptions import UsageError


class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return '[options]'

    def short_desc(self):
        return 'Runs all of the spiders'

    def add_options(self, parser):
        ScrapyCommand.add_options(self, parser)
        parser.add_option("-a", dest="spargs", action="append", default=[], metavar="NAME=VALUE",
                          help="set spider argument (may be repeated)")
        parser.add_option("-o", "--output", metavar="FILE",
                          help="dump scraped items into FILE (use - for stdout)")
        parser.add_option("-t", "--output-format", metavar="FORMAT",
                          help="format to use for dumping items with -o")

    def process_options(self, args, opts):
        ScrapyCommand.process_options(self, args, opts)
        try:
            opts.spargs = arglist_to_dict(opts.spargs)
        except ValueError:
            raise UsageError("Invalid -a value, use -a NAME=VALUE", print_help=False)

    def run(self, args, opts):
        try:
            print "===========mc_crawl_all run==================="
            spider_loader = self.crawler_process.spider_loader
            for spidername in args or spider_loader.list():
                print "*********mc_crawl_all spidername************" + spidername
                self.crawler_process.crawl(spidername, **opts.spargs)
            self.crawler_process.start()
            print "===========mc_crawl_all over==================="
        except Exception, e:
            print "===========mc_crawl_all exception==================="
            print e.message
