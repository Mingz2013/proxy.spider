# -*- coding:utf-8 -*-
__author__ = 'zhaojm'


from log import init_logging
from mongo import ProxyItemsDB, ProxyItemsDropDB

from valid_proxy import valid_proxy
from get_proxy import GetProxy



def main():
    get_proxy = GetProxy(ProxyItemsDB)
    while True:
        item = get_proxy.get_proxy()
        ret = valid_proxy(item)
        if ret:
            ProxyItemsDB.remove_proxy_item(item)
            ProxyItemsDB.upsert_proxy_item(ret)
            pass
        else:
            ProxyItemsDB.remove_proxy_item(item)
            ProxyItemsDropDB.upsert_proxy_item(item)
            pass
    pass


if __name__ == "__main__":
    init_logging("log/valid_all_to_drop.log", "log/valid_all_to_drop_2.log")
    main()
    pass
