# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import urllib2
import threadpool

from proxy_spider.db.mongo import ProxyItemsDB, ProxyItemsValidDB, ProxyItemsJdDB


class DumpAToB(object):
    '''
    验证a中的数据到b中
    '''

    def __init__(self, http_url=None, https_url=None):
        self.http_url = http_url
        self.https_url = https_url
        if not self.http_url and not self.https_url:
            return

        self.pool = None
        self._init_threadpool()
        pass

    def _is_valid_proxy_item(self, item):
        '''
        检查item是否可用,通过传入的URl去检查
        :param item:
        :param http_url:
        :param https_url:
        :return:
        '''

        proxy_type = item["type"].lower()
        if self.https_url and proxy_type == 'https':
            pass
        elif self.http_url and proxy_type == 'http':
            pass
        else:
            # item类型和要爬取的url协议不同, 不可用
            print "item type not valid: proxy type: %s" % proxy_type
            return False

        url = self.http_url if proxy_type == "http" else self.https_url
        proxy = "%s:%s" % (item["ip"], item["port"])
        try:
            req = urllib2.Request(url=url)
            req.set_proxy(proxy, proxy_type)
            response = urllib2.urlopen(req, timeout=self.get_timeout())
        except Exception, e:
            return False
        else:
            code = response.getcode()
            if 200 <= code < 300:
                return True
            else:
                return False

    def thread_call_back(self, is_valid, item):
        pass

    def _thread_call_back(self, args):
        try:
            is_valid = self._is_valid_proxy_item(args)
            if is_valid:
                print "valid item: %s:%s" % (args['ip'], args['port'])
            self.thread_call_back(is_valid, args)
        except Exception, e:
            print "thread_call_back: ", e.message

    def get_argss(self):
        return []

    def get_thread_num(self):
        return 1

    def get_timeout(self):
        return 20

    def _init_threadpool(self):
        try:
            thread_num = self.get_thread_num()
            argss = self.get_argss()
            print "thread_num: ", thread_num
            print "items num: ", argss.count()
            self.pool = threadpool.ThreadPool(thread_num)
            requests = threadpool.makeRequests(self._thread_call_back, argss)
            [self.pool.putRequest(req) for req in requests]
        except Exception, e:
            print "init threadpool: ", e.message
        pass

    def start_threadpool(self):
        try:
            self.pool.wait()
            return True
        except Exception, e:
            print "start threadpool: ", e.message
            return False


class DumpProxyItemsToProxyItemsValid(DumpAToB):
    '''
    验证爬虫爬取的代理到已验证代理中
    '''
    def __init__(self):
        http_url = "http://www.baidu.com/"
        https_url = "https://www.baidu.com/"
        DumpAToB.__init__(self, http_url=http_url, https_url=https_url)
        pass

    def get_argss(self):
        return ProxyItemsDB.get_proxy_items()

    def get_thread_num(self):
        return 60

    def thread_call_back(self, is_valid, item):
        if is_valid:
            ProxyItemsValidDB.upsert_proxy_item(item)
        ProxyItemsDB.remove_proxy_item(item)
        pass


class ValidProxyItemsValid(DumpAToB):
    '''
    重复 验证已验证代理
    '''

    def __init__(self):
        http_url = "http://www.baidu.com/"
        https_url = "https://www.baidu.com/"
        DumpAToB.__init__(self, http_url=http_url, https_url=https_url)
        pass

    def get_argss(self):
        return ProxyItemsValidDB.get_proxy_items()

    def get_thread_num(self):
        return 60

    def thread_call_back(self, is_valid, item):
        if not is_valid:
            ProxyItemsValidDB.remove_proxy_item(item)


class ValidProxyItemsJd(DumpAToB):
    '''
    重复 验证已验证jd代理
    '''

    def __init__(self):
        http_url = "http://www.jd.com"
        https_url = "https://www.jd.com/"
        DumpAToB.__init__(self, http_url=http_url, https_url=https_url)
        pass

    def get_argss(self):
        return ProxyItemsJdDB.get_proxy_items()

    def get_thread_num(self):
        return 60

    def thread_call_back(self, is_valid, item):
        if not is_valid:
            ProxyItemsJdDB.remove_proxy_item(item)


class DumpProxyItemsValidToProxyItemsSite(DumpAToB):
    '''
    验证爬取单个网站可用的代理ip
    '''
    def __init__(self, http_url=None, https_url=None):
        DumpAToB.__init__(self, http_url=http_url, https_url=https_url)
        pass

    def get_argss(self):
        return ProxyItemsValidDB.get_proxy_items()

    def get_thread_num(self):
        return 60

    def upsert_proxy_item(self, item):
        pass

    def thread_call_back(self, is_valid, item):
        if is_valid:
            self.upsert_proxy_item(item)


class DumpProxyItemsValidToProxyItemsJd(DumpProxyItemsValidToProxyItemsSite):
    '''
    验证爬取jd可用的代理ip
    '''
    def __init__(self):
        http_url = "http://www.jd.com/"
        https_url = "https://www.jd.com/"
        DumpProxyItemsValidToProxyItemsSite.__init__(self, http_url=http_url, https_url=https_url)

    def upsert_proxy_item(self, item):
        ProxyItemsJdDB.upsert_proxy_item(item)
