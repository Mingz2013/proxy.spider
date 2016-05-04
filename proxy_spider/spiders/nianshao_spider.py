# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy

from ..items import ProxyItem


class NianshaoSpider(scrapy.Spider):
    name = "nianshao_spider"
    allowed_domains = [
        "nianshao.me"
    ]

    # start_urls = [
    #     "http://ip84.com/dl"
    # ]

    custom_settings = {
        'LOG_FILE': 'log/nianshao.log'
    }

    def start_requests(self):
        for i in [1, 2, 5]:
            for j in range(1, 20):  # page
                url = "http://www.nianshao.me/?stype=%s&page=%s" % (i, j)
                yield scrapy.Request(url, self.parse)

    def parse(self, response):
        # print "parse"

        for trs in response.xpath('//tr'):
            tds = trs.xpath('.//td')
            if len(tds) < 8:
                continue
            proxy_item = ProxyItem()
            # proxy_item['country'] = tds[0].xpath('.//img/@alt').extract_first()
            proxy_item['ip'] = tds[0].xpath('.//text()').extract_first()
            proxy_item['port'] = tds[1].xpath('.//text()').extract_first()
            proxy_item['location'] = tds[2].xpath('.//text()').extract_first()
            proxy_item['anonymous'] = tds[3].xpath('.//text()').extract_first()
            proxy_item['type'] = tds[4].xpath('.//text()').extract_first()
            # proxy_item['speed'] = tds[5].xpath('.//text()').extract_first()
            proxy_item['time'] = tds[7].xpath('.//text()').extract_first()

            yield proxy_item