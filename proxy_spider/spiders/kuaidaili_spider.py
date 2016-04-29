# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import scrapy

from ..items import ProxyItem


class XicidailiSpider(scrapy.Spider):
    name = "kuaidaili_spider"
    allowed_domains = [
        "kuaidaili.com"
    ]

    start_urls = [
        "http://www.kuaidaili.com/free/inha/",     # 国内高匿代理
        "http://www.kuaidaili.com/free/intr/",     # 国内普通代理
        "http://www.kuaidaili.com/free/outha/",     # 国外高匿代理
        "http://www.kuaidaili.com/free/outtr/"    # 国外普通代理
    ]

    def parse(self, response):

        success = 0
        for sel in response.xpath('//tr[@class="odd"]'):
            tds = sel.xpath('.//td')

            proxy_item = ProxyItem()
            proxy_item['country'] = tds[0].xpath('.//img/@alt').extract_first()
            proxy_item['ip'] = tds[1].xpath('.//text()').extract_first()
            proxy_item['port'] = tds[2].xpath('.//text()').extract_first()
            proxy_item['location'] = tds[3].xpath('.//a/text()').extract_first()
            proxy_item['anonymous'] = tds[4].xpath('.//text()').extract_first()
            proxy_item['type'] = tds[5].xpath('.//text()').extract_first()
            proxy_item['time'] = tds[8].xpath('.//text()').extract_first()
            # TODO check the proxy

            success += 1
            yield proxy_item

        if success > 0:
            next_page = response.xpath('//a[@class="next_page"]/@href')
            if next_page:
                url = "http://www.xicidaili.com" + next_page.extract_first()
                print url
                request = scrapy.Request(url, self.parse)
                yield request