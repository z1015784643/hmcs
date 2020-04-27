from flask import session
import os
from datetime import timedelta

SERVER_PORT = 9000

SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@127.0.0.1/hmsc?charset=utf8'
SQLALCHEMY_TRACK_MODIFICATIONS = False   #关闭对模型修改的监控




# cookie
AUTH_COOKIE_NAME='hsmc_1901c'

# 设置拦截器的忽略规则
IGNORE_URLS = [
    '^/user/login'
]
IGNORE_CHECK_LOGIN_URLS =[
    '^/static',
    '/favicon.ico'
]

# session

# AUTH_SESSION_NAME="hmsc_1901"
# # session加密字符
# SECRET_KEY = os.urandom(24)
# # session过期时间
# PERMANENT_SESSION_LIFETIME=timedelta(days=7)
