# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import os
import sys

# sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.abspath('.'))

# print os.path.abspath('.')
# print os.path.dirname(os.path.abspath(__file__))

from apps.website import create_app

print "************* CURRENT CONFIG MODE: ", os.getenv('proxy.services.config.mode')
mode = os.getenv('proxy.services.config.mode') or 'default'
if mode:
    mode = mode.lower()
    print 'current config mode: %s' % mode
app = create_app(mode)

if __name__ == '__main__':
    from apps.common.default_encoding import init_encoding

    init_encoding()

    app.debug = True
    app.run(host='0.0.0.0', port=5000)
