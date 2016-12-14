#!/usr/bin/env bash
cd /home/apps/proxy.service
#python src/setup.proxy.service.py &
python flask/test_ip_service.py &
#python flask/refresh_proxy_service.py &