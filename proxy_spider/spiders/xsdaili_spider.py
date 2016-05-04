# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy

from ..items import ProxyItem


class XsdailiSpider(scrapy.Spider):
    name = "xsdaili_spider"
    allowed_domains = [
        "xsdaili.com"
    ]

    # start_urls = [
    #     "http://ip84.com/dl"
    # ]

    custom_settings = {
        'LOG_FILE': 'log/xsdaili.log'
    }

    def start_requests(self):
        for i in [1, 2, 3, 4]:
            for j in range(1, 10):   # page
                url = "http://www.xsdaili.com/index.php?s=/index/mfdl/type/%s/p/%s.html" % (i, j)
                yield scrapy.Request(url, self.parse)

    def parse(self, response):
        # print "parse"

        for trs in response.xpath('//tr'):
            tds = trs.xpath('.//td')

            proxy_item = ProxyItem()
            # proxy_item['country'] = tds[0].xpath('.//img/@alt').extract_first()
            proxy_item['ip'] = tds[0].xpath('.//text()').extract_first()
            proxy_item['port'] = tds[1].xpath('.//text()').extract_first()
            proxy_item['anonymous'] = tds[2].xpath('.//text()').extract_first()
            proxy_item['type'] = tds[3].xpath('.//text()').extract_first()
            proxy_item['location'] = tds[5].xpath('.//a/text()').extract_first()
            proxy_item['speed'] = tds[7].xpath('.//text()').extract_first()
            proxy_item['time'] = tds[8].xpath('.//text()').extract_first()

            yield proxy_item