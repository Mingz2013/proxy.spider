# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import options, define

from log import init_logging
from webserver import make_app

define("port", default=8888, help="跑在8001", type=int)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    init_logging()
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
    pass
