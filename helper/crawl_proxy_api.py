# -*- coding:utf-8 -*-
__author__ = 'zhaojm'


import requests
import json
from mongo import ProxyItemsDB
import logging
from log import init_logging


def run():
    try:
        logging.info("===========mc_crawl_proxy_api run===================")
        r = requests.get(
            "http://proxy.mimvp.com/api/fetch.php?orderid=860160922170106912&num=5000&result_fields=1,2,3,4,5,6,7,8,9&result_format=json")
        r_json = json.loads(r.text)
        proxy_list = r_json['result']
        for proxy in proxy_list:
            logging.info(proxy)
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

        logging.info("===========mc_crawl_proxy_api over===================")
    except Exception, e:
        logging.info("===========mc_crawl_proxy_api exception===================")
        logging.info(e.message)


if __name__ == "__main__":
    init_logging("log/crawl_proxy_api.log", "log/crawl_proxy_api_2.log")
    run()
