# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import json
import logging

import tornado.ioloop
import tornado.web

from vpssshclient import VPSSSHClient


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info("get....." + self.request.remote_ip)
        self.write(self.request.remote_ip)

    def post(self):
        # logging.info("post........")
        logging.info("post....." + self.request.remote_ip)
        self.set_header("Content-Type", "text/plain")
        self.write(self.request.headers['user-agent'] + "\nyour current ip is: " + self.request.remote_ip)


class RefreshHandler(tornado.web.RequestHandler):
    def initialize(self):
        self._vpnsshClient = VPSSSHClient()

    def get(self):
        logging.info("get....." + self.request.remote_ip)
        proxy = self._vpnsshClient.refresh_proxy_ip()
        proxies = {"ip": proxy, "port": 5839}
        logging.info(self.request.headers['user-agent'] + "\nyour current ip is: " + self.request.remote_ip)
        logging.info("write:-> %s" % proxies)
        self.write(json.dumps(proxies))
        # self.write("111")

    def post(self):
        # logging.info("post........")
        logging.info("post....." + self.request.remote_ip)
        self.set_header("Content-Type", "text/plain")
        self.write(self.request.headers['user-agent'] + "\nyour current ip is: " + self.request.remote_ip)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        logging.info("get.....")
        self.write('true')

    def post(self):
        logging.info("post........")
        self.set_header("Content-Type", "text/plain")
        self.write("true")


def make_app():
    application = tornado.web.Application([
        (r"/test_ip", TestHandler),
        (r"/refresh_proxy", RefreshHandler),
        (r"/", MainHandler),
    ])
    return application
