# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import codecs
import datetime
import time
from copy import deepcopy


def get_value_from_dict(dict, key, defaut_v):
    """
    从字典获得查询某个键值，如果不存在，返回默认值
    :param dict:
    :param key:
    :param defaut_v:
    :return:
    """
    if key in dict:
        return dict[key]
    else:
        return defaut_v


def require_value_from_dict(dict, key):
    """
    从字典获得查询某个键值，如果不存在，抛出异常
    :param dict:
    :param key:
    :param defaut_v:
    :return:
    """
    # TODO 处理异常
    return dict[key]


class Storage(dict):
    """
    A Storage object is like a dictionary except `obj.foo` can be used in addition to `obj['foo']`.
        >>> o = storage(a=1)
        >>> o.a
        1
        >>> o['a']
        1
        >>> o.a = 2
        >>> o['a']
        2
        >>> del o.a
        >>> o.a
        Traceback (most recent call last):
            ...
        AttributeError: 'a'
    """

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __setattr__(self, key, value):
        self[key] = value

    def __delattr__(self, key):
        try:
            del self[key]
        except KeyError as k:
            raise AttributeError(k)

    def __repr__(self):
        return '<Storage ' + dict.__repr__(self) + '>'


def model2dict(model, datetime_format='%Y-%m-%d %H:%M:%S'):
    """
    本函数用于使对象可 json 序列化，且返回的字典都是新的（deepcopy）
    """
    if isinstance(model, dict):
        model = Storage(deepcopy(model))
        to_pop = []
        for k in model:
            # 过滤
            if isinstance(k, basestring) and (k.startswith('_') or k.isupper()):
                to_pop.append(k)
                continue
            # 转换
            elif isinstance(model[k], datetime.datetime):
                model[k] = model[k].strftime(datetime_format)
            # 递归
            else:
                model[k] = model2dict(model[k], datetime_format)
        for k in to_pop:
            model.pop(k)
        return model
    elif hasattr(model, '__dict__'):
        return model2dict(model.__dict__, datetime_format)
    elif isinstance(model, (list, tuple)):
        return [model2dict(m, datetime_format) for m in model]
    else:
        return model


def model2dict_x(obj, keys=None):
    """
    获取指定keys的字典
    keys=None 返回所有属性的字典
    """
    if keys is None:
        if isinstance(obj, dict):
            return obj
        elif hasattr(obj, '__dict__'):
            return obj.__dict__
        else:
            raise ValueError('无法处理对象: {0}'.format(str(obj)))

    elif isinstance(keys, list):
        ret = {}
        if isinstance(obj, dict):
            for key in keys:
                ret[key] = obj.get(key, None)
        elif hasattr(obj, '__dict__'):
            obj_dict = obj.__dict__
            for key in keys:
                ret[key] = obj_dict.get(key, None)
                if not ret[key] or ret[key] == 'None':
                    ret[key] = ''
        else:
            raise ValueError('无法处理对象: {0}'.format(str(obj)))
    else:
        raise TypeError('参数类型错误')

    return ret


def get_1000_txt():
    f = codecs.open('data/1000.txt', 'r', 'utf-8')
    return f.read()


def get_timeStamp():
    return int(time.time() * 1000)
