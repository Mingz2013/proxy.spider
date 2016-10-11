

# For details see man 4 crontabs

# Example of job definition:
# .---------------- minute (0 - 59)
# |  .------------- hour (0 - 23)
# |  |  .---------- day of month (1 - 31)
# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
# |  |  |  |  |
# *  *  *  *  * user-name  command to be executed
  0  *  *  *  * root       sh /home/apps/proxy.spider/crontab/crawl_all.sh
  0  *  *  *  * root       sh /home/apps/proxy.spider/crontab/crawl_proxy_api.sh
  30 *  *  *  * root       sh /home/apps/proxy.spider/crontab/valid_tmp.sh
  0  0  *  *  * root       sh /home/apps/proxy.spider/crontab/valid_drop_to_all.sh
  30 0  *  *  * root       sh /home/apps/proxy_spider/crontab/valid_all_to_drop.sh


  0  1  *  *  * root       sh /home/apps/qianlima_spider/crontab/run_spider_with_selenium.sh 