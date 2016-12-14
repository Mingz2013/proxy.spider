# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import Flask, request
from log import init_logging
import logging
import json
from vpssshclient import VPSSSHClient

app = Flask(__name__)

vpnsshClient = VPSSSHClient()


@app.route('/')
def home():
    return 'true'


@app.route('/refresh_proxy/<level>/<thread>', methods=['GET'])
def refresh_proxy_level_thread(level, thread):
    level = int(level)
    thread = int(thread)
    num = 0
    if level == 0:
        if thread == 0:
            num = 0
        elif thread == 1:
            num = 1
        elif thread == 2:
            num = 2
    elif level == 1:
        if thread == 0:
            num = 3
    elif level == 2:
        if thread == 0:
            num = 4
    elif level == 3:
        if thread == 0:
            num = 5
    else:
        raise Exception(level)
    logging.info("%s:%s:%s" % (level, thread, num))
    proxy = vpnsshClient.refresh_proxy_ip(num)
    proxies = {"ip": proxy, "port": 5839}
    logging.info(request.headers['user-agent'] + "\nyour current ip is: " + request.remote_addr)
    logging.info("write:-> %s" % proxies)
    return json.dumps(proxies)


# @app.route('/refresh_proxy/level_1', methods=['GET'])
# def refresh_proxy_level_1():
#     proxy = vpnsshClient.refresh_proxy_ip(2)
#     proxies = {"ip": proxy, "port": 5839}
#     logging.info(request.headers['user-agent'] + "\nyour current ip is: " + request.remote_addr)
#     logging.info("write:-> %s" % proxies)
#     return json.dumps(proxies)


# @app.route('/test_ip', methods=['GET'])
# def test_ip():
#     return request.remote_addr
#     pass


if __name__ == '__main__':
    init_logging('log/refresh_proxy.log', 'log/refresh_proxy_2.log')
    logging.info("run.................")
    app.run(host="0.0.0.0", port=8881)
