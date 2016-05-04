# 思路
- scrapy spider     ---------> proxy_items
- proxy_items       --baidu--> proxy_items_valid
- proxy_item_valid  --jd-----> proxy_items_jd

---

# service
- 每天定时爬取网站,放到proxy_items
- 不断验证proxy_items, 放到proxy_items_valid
- 定时验证proxy_items_valid
- 定时验证proxy_items_valid, 放到proxy_items_jd
- 定时验证proxy_items_jd

---

# 定时任务

		1  2  *  *  * root       /home/apps/proxy_spider/crontab/scrawl.sh
		30 *  *  *  * root       /home/apps/proxy_spider/crontab/dump_to_valid.sh
		1  *  *  *  * root       /home/apps/proxy_spider/crontab/valid_valid.sh
		30 *  *  *  * root       /home/apps/proxy_spider/crontab/valid_valid.sh
		1  6  *  *  * root       /home/apps/proxy_spider/crontab/dump_to_jd.sh
		30 *  *  *  * root       /home/apps/proxy_spider/crontab/valid_jd.sh

