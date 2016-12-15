# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import time

from .base0 import Base0
from ..utils import require_value_from_dict


class Proxy(Base0):
    def __init__(self, obj):
        Base0.__init__(self)

        self.ip = require_value_from_dict(obj, 'ip')
        self.port = require_value_from_dict(obj, 'port')
        self.type = require_value_from_dict(obj, 'type')
        self.update_time = require_value_from_dict(obj, 'update_time')
