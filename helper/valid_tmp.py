# -*- coding:utf-8 -*-
__author__ = 'zhaojm'


from log import init_logging
from mongo import ProxyItemsDB, ProxyItemsDropDB, ProxyItemsTmpDB

from valid_proxy import valid_proxy


def main():
    cur = ProxyItemsTmpDB.get_proxy_items()
    for item in cur:
        ret = valid_proxy(item)
        if ret:
            ProxyItemsDB.upsert_proxy_item(ret)
            pass
        else:
            ProxyItemsDropDB.upsert_proxy_item(item)
            pass
        ProxyItemsTmpDB.remove_proxy_item(item)

    pass


if __name__ == "__main__":
    init_logging("log/valid_tmp.log", "log/valid_tmp_2.log")
    main()
    pass
