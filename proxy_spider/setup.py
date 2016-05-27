# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from setuptools import setup, find_packages

setup(name='scrapy-proxy_spider',
      entry_points={
          'scrapy.commands': [
              'mc_crawl_all=proxy_spider.commands:mc_crawl_all',
              'mc_dump_to_valid=proxy_spider.commands:mc_dump_to_valid',
              'mc_valid_valid=proxy_spider.commands:mc_valid_valid',
              'mc_valid_drop=proxy_spider.commands:mc_valid_drop',
              'mc_crawl_proxy_api=proxy_spider.commands:mc_crawl_proxy_api',

              'mc_valid_jd=proxy_spider.commands:mc_valid_jd',
              'mc_dump_to_jd=proxy_spider.commands:mc_dump_to_jd',

              'mc_dump_to_jd=proxy_spider.commands:mc_dump_to_jd',
              'mc_valid_jd=proxy_spider.commands:mc_valid_jd',

              'mc_dump_to_bjda=proxy_spider.commands:mc_dump_to_bjda',
              'mc_valid_bjda=proxy_spider.commands:mc_valid_bjda',

              'mc_dump_to_qichacha=proxy_spider.commands:mc_dump_to_qichacha',
              'mc_valid_qichacha=proxy_spider.commands:mc_valid_chacha',
          ],
      },
      )
