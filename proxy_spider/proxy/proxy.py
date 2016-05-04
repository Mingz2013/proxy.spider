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
            return False

        # TODO 写到这里了
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
        is_valid = self._is_valid_proxy_item(args)
        self.thread_call_back(is_valid, args)
        pass

    def get_argss(self):
        return []

    def get_thread_num(self):
        return 1

    def get_timeout(self):
        return 5

    def _init_threadpool(self):
        try:
            self.pool = threadpool.ThreadPool(self.get_thread_num())
            requests = threadpool.makeRequests(self._thread_call_back, self.get_argss())
            [self.pool.putRequest(req) for req in requests]
        except Exception, e:
            print e.message
        pass

    def start_threadpool(self):
        try:
            self.pool.wait()
            print "check over"
        except Exception, e:
            print e.message


class DumpProxyItemsToProxyItemsValid(DumpAToB):
    def __init__(self):
        DumpAToB.__init__(self)
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


class DumpProxyItemsValidToProxyItemsSite(DumpAToB):
    def __init__(self, http_url=None, https_url=None):
        DumpAToB.__init__(self, http_url, https_url)
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
    def __init__(self):
        http_url = "http://www.jd.com/"
        DumpProxyItemsValidToProxyItemsSite.__init__(self, http_url=http_url)

    def upsert_proxy_item(self, item):
        ProxyItemsJdDB.upsert_proxy_item(item)
