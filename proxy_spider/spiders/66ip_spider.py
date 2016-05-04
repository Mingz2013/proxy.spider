# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy

from ..items import ProxyItem


class _66IPSpider(scrapy.Spider):
    name = "66ip_spider"
    allowed_domains = [
        "66ip.cn"
    ]

    # start_urls = [
    #     "http://www.66ip.cn/areaindex_1/1.html"
    # ]

    custom_settings = {
        'LOG_FILE': 'log/66ip.log'
    }

    def start_requests(self):
        for i in range(1, 34):
            for j in range(1, 10):   # page
                url = "http://www.66ip.cn/areaindex_%s/%s.html" % (i, j)
                yield scrapy.Request(url, self.parse)

    def parse(self, response):
        # print "parse"

        for trs in response.xpath('//tr'):
            tds = trs.xpath('.//td')
            if len(tds) < 5:
                continue
            proxy_item = ProxyItem()
            # proxy_item['country'] = tds[0].xpath('.//img/@alt').extract_first()
            proxy_item['ip'] = tds[0].xpath('.//text()').extract_first()
            proxy_item['port'] = tds[1].xpath('.//text()').extract_first()
            proxy_item['location'] = tds[2].xpath('.//text()').extract_first()
            proxy_item['anonymous'] = tds[3].xpath('.//text()').extract_first()
            proxy_item['type'] = 'HTTP'
            proxy_item['time'] = tds[4].xpath('.//text()').extract_first()

            yield proxy_item