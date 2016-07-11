# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import urllib2


def main():
    proxy = "%s:%s" % (item["ip"], item["port"])
    try:
        req = urllib2.Request(url=self.http_url)
        req.set_proxy(proxy, 'http')
        response = urllib2.urlopen(req, timeout=5)
    except Exception, e:
        return False
    else:
        code = response.getcode()
        if 200 <= code < 300:
            return True
        else:
            return False
