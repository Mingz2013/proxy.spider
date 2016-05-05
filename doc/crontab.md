# 定时任务

		# Example of job definition:
		# .---------------- minute (0 - 59)
		# |  .------------- hour (0 - 23)
		# |  |  .---------- day of month (1 - 31)
		# |  |  |  .------- month (1 - 12) OR jan,feb,mar,apr ...
		# |  |  |  |  .---- day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
		# |  |  |  |  |
		# *  *  *  *  * user-name  command to be executed
		  1  2  *  *  * root       /home/apps/proxy_spider/crontab/crawlall.sh
		  30 *  *  *  * root       /home/apps/proxy_spider/crontab/dump_to_valid.sh
		  1  *  *  *  * root       /home/apps/proxy_spider/crontab/valid_valid.sh
		  20 *  *  *  * root       /home/apps/proxy_spider/crontab/valid_drop.sh
		  30 6  *  *  * root       /home/apps/proxy_spider/crontab/dump_to_jd.sh
		  1  *  *  *  * root       /home/apps/proxy_spider/crontab/valid_jd.sh 
