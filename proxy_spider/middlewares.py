# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import base64
import random
from proxy import GetIp
import logging

ips = GetIp().get_ips()


class RandomUserAgentMiddleware(object):
    """Randomly rotate user agents based on a list of predefined ones"""

    def __init__(self, agents):
        self.agents = agents

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler.settings.getlist('USER_AGENTS'))

    def process_request(self, request, spider):
        request.headers.setdefault('User-Agent', random.choice(self.agents))


class ProxyMiddleware(object):
    http_n = 0
    https_n = 0

    def process_request(self, request, spider):
        # Set the location of the proxy
        if request.url.startswith("http://"):
            n = ProxyMiddleware.http_n
            n = n if n < len(ips['http']) else 0
            request.meta['proxy'] = "http://%s:%d" % (
                ips['http'][n]["ip"], int(ips['http'][n]["port"]))
            # logging.info('Squence - http: %s - %s:%s' % (n, ips['http'][n]['ip'], ips['http'][n]['port']))
            ProxyMiddleware.http_n = n + 1

        if request.url.startswith("https://"):
            n = ProxyMiddleware.https_n
            n = n if n < len(ips['https']) else 0
            request.meta['proxy'] = "https://%s:%d" % (
                ips['https'][n]["ip"], int(ips['https'][n]["port"]))
            # logging.info('Squence - http: %s - %s:%s' % (n, ips['http'][n]['ip'], ips['http'][n]['port']))
            ProxyMiddleware.https_n = n + 1
