# 定时任务

		# Example of job definition:
		# .---------------- minute (0 - 59)
		# |  .------------- hour (0 - 23)
		# |  |  .---------- day of month (1 - 31)
		# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
		# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
		# |  |  |  |  |
		# *  *  *  *  * user-name  command to be executed
		  0  *  *  *  * root       sh /home/apps/proxy_spider/crontab/crawlall.sh
		  10 *  *  *  * root       sh /home/apps/proxy_spider/crontab/crawl_proxy_api.sh
		  20 *  *  *  * root       sh /home/apps/proxy_spider/crontab/dump_to_valid.sh
		  30 *  *  *  * root       sh /home/apps/proxy_spider/crontab/valid_valid.sh
		  40 *  *  *  * root       sh /home/apps/proxy_spider/crontab/valid_drop.sh
		  50 *  *  *  * root       sh /home/apps/proxy_spider/crontab/dump_to_jd.sh
		  15  *  *  *  * root       sh /home/apps/proxy_spider/crontab/valid_jd.sh 
		  
		  0  1  *  *  * root       sh /home/apps/proxy_spider/crontab/backup_mongodb.sh