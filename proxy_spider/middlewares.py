# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import base64
import random
from proxy_spider.proxy.proxy_helper import ProxyHelper
import logging


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
    def __init__(self):
        self.proxy_helper = ProxyHelper()

    def process_request(self, request, spider):

        if request.url.startswith("https://"):
            # TODO 由于https代理验证有问题,这里暂时改为,将https代理替换成http代理
            request.url = request.url.replace("https://", "http://")

        if request.url.startswith("http://"):
            proxy = self.proxy_helper.get_one_proxy()

            request.meta['proxy'] = "http://%s:%d" % (proxy["ip"], int(proxy["port"]))

            # # Use the following lines if your proxy requires authentication
            # proxy_user_pass = "USERNAME:PASSWORD"
            # # setup basic authentication for the proxy
            # encoded_user_pass = base64.b64encode(proxy_user_pass)
            # request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
