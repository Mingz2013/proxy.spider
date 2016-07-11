# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from scrapy.commands import ScrapyCommand
import requests
import json
from proxy_spider.db.mongo import ProxyItemsDB


class Command(ScrapyCommand):
    requires_project = True
    default_settings = {'LOG_ENABLED': True}

    def short_desc(self):
        return "crawl proxy api"

    def run(self, args, opts):
        try:
            print "===========mc_crawl_proxy_api run==================="
            r = requests.get(
                "http://proxy.mimvp.com/api/fetch.php?orderid=860160711120754476&num=3000&http_type=1,2&result_fields=1,2,3,4,5,6,7,8,9&result_format=json")
            r_json = json.loads(r.text)
            proxy_list = r_json['result']
            for proxy in proxy_list:
                # print proxy
                ip_port = proxy['ip:port']
                ip, port = ip_port.split(':')
                item = {
                    'ip': ip,
                    'port': port,
                    'location': proxy['country'],
                    'anonymous': proxy['anonymous'],
                    'type': proxy['http_type'],
                    'speed': proxy['transfer_time'],
                    'time': proxy['check_dtime'],
                }
                ProxyItemsDB.upsert_proxy_item(item)

            print "===========mc_crawl_proxy_api over==================="
        except Exception, e:
            print "===========mc_crawl_proxy_api exception==================="
            print e.message
