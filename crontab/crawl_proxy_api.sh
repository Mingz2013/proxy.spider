#!/usr/bin/env bash
cd /home/apps/proxy.spider
dt=$(date "+%Y-%m-%d")
path_to_log="log/""$dt""_crawl_proxy_api.log"
echo $path_to_log
scrapy mc_crawl_proxy_api -s LOG_FILE=$path_to_log &
