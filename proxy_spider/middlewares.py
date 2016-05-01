# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import base64
from proxy import GetIp
import logging

ips = GetIp().get_ips()

print "ips: %s" + ips

class ProxyMiddleware(object):
    def __init__(self):
        print "proxyMiddleware init"
        self.http_n = 0  # counter for http requests
        self.https_n = 0  # counter for https requests

    # overwrite process request
    def process_request(self, request, spider):
        print "process request"
        # Set the location of the proxy
        if request.url.startswith("http://"):
            n = self.http_n
            n = n if n < len(ips['http']) else 0
            request.meta['proxy'] = "http://%s:%d" % (
                ips['http'][n][0], int(ips['http'][n][1]))
            logging.info('Squence - http: %s - %s' % (n, str(ips['http'][n])))
            self.http_n = n + 1

        if request.url.startswith("https://"):
            n = self.https_n
            n = n if n < len(ips['https']) else 0
            request.meta['proxy'] = "https://%s:%d" % (
                ips['https'][n][0], int(ips['https'][n][1]))
            logging.info('Squence - https: %s - %s' % (n, str(ips['https'][n])))
            self.https_n = n + 1
