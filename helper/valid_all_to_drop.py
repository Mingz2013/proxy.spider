# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from mongo import ProxyItemsDB, ProxyItemsDropDB
import requests


def valid_proxy(item):
    try:
        proxies = {"http": "%s:%s" % (item["ip"], item["port"])}
        response = requests.get("http://www.baidu.com", proxies=proxies, allow_redirects=False, timeout=5)
        if response.status_code != 200:
            raise Exception("status code error")
        if response.text.find(u"百度") < 0:
            raise Exception("not found baidu")
        return True
    except Exception, e:
        return False


def main():
    cur = ProxyItemsDB.get_proxy_items()
    for item in cur:
        if valid_proxy(item):
            pass
        else:
            ProxyItemsDB.remove_proxy_item(item)
            ProxyItemsDropDB.upsert_proxy_item(item)

    pass


if __name__ == "__main__":
    main()
    pass
