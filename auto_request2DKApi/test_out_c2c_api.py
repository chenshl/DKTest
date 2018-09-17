# coding:utf-8
# @author : csl
# @date   : 2018/08/04 16:30
# c2c查询类接口

import unittest
from common.request2DKApi import request2DKApi
from common.base import DKApiBase

class DKApiautoTest_c2c_out(unittest.TestCase):
    """c2c查询类接口"""

    def setUp(self):

        self.otc_coin_id = "2"  # otc_coin表币种ID
        self.unit = "USDT"  # 根据币种分页查询广告,币种
        self.username = "测试1"  # 会员用户名
        self.advertid = "98"  # 广告id
        self.orderSn = "81390709814464512"  # 查询订单号
        self.memberId = "74773"  # 用户表memberId

    def tearDown(self):

        pass

    def test_otc_advertise_all(self):
        """个人所有广告and广告详情"""
        # 所有广告
        serverc = "otc/advertise/all"
        r = request2DKApi(serverc).send()
        print(r)
        # 广告详情
        serverc = "otc/advertise/detail"
        data = {"id":str(DKApiBase().str2json(r[2])["data"][0]["id"])}
        r_detail = request2DKApi(serverc, data).send()
        print(r_detail)
        self.assertRegexpMatches(r_detail[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_otc_advertise_self_all(self):
        """个人所有广告self_all"""
        serverc = "otc/advertise/self/all"
        r = request2DKApi(serverc).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_otc_advertise_excellent(self):
        """查询优质广告"""
        server = "otc/advertise/excellent"
        data = {"advertiseType": "1"}  # 广告类型0买入1卖出
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_otc_advertise_page(self):
        """分页查询广告"""
        server = "otc/advertise/page"
        data = {"pageNo": "0",  # 非必传
                "pageSize": "10",  # 非必传
                "advertiseType": "0",  # 条件：0买、1卖
                "id": self.otc_coin_id,  # 币种id  otc_coin表
                "isCertified": "0"  # 是否只显示认证商家.1:是0：否  # 非必传
                }
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_otc_advertise_page_by_unit(self):
        """根据币种分页查询广告"""
        server = "otc/advertise/page-by-unit"
        data = {"pageNo": "2",
                "pageSize": "10",
                "advertiseType": "0",  # 条件：0买、1卖  #必传
                "unit": self.unit,  # 币种string  必传
                "isCertified": "0"  # 是否只显示认证商家.1:是0：否
                }
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_otc_advertise_member(self):
        """会员广告查询"""
        server = "otc/advertise/member"
        data = {"name": self.username}
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_otc_order_pre(self):
        """买入，卖出详细信息"""
        server = "otc/order/pre"
        data = {"id": self.advertid}  # 广告id
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_otc_order_self(self):
        """我的订单"""
        server = "otc/order/self"
        data = {"status": "0",  # 订单状态， 0=已取消/1=未付款/2=已付款/3=已完成/4=申诉中
                "pageNo": "0",  # 页数,非必传
                "pageSize": "10",  # 每页数目，非必传
                "orderSn": self.orderSn  # 订单号
                }
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_otc_order_detail(self):
        """订单详情"""
        server = "otc/order/detail"
        data = {"orderSn": self.orderSn}
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_otc_coin_pcall(self):
        """取得正常的币种"""
        server = "otc/coin/pcall"
        data = {"memberId": self.memberId}
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_otc_coin_all(self):
        server = "otc/coin/all"
        r = request2DKApi(server).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")


if __name__ == "__main__":
    unittest.main()