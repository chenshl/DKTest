#!/usr/bin python3
# -*- coding: utf-8 -*-
# @Author : csl
# @Time   : 2018/2/28 15:09
from common.writelog_up import WriteLogger
import time
from HTMLTestRunner import HTMLTestRunner
import unittest

logger = WriteLogger().getLogger()
test_dir = './auto_request2DKApi'  #测试脚本存放路径
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
logger.info("=============")
logger.info("搜寻测试脚本结束")
if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    filename = './report/' + u'接口测试报告_' + now + '.html'  #拼接测试报告完整路径
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'接口测试报告' + now,
                            description=u'''
                            内部接口测试报告结果（仅供参考）,
                            错误的一般为断言结果失败或参数数据变更导致执行错误。''')

    logger.info("开始测试...")
    print("测试进行中...")
    runner.run(discover)
    logger.info("测试结束...")
    fp.close()
    logger.info("保存html报告成功")
    logger.info("=============")