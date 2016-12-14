# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import paramiko
import time

from haha import *


class VPSSSHClient(object):
    def __init__(self):
        self._min_time_interval = 5  # 最短拨号间隔3-5s
        self._last_request_time = -1
        pass

    def _set_last_request_time(self):
        now = time.time()
        if now - self._last_request_time < self._min_time_interval:
            sleep = self._min_time_interval - (now - self._last_request_time)
            if sleep > 0:
                time.sleep(sleep)
            pass
        self._last_request_time = time.time()
        pass

    def refresh_proxy_ip(self):
        self._set_last_request_time()

        # print "1"
        ssh = paramiko.SSHClient()
        # print "2"
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # print "3"
        ssh.connect(haha, hahaha, hahahaha, hahahahaha)
        # print "4"
        # time.sleep(1)
        stdin, stdout, stderr = ssh.exec_command("adsl-stop")
        # time.sleep(1)
        stdin, stdout, stderr = ssh.exec_command("adsl-start")
        time.sleep(1)
        stdin, stdout, stderr = ssh.exec_command("curl http://123.206.6.251:8888/test_ip")
        # print "5"
        ip = stdout.readline()
        # print "6"
        ssh.close()
        # print "7"
        return ip


        # if __name__  == "__main__":
        #     VPSSSHClient.refresh_proxy_ip()
