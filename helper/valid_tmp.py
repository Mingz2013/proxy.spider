# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import logging

import requests

from log import init_logging
from mongo import ProxyItemsDB, ProxyItemsDropDB, ProxyItemsTmpDB

default_header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # Cookie:BAIDUID=0FAB7AC75B563748879524E53467A1C9:FG=1; BIDUPSID=82981CC127B05686979592572B76E0FA; PSTM=1469697709; __cfduid=dee876621e330e5d3cb6ec9a4c114dbbd1472051490; MCITY=-150%3A131%3A; BDUSS=i1YTE9XY2J6dzIwVVBIdmRRTzFCWHItWGVhYmRmZkJ-dkRDc3JJcXpFR2xPUjlZQVFBQUFBJCQAAAAAAAAAAAEAAAC6ksIyTWluZ1p6bmV0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKWs91elrPdXa; BDSFRCVID=ts_sJeC62rBsbhRRUC5jbhKJsHLpYQnTH6aoboc7AGJ4-1jZebOCEG0PfU8g0Ku-hfU6ogKK0mOTH65P; H_BDCLCKID_SF=tJPD_KKXJIvbfP0k-465bJDBMfb-etJya4o2WDkEKf75OR5Jj6K-5PFWLUnNK53nbIr3ahcb5lvYqJIR3MA--t4Syxcj-Tv9LbTG5R7F-pjbsq0x0bOte-bQyp_LK4ReKDOMahkMal7xOKLG05ChDTOyjauqq-Tta64XWP58K6uhb5rnhPF3hjFrKP6-3MJO3b7OWUn4LJ3mVRIx5tccyfPWbqoUKMA83j7johFLtCt2hCKRej83KPIhql63-4T0KRAqoTrJabC3DKjDKU6qLT5XLtr7JT5nLDvqXRvt2pvkqn5pMjOIMl0njxQy5-rv-mvlWPOlQhcbJJT8jxonDh8E3H7MJUntHC7d0MjO5hvvhb6O3MA-jqOhjH-jJ508JJ3BLR6MHJRhDRDkjjA_-P4Dep5BQnJZ5m7mXp0bJJT_SMo83PoN0pkd54Tm--QtQKvrVlQb-IOkbCL6e5DKjjJM-Uv05-PXKCJ0X458HJOoDDvoLJo5y4LdLp7xJ-rhymQNWfQ5t4j0qf7JQ6QbbMImXbQgJPteWJLD_KIbJIKbbP365IT55tCthxtX5-RLfaIHbPOF5lOTJh0RjxQ1hpDA-lrHbRcwH67r5fojLt38SRTw3Tbke6bBjHLeJj0sb5vfstct2jrjDnC7K-cjhP08HHL8J5_jJJKO8t52ax75DP54-P_X-40Q2mjt-PrdaCTbB45Eq4OqDDv1bRO5y4LdLp7xJ-rZQI7N-xnT2R7-jnc1j-OTX4tz3p6LXl_eWJLfoKL-JKDWbP365ITV5tAVhMnMetJyaR3JQM7bWJ5TMCo4LRbDMhDw3t-tatj3W2QeapRMyxj_ShPC-tnDhPJWLtJZtIuD2HQ-3q7n3l02VbQae-t2ynQDMMjPttRMW20jWl7mWILhVKcnK4-Xjj3yeHjP; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; BD_CK_SAM=1; BD_HOME=1; H_PS_PSSID=1463_13289_21082_21191_21161; BD_UPN=123253; __bsi=11816751578327644818_00_0_I_R_24_0303_C02F_N_I_I_0
    'Host': 'www.baidu.com',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}


def valid_proxy(item):
    try:
        proxies = {"http": "%s:%s" % (item["ip"], item["port"])}
        logging.info(proxies)
        response = requests.get("http://www.baidu.com", proxies=proxies, allow_redirects=False, timeout=3,
                                headers=default_header)
        if response.status_code != 200:
            raise Exception("status code error")
        if response.text.find(u"百度") < 0:
            raise Exception("not found baidu")
        logging.info("-----------------valid good---------------------")
        return True
    except Exception, e:
        logging.info("-----------------valid bad---------------------%s" % e.message)
        return False


def main():
    cur = ProxyItemsTmpDB.get_proxy_items()
    for item in cur:
        if valid_proxy(item):
            ProxyItemsDB.upsert_proxy_item(item)
            pass
        else:
            ProxyItemsDropDB.upsert_proxy_item(item)
            pass
        ProxyItemsTmpDB.remove_proxy_item(item)

    pass


if __name__ == "__main__":
    init_logging("log/valid_tmp.log", "log/valid_tmp_2.log")
    main()
    pass
