#!/usr/bin/python3
# coding:utf-8

from common.base_connect_mysql import connect_mysql
from common.base import DKApiBase
from common.writelog_up import WriteLogger
from common.request2DKApi import request2DKApi
import requests
# import datetime
import time

logger = WriteLogger.getLogger()


class damo1(object):

    # beging_date = "2018-11-21 17:05:00"
    # print("开始时间",beging_date)
    # timeArray = time.strptime(beging_date, "%Y-%m-%d %H:%M:%S")
    # stime = int(round(time.mktime(timeArray)))
    # print("初始时间戳",stime)
    # tt = stime + 300
    # t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(tt))
    # print("加5分钟后的时间", t)

    # 游戏投票开始时间
    begin_time = "2018-11-21 17:05:00"
    timeArray = time.strptime(begin_time, "%Y-%m-%d %H:%M:%S")
    # 初始时间转换成时间戳
    stime = int(round(time.mktime(timeArray)))
    end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stime + 600))
    open_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stime + 900))
    prize_end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stime + 1500))
    print("开始时间", begin_time)
    print("结束时间", end_time)
    print("开奖时间", open_time)
    print("红包领取结束时间", prize_end_time)



if __name__ == '__main__':
    damo1()