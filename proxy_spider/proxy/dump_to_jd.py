# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import time

from proxy import DumpProxyItemsValidToProxyItemsJd

if __name__ == '__main__':

    try:
        dump_to_jd = DumpProxyItemsValidToProxyItemsJd()
        dump_to_jd.start_threadpool()
    except Exception, e:
        print e.message
