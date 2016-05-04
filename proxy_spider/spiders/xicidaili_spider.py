# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy

from ..items import ProxyItem


class XicidailiSpider(scrapy.Spider):
    name = "xicidaili_spider"
    allowed_domains = [
        "xicidaili.com"
    ]

    # start_urls = [
    #     "http://ip84.com/dl"
    # ]

    custom_settings = {
        'LOG_FILE': 'log/xicidaili.log'
    }

    def start_requests(self):
        for i in ['nn', 'nt', 'wn', 'wt']:
            for j in range(1, 10):   # page
                url = "http://www.xicidaili.com/%s/%s" % (i, j)
                yield scrapy.Request(url, self.parse)

    def parse(self, response):
        # print "parse"

        for trs in response.xpath('//tr'):
            tds = trs.xpath('.//td')
            if len(tds) < 9:
                continue
            proxy_item = ProxyItem()
            # proxy_item['country'] = tds[0].xpath('.//img/@alt').extract_first().strip()
            proxy_item['ip'] = tds[1].xpath('.//text()').extract_first().strip()
            proxy_item['port'] = tds[2].xpath('.//text()').extract_first().strip()
            proxy_item['location'] = tds[3].xpath('.//a/text()').extract_first().strip()
            proxy_item['anonymous'] = tds[4].xpath('.//text()').extract_first().strip()
            proxy_item['type'] = tds[5].xpath('.//text()').extract_first().strip()
            proxy_item['time'] = tds[8].xpath('.//text()').extract_first().strip()

            yield proxy_item