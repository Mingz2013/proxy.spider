# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import base64
import random
from proxy_helper import ProxyHelper
import logging

proxy_items = ProxyHelper.get_proxy_valid_items()


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
            n = n if n < len(proxy_items['http']) else 0
            request.meta['proxy'] = "http://%s:%d" % (
                proxy_items['http'][n]["ip"], int(proxy_items['http'][n]["port"]))
            ProxyMiddleware.http_n = n + 1

            # # Use the following lines if your proxy requires authentication
            # proxy_user_pass = "USERNAME:PASSWORD"
            # # setup basic authentication for the proxy
            # encoded_user_pass = base64.b64encode(proxy_user_pass)
            # request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass

        if request.url.startswith("https://"):
            n = ProxyMiddleware.https_n
            n = n if n < len(proxy_items['https']) else 0
            request.meta['proxy'] = "https://%s:%d" % (
                proxy_items['https'][n]["ip"], int(proxy_items['https'][n]["port"]))
            ProxyMiddleware.https_n = n + 1
