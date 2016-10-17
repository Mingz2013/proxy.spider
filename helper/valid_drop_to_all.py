# -*- coding:utf-8 -*-
__author__ = 'zhaojm'



from log import init_logging
from mongo import ProxyItemsDB, ProxyItemsDropDB

from valid_proxy import valid_proxy


def main():
    cur = ProxyItemsDropDB.get_proxy_items()
    for item in cur:
        ret = valid_proxy(item)
        if ret:
            ProxyItemsDB.upsert_proxy_item(ret)
            ProxyItemsDropDB.remove_proxy_item(item)
            pass
    pass


if __name__ == "__main__":
    init_logging("log/valid_drop_to_all.log", "log/valid_drop_to_all_2.log")
    main()
    pass
