# # -*- coding:utf-8 -*-
# __author__ = 'zhaojm'
#
# import redis
# import os
#
# REDIS_HOST = os.getenv("REDIS_HOST", '127.0.0.1')
# REDIS_PORT = os.getenv("REDIS_PORT", 6379)
#
# redis_client = redis.StrictRedis(REDIS_HOST, REDIS_PORT, db=0)
#
# # 向redis里缓存用户信息 key:user_info field:user_id value:name;head_img_url
# # redis> HSET myhash field1 "Hello"
#
# USER_INFO_KEY = "user_info"
# USER_OPENID = "user_openid"
# TOKEN = "token"
# TOKEN_EXPIRE_SECONDS = 3600 * 24 * 90  # 三个月
# USER_ID = "user_id"
# CLUB_ID = "club_id"
# EVENT_ID = "event_id"
# POST_ID = "post_id"
# VENUE_ID = "venue_id"
# COMPANY_ID = "company_id"
# SMS_ID = 'sms_id'
# SMS_CODE = "sms_code"
# SMS_USER_TIMES = "sms_user_times"
# ROBOT_QQ_KEY = "robot_qq_key"
# ADMIN_TOKEN = "admin_token"
#
# redis_client.expire(ROBOT_QQ_KEY, 3)
# redis_client.expire(SMS_USER_TIMES, 3600*2)
# redis_client.expire(SMS_CODE, 300)
# redis_client.expire(TOKEN, TOKEN_EXPIRE_SECONDS)
# redis_client.expire(ADMIN_TOKEN, 60 * 60 * 24)
#
#
# class RedisClient():
#
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def clear_redis():
#         """
#         清理缓存，慎用
#         """
#         fkeys = redis_client.keys()
#         for key in fkeys:
#             redis_client.delete(key)
#
#     @staticmethod
#     def cache_user(u_id, value):
#         """
#         缓存用户基本信息  key:id value:
#         """
#         return redis_client.hset(USER_INFO_KEY, u_id, value)
#
#     @staticmethod
#     def new_user_id():
#         return redis_client.incr(USER_ID)
#
#     @staticmethod
#     def new_club_id():
#         return redis_client.incr(CLUB_ID)
#
#     @staticmethod
#     def new_event_id():
#         return redis_client.incr(EVENT_ID)
#
#     @staticmethod
#     def new_post_id():
#         return redis_client.incr(POST_ID)
#
#     @staticmethod
#     def new_venue_id():
#         return redis_client.incr(VENUE_ID)
#
#     @staticmethod
#     def new_company_id():
#         return redis_client.incr(COMPANY_ID)
#
#     @staticmethod
#     def new_sms_id():
#         return redis_client.incr(SMS_ID)
#
#     @staticmethod
#     def cache_sms_code(mobile, code):
#         """
#         缓存短信，一分钟有效
#         """
#         redis_client.hset(SMS_CODE, mobile, code)
#
#     @staticmethod
#     def get_sms_code(mobile):
#         """
#         缓存短信，一分钟有效
#         """
#         return redis_client.hget(SMS_CODE, mobile)
#
#     @staticmethod
#     def inc_user_sms_times(mobile):
#         """
#         限制用户10次发送验证码后两小时内不能再发
#         """
#         return redis_client.hincrby(SMS_USER_TIMES, mobile, 1)
#
#     @staticmethod
#     def get_user_from_cache(u_id):
#         return redis_client.hget(USER_INFO_KEY, u_id)
#
#     @staticmethod
#     def cache_openid(open_id, value):
#         """
#         缓存用户微信信息  key:openid value: id|wx_nickname|wx_sex|wx_head_img_url
#         """
#         return redis_client.hset(USER_OPENID, open_id, value)
#
#     @staticmethod
#     def get_openid_from_cache(openid):
#         return redis_client.hget(USER_OPENID, openid)
#
#     @staticmethod
#     def cache_token(token, user_id):
#         """
#         缓存用户token  key:token value: user_id
#         """
#         redis_client.hset(TOKEN, user_id, token)
#
#     @staticmethod
#     def check_token(token, user_id):
#         if redis_client.hget(TOKEN, user_id) and token == redis_client.hget(TOKEN, user_id):
#             return True
#         else:
#             return False
#
#     @staticmethod
#     def get_wx_jsapi_ticket_from_cache():
#         return redis_client.get("wx_jsapi_ticket")
#
#     @staticmethod
#     def set_wx_jsapi_ticket_from_cache(token, s):
#         redis_client.set("wx_jsapi_ticket", token)
#         redis_client.expire("wx_jsapi_ticket", s)
#
#     @staticmethod
#     def set_robot_qq_key(qq):
#         redis_client.hset(ROBOT_QQ_KEY, qq, True)
#
#     @staticmethod
#     def get_robot_qq_key(qq):
#         return redis_client.hget(ROBOT_QQ_KEY, qq)
#
#     @staticmethod
#     def del_robot_qq_key(qq):
#         redis_client.hdel(ROBOT_QQ_KEY, qq)
#
#     @staticmethod
#     def cache_admin_token(token, admin_id):
#         """
#         缓存用户token  key:token value: user_id
#         """
#         redis_client.hset(ADMIN_TOKEN, str(admin_id), token)
#
#     @staticmethod
#     def check_admin_token(token, admin_id):
#         if redis_client.hget(ADMIN_TOKEN, str(admin_id)) and token == redis_client.hget(ADMIN_TOKEN, str(admin_id)):
#             return True
#         else:
#             return False
