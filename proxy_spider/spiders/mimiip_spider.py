# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy

from ..items import ProxyItem


class MimiipSpider(scrapy.Spider):
    name = "mimiip_spider"
    allowed_domains = [
        "mimiip.com"
    ]

    # start_urls = [
    #     "http://ip84.com/dl"
    # ]

    def start_requests(self):
        for i in ['gngao', 'gnpu', 'gntou', 'hw']:
            for j in range(1, 10):   # page
                url = "http://www.mimiip.com/%s/%s" % (i, j)
                yield scrapy.Request(url, self.parse)

    def parse(self, response):
        # print "parse"

        for trs in response.xpath('//tr'):
            tds = trs.xpath('.//td')

            proxy_item = ProxyItem()
            # proxy_item['country'] = tds[0].xpath('.//img/@alt').extract_first()
            proxy_item['ip'] = tds[0].xpath('.//text()').extract_first()
            proxy_item['port'] = tds[1].xpath('.//text()').extract_first()
            proxy_item['location'] = tds[3].xpath('.//a/text()').extract_first()
            proxy_item['anonymous'] = tds[4].xpath('.//text()').extract_first()
            proxy_item['type'] = tds[5].xpath('.//text()').extract_first()
            # proxy_item['speed'] = tds[6].xpath('.//text()').extract_first()
            proxy_item['time'] = tds[7].xpath('.//text()').extract_first()

            yield proxy_item