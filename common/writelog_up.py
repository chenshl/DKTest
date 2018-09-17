# coding:utf-8
# @author : csl
# @date   : 2018/08/01 09:49
"""logging日志封装"""

import logging.handlers
import time,sys
import os

PATH = os.path.abspath(os.path.join(os.path.dirname('.'),os.path.pardir))  #返回当前执行文件的上一级目录，常用写法
logPATH = str(PATH) + '\\report\\log\\'  #拼接日志目录
if "DKTest" not in logPATH:
    logPATH = str(PATH) + "\\DKTest\\report\\log\\"
date = time.strftime('%Y-%m-%d')  #以字符串形式返回格式化的当前时间time.strftime('%Y-%m-%d %H:%M:%S')
fielname = date+'.log'  #记录日志文件名
abspath = logPATH + fielname  #拼接出完整的路径和日志文件名

class WriteLogger:
    logger = None

    levels = {"n": logging.NOTSET,
              "d": logging.DEBUG,
              "i": logging.INFO,
              "w": logging.WARN,
              "e": logging.ERROR,
              "c": logging.CRITICAL}

    log_level = "d"
    log_file = abspath
    log_max_byte = 10 * 1024 * 1024;
    log_backup_count = 5
    log_encoding = "utf-8"

    @staticmethod
    def getLogger():
        if WriteLogger.logger is not None:
            return WriteLogger.logger

        WriteLogger.logger = logging.Logger("oggingmodule.FinalLogger")
        log_handler = logging.handlers.RotatingFileHandler(filename=WriteLogger.log_file,
                                                           maxBytes=WriteLogger.log_max_byte,
                                                           backupCount=WriteLogger.log_backup_count,
                                                           encoding=WriteLogger.log_encoding)
        log_fmt = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")
        log_handler.setFormatter(log_fmt)
        WriteLogger.logger.addHandler(log_handler)
        WriteLogger.logger.setLevel(WriteLogger.levels.get(WriteLogger.log_level))
        return WriteLogger.logger

    # def __init__(self):
    #     self.getLogger()


# if __name__ == "__main__":
#     logger = WriteLogger.getLogger()
#     logger.debug("测试中文输入!")
#     logger.info("this is a info msg!")
#     logger.warn("this is a warn msg!")
#     logger.error("this is a error msg!")
#     logger.critical("this is a critical msg!")