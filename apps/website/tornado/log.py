# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging
from logging.handlers import RotatingFileHandler


# CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET

def init_logging(log_file1="log/log.log", log_file2="log/debug.log"):
    format_str = '%(asctime)s %(filename)s[line:%(lineno)d] <%(levelname)s> %(message)s'

    logging.basicConfig(
        level=logging.DEBUG,
        format=format_str,
        datefmt='%Y-%m-%d %H:%M:%S',
        filename=log_file1,
        filemode='w'
    )

    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    formatter = logging.Formatter(format_str)
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    # 定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大10M
    Rthandler = RotatingFileHandler(log_file2, maxBytes=10 * 1024 * 1024, backupCount=5)
    Rthandler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(format_str)
    Rthandler.setFormatter(formatter)
    logging.getLogger('').addHandler(Rthandler)

    # logging.debug('This is debug message')
    # logging.info('This is info message')
    # logging.warning('This is warning message')
