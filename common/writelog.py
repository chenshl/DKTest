# -*- coding: utf-8 -*-
# Author   : csl
# @Time    : 2018/07/25 10:25
'''日志模块封装'''
import logging
import time,sys
import os
PATH = os.path.abspath(os.path.join(os.path.dirname('.'),os.path.pardir))  #返回当前执行文件的上一级目录，常用写法
logPATH = str(PATH) + '\\report\\log\\'  #拼接日志目录
if "DKTest" not in logPATH:
    logPATH = str(PATH) + "\\DKTest\\report\\log\\"
date = time.strftime('%Y-%m-%d')  #以字符串形式返回格式化的当前时间time.strftime('%Y-%m-%d %H:%M:%S')
fielname = date+'.log'  #记录日志文件名
abspath = logPATH + fielname  #拼接出完整的路径和日志文件名
class writelog(object):
    #配置日志内容
    logging.basicConfig(level=logging.INFO,  #设置日志级别，默认为logging.WARNING
                        format='%(asctime)s %(levelname)s %(message)s',  #指定输出的格式和内容，format可以输出很多有用信息
                        # datefmt='%Y %b %d %a %H:%M:%S',  #指定时间格式，同time.strftime()
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename=abspath,  #指定日志文件名
                        filemode='a'  #和file函数意义相同，指定日志文件的打开模式，'w'或'a'，a+只能在文件最后补充，光标在结尾
                        )

    def writelog(self,level,string):
        if level == 'debug':
            logging.debug(string)
        elif level == "error":
            logging.error(string)
        else:
            logging.info(string)
    def __init__(self,level,string):
        self.writelog(level,string)