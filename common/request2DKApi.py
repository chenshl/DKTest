# coding:utf-8
# @author : csl
# @date   : 2018/07/24 13:35
"""
请求封装
"""

import requests
import time
from common.writelog_up import WriteLogger
from common.baseDatas import *

logger = WriteLogger().getLogger()

class request2DKApi(object):

    def __init__(self, server, datas={}, header={"access-auth-token":COMMON_TOKEN}):

        # 判断后台路径
        if "admin/" in server:
            self.url = REQUESTS_URL_ADMIN  # 后台
        else:
            self.url = REQUESTS_URL
        # self.url = "http://172.16.0.79:6003/"  # 撮合exchange-api
        # self.url = "http://172.16.0.79:6001/"  # ucenter-api
        # self.url = "http://172.16.0.79:6002/"  # otc-api
        # self.url = "http://172.16.1.84:6003/"  # 撮合exchange-api田波本机

        self.server = server
        self.requrl = self.url + self.server
        self.data = datas
        self.header = header  # 定义请求头信息，用户token
        # self.cookie = {'key': 'value'}  # 定义cookie


    def send(self, requestMark="POST"):
        try:
            logger.info("请求地址：{}  请求方式：{}--请求参数：{}".format(self.url + self.server, requestMark, self.data))
            self.beforetime = time.time()
            if requestMark == "GET":
                print("请求地址：{}  请求方式：{}--请求参数{}".format(self.url + self.server, requestMark, self.data))
                self.req = requests.get(self.requrl)
            elif requestMark == "POST":
                print("请求地址：{}  请求方式：{}--请求参数{}".format(self.url + self.server, requestMark, self.data))
                self.req = requests.post(self.requrl, self.data, headers=self.header)
            elif requestMark == "PATCH":
                print("请求地址：{}  请求方式：{}--请求参数{}".format(self.url + self.server, requestMark, self.data))
                self.req = requests.patch(self.requrl,self.data)
            self.aftertime = time.time()
            self.reqtime = str(round((self.aftertime - self.beforetime) * 1000, 3))
            logger.info("响应时长：{}--响应状态:{}--响应结果：{}".format(self.reqtime,self.req.status_code, self.req.text))
        except Exception as e:
            print("请求异常：{}".format(e))
            logger.error("请求异常{}".format(e))
        return self.req.status_code, self.reqtime, self.req.text
