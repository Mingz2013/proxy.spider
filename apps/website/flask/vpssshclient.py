# -*- coding:utf-8 -*-
__author__ = 'zhaojm'

import paramiko
import time

from ssh_config import get_ssh_config, username, password


class VPSSSHClient(object):
    def __init__(self):
        self._min_time_interval = 3  # 最短拨号间隔3-5s
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

    def refresh_proxy_ip(self, num):
        cfg = get_ssh_config(num)
        ip = cfg['ip']
        port = cfg['port']
        return self.refresh_proxy(ip, port)

    def refresh_proxy(self, ip, port):

        self._set_last_request_time()
        # time.sleep(100000)

        print "1"
        ssh = paramiko.SSHClient()
        print "2"
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        print "3"
        ssh.connect(ip, port, username, password)
        print "4"
        # time.sleep(1)
        stdin, stdout, stderr = ssh.exec_command("adsl-stop")
        # time.sleep(1)
        print "5"
        stdin, stdout, stderr = ssh.exec_command("adsl-start")
        print "6"
        time.sleep(2)
        stdin, stdout, stderr = ssh.exec_command("curl http://123.206.6.251:8888/test_ip")
        print "7"
        ip = stdout.readline()
        print "8"
        ssh.close()
        print "9"
        return ip
