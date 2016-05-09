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
- 没通过验证的放到drop里,再次验证一次

---


