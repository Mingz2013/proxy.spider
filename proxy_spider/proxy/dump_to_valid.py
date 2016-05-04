# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import time

from proxy import DumpProxyItemsToProxyItemsValid

if __name__ == '__main__':

    while True:
        try:
            dump_to_valid = DumpProxyItemsToProxyItemsValid()
            dump_to_valid.start_threadpool()
        except Exception, e:
            print "loop error: ", e.message

        time.sleep(60 * 5)
        pass
