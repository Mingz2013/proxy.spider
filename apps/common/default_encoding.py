# -*- coding:utf-8 -*-
__author__ = 'zhaojm'


def init_encoding():
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")
    print "sys default encoding: ", sys.getdefaultencoding()
