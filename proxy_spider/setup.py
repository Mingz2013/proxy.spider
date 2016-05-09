# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from setuptools import setup, find_packages

setup(name='scrapy-proxy_spider',
      entry_points={
          'scrapy.commands': [
              'mc_crawlall=proxy_spider.commands:mc_crawlall',
              'mc_dump_to_valid=proxy_spider.commands:mc_dump_to_valid',
              'mc_valid_jd=proxy_spider.commands:mc_valid_jd',
              'mc_dump_to_jd=proxy_spider.commands:mc_dump_to_jd',
              'mc_valid_valid=proxy_spider.commands:mc_valid_valid',
              'mc_valid_drop=proxy_spider.commands:mc_valid_drop',
              'mc_crawl_proxy_api=proxy_spider.commands:mc_crawl_proxy_api',
          ],
      },
      )
