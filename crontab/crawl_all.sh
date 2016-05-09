#!/usr/bin/env bash
cd /home/apps/proxy_spider
dt=$(date "+%Y-%m-%d")
path_to_log="log/""$dt""_crawl_all.log"
echo $path_to_log
scrapy mc_crawlall -s LOG_FILE=$path_to_log &
