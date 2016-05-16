#!/usr/bin/env bash
cd /home/apps/proxy_spider
dt=$(date "+%Y-%m-%d")
path_to_log="log/""$dt""_dump_to_qixin.log"
echo $path_to_log
scrapy mc_dump_to_qixin -s LOG_FILE=$path_to_log &
