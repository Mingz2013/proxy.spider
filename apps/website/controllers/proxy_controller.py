# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import request, Blueprint, jsonify, current_app

api = Blueprint('proxy_controller', __name__, url_prefix='/proxy')


@api.route('/test_ip', methods=['GET'])
def test_ip():
    current_app.logger.info("remote_addr: %s" % request.remote_addr)
    return request.remote_addr
