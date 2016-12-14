# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import Flask, request
from log import init_logging
import logging
import json

# from vpssshclient import VPSSSHClient

app = Flask(__name__)


# vpnsshClient = VPSSSHClient()


@app.route('/')
def home():
    return 'true'


# @app.route('/refresh_proxy', methods=['GET'])
# def refresh_proxy():
#     proxy = vpnsshClient.refresh_proxy_ip()
#     proxies = {"ip": proxy, "port": 5839}
#     logging.info(request.headers['user-agent'] + "\nyour current ip is: " + request.remote_addr)
#     logging.info("write:-> %s" % proxies)
#     return json.dumps(proxies)
#     pass


@app.route('/test_ip', methods=['GET'])
def test_ip():
    logging.info("remote_addr: %s" % request.remote_addr)
    return request.remote_addr
    pass


if __name__ == '__main__':
    init_logging('log/test_ip.log', 'log/test_ip_2.log')
    logging.info("run.................")
    app.run(host="0.0.0.0", port=8888)
