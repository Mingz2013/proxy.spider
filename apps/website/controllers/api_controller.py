# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

from flask import request, Blueprint, jsonify, current_app, render_template

from ..services.api_service import APIService

api = Blueprint('api_controller', __name__, url_prefix='/api')


@api.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@api.route('/get_one', methods=['GET'])
def get_one():
    try:
        proxy = APIService.get_one()
        return jsonify({'retcode': 0, 'errmsg': "", 'result': proxy})
    except Exception, e:
        current_app.logger.error(e.message)
        return jsonify({'retcode': -1, 'errmsg': e.message, 'result': ""})
