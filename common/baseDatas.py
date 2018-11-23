# coding:utf-8
# @author : csl
# @date   : 2018/08/17 15:08
"""基础数据配置"""

# 请求路径配置
REQUESTS_URL = "http://api.400.pro/"  # 前端测试环境地址
# REQUESTS_URL = "http://api.dev.pro/"  # 前端联调环境地址
REQUESTS_URL_ADMIN = "http://api.dkadmin.400.pro/"  # 后台
# REQUESTS_URL_ADMIN = "http://api.dkadmin.dev.pro/"  # 后台联调环境地址

# 用户token
COMMON_TOKEN = "1000000000001"  # 常用用户token/memberId=74773
# COMMON_TOKEN = "test17700000041"  # 常用用户token/memberId=80068
COMMON_TOKEN_ANOTHER = "f2794f54e17720d34aa505e3556724f3"  # 另外一个常用用户token用于C2C交互/memberId=74782
COMMON_TOKEN_GENERAL_USER = "17700000030"  # 普通用户，用于C2C广告发布
COMMON_TOKEN_GENERAL_USER_ANOTHER = "17700000031"  # 普通用户，用于C2C广告交易