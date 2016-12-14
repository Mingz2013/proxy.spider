#!/usr/bin/env bash
cd /home/apps/proxy.services
sleep 5
ps -aux | grep test_ip | awk '{print $2}' | while read line; do kill -9 $line; done;
sleep 5
sh scripts/setup_test_ip.sh &

