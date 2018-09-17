#!/usr/bin/python3
# coding:utf-8
import unittest
from common.base_connect_mysql import connect_mysql
from common.base import DKApiBase
from common.writelog_up import WriteLogger

logger = WriteLogger.getLogger()

def setUpModule():
    print("setUpModule")

class damo1(unittest.TestCase):

    print("start...")
    @classmethod
    def setUpClass(cls):
        print("输出setUpClass")
        cls.aaa = "111"

        # try:
        #     cls.activitie_id_sql = """SELECT id1, `name`, activitie_id FROM lock_coin_activitie_setting WHERE coin_symbol = 'SLB' AND damages_calc_type = 1 ORDER BY id DESC;"""
        #     cls.activitie_result = DKApiBase().mysqlResultFormat(connect_mysql().connect2mysql(cls.activitie_id_sql),["id", "name", "activitie_id"])
        # except Exception as e:
        #     e

    def tearDown(self):
        print("结果处理完成")


    def test_0(self):
        print("rrrrrr")
        print(self.activitie_result)


    def test_1(self):
        print("test_1运行输出：{}".format(self.aaa))
        print(self.activitie_result)



if __name__ == '__main__':
    unittest.main()