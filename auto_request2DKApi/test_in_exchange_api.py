# coding:utf-8
# @author : csl
# @date   : 2018/07/25 14:54
# 调用写入类接口

from common.request2DKApi import request2DKApi
import unittest
from common.base import DKApiBase
import time

class DKApiautoTes_exchange_in(unittest.TestCase):
    """exchange写入类接口"""

    def setUp(self):
        self.symbol = "SLB/USDT"

    def tearDown(self):
        pass

    def test_exchange_order_add_buy(self):
        """买入"""
        serverc = "exchange/order/add"
        data = {
                "symbol":self.symbol,
                "price":"0.08",
                "amount":"100",
                "direction":"0",  # 买卖方向，0=BUY（买）/1=SELL（卖）
                "type":"1"  # 交易类型，1=LIMIT_PRICE(限价交易)
                }
        r = request2DKApi(serverc, data).send()
        print(r)
        self.assertRegexpMatches(r[2], "Submit order successfully", "结果断言失败")

    def test_exchange_order_add_sell(self):
        """卖出"""
        serverc = "exchange/order/add"
        data = {
            "symbol": self.symbol,
            "price": "0.08",
            "amount": "100",
            "direction": "1",  # 买卖方向，0=BUY（买）/1=SELL（卖）
            "type": "1"  # 交易类型，1=LIMIT_PRICE(限价交易)
            }
        r = request2DKApi(serverc, data).send()
        print(r)
        self.assertRegexpMatches(r[2], "Submit order successfully", "结果断言失败")

    def test_exchange_favor_add(self):
        """查询用户自选and添加自选and删除自选"""
        # 查询
        serverc = "exchange/favor/find"
        r = request2DKApi(serverc).send()
        print(r)
        # if DKApiBase().str2json(r[2]) is None:
        if self.symbol not in r[2]:
            # 添加
            serverc = "exchange/favor/add"
            data = {"symbol":self.symbol}
            radd = request2DKApi(serverc, data).send()
            print(radd)
        # 删除
        serverc = "exchange/favor/delete"
        data = {"symbol":self.symbol}
        rdel = request2DKApi(serverc, data).send()
        print(rdel)
        self.assertRegexpMatches(rdel[2], '"message":"success"', "结果断言失败")

    def test_exchange_order_cancel(self):
        """添加and取消委托订单"""
        # 添加
        serverc = "exchange/order/add"
        data = {
                "symbol":self.symbol,
                "price":"1.08",
                "amount":"100",
                "direction":"1",  # 买卖方向，0=BUY（买）/1=SELL（卖）
                "type":"1"  # 交易类型，1=LIMIT_PRICE(限价交易)
                }
        r = request2DKApi(serverc, data).send()
        print(serverc, r)
        # 撤销
        orderId = DKApiBase().str2json(r[2])["data"]["orderId"]
        time.sleep(3)  # 避免取消时订单状态不正确
        serverc = "exchange/order/cancel/" + orderId
        rcancel = request2DKApi(serverc).send()
        print(serverc, rcancel)
        self.assertRegexpMatches(rcancel[2], '"message":"Cancel order success"', "结果断言失败")

    def test_exchange_order_add_detail(self):
        """委托and交易撮合and查询委托成交明细"""
        # 添加买入委托订单
        serverc = "exchange/order/add"
        data = {
            "symbol": self.symbol,
            "price": "0.08",
            "amount": "100",
            "direction": "0",  # 买卖方向，0=BUY（买）/1=SELL（卖）
            "type": "1"  # 交易类型，1=LIMIT_PRICE(限价交易)
        }
        r = request2DKApi(serverc, data).send()
        print(r)
        # 添加卖出委托订单
        data_sell = {
            "symbol": self.symbol,
            "price": "0.08",
            "amount": "100",
            "direction": "1",  # 买卖方向，0=BUY（买）/1=SELL（卖）
            "type": "1"  # 交易类型，1=LIMIT_PRICE(限价交易)
        }
        r_transaction = request2DKApi(serverc, data_sell).send()
        print(r_transaction)
        # 查询委托订单成交明细
        orderId = DKApiBase().str2json(r_transaction[2])["data"]["orderId"]
        # print(orderId)
        serverc = "exchange/order/detail/" + orderId
        time.sleep(3)  # 等待订单后台撮合成功
        r_detail = request2DKApi(serverc).send()
        print(r_detail)
        self.assertRegexpMatches(r_detail[2], orderId, "结果断言失败")





if __name__ == "__main__":
    unittest.main()