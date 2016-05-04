# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from setuptools import setup, find_packages

setup(name='scrapy-proxy_spider',
      entry_points={
          'scrapy.commands': [
              'crawlall=proxy_spider.commands:crawlall',
              'dump_to_valid=proxy_spider.commands:dump_to_valid',
              'valid_jd=proxy_spider.commands:valid_jd',
              'dump_to_jd=proxy_spider.commands:dump_to_jd',
              'valid_valid=proxy_spider.commands:valid_valid',
          ],
      },
      )
