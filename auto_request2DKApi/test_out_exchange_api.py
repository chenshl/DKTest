# coding:utf-8
# @author : csl
# @date   : 2018/07/25 10:13
# 调用查询类接口

import unittest
from common.request2DKApi import request2DKApi
from common.base import DKApiBase
from common.base_connect_mysql import connect_mysql

class DKApiautoTest_exchange_out(unittest.TestCase):
    """exchange查询类接口"""

    def setUp(self):

        # 获取订单明细接口订单号
        self.exchange_order_orderInfo_sql = '''SELECT order_id FROM exchange_order 
        WHERE member_id = '74773' AND completed_time IS NOT NULL ORDER BY completed_time DESC LIMIT 5;'''  # 查询最近成交的订单号
        try:
            # 获取查询到的第一条订单号
            self.exchange_order_orderInfo = DKApiBase().mysqlResultFormat(connect_mysql().connect2mysql(self.exchange_order_orderInfo_sql), ["order_id"])[0]["order_id"]
        except Exception as e:
            print("获取订单明细查询订单号错误{}".format(e))

        self.announcementID = "8"  # 公告内容接口公告ID
        self.coinId = "6"  # 获取制定币种接口币种ID
        self.coinName = "SLB"  # 资产查询接口币种ID
        self.symbol = "SLB/USDT"  # 币种对
        self.fromdate = "2018-07-23 00:00:00"  # 查询K线数据起始时间


    def tearDown(self):
        pass

    def test_current(self):
        """查询当前委托订单接口"""
        serverc = "exchange/order/current"
        data = {"symbol":self.symbol,
                "pageNo":"0",  # 请求开始页码，从0开始
                "pageSize":"100"  # 请求数量
                }
        r = request2DKApi(serverc, data).send()
        print(r)
        self.assertRegexpMatches(r[2], "content", "结果断言失败")

    def test_history(self):
        """查询历史委托订单接口"""
        serverc = "exchange/order/history"
        data = {"symbol":self.symbol,
                "pageNo":"0",
                "pageSize":"10"
                }
        r = request2DKApi(serverc, data).send()
        print(r)
        self.assertRegexpMatches(r[2], "content", "结果断言失败")  # 正则表达是匹配比较结果断言


    def test_symbol_info(self):
        """获取指定交易对的配置信息接口"""
        serverc = "market/symbol-info"
        data = {"symbol":self.symbol}
        r = request2DKApi(serverc, data).send()
        print(r)
        self.assertRegexpMatches(r[2], self.symbol, "结果断言失败")

    def test_symbol(self):
        """获取所有交易对信息接口"""
        serverc = "market/symbol"
        # data = {}
        r = request2DKApi(serverc).send()
        print(r)
        self.assertIsNotNone(r[2], "返回数据为空")

    def test_symbol_thumb(self):
        """获取所有交易对的当前行情信息接口"""
        serverc = "market/symbol-thumb"
        r = request2DKApi(serverc).send()
        print(r)
        self.assertIsNotNone(r[2], "返回数据为空")

    def test_market_history(self):
        """获取K线数据接口"""
        serverc = "market/history"
        data = {"symbol":self.symbol,
                "from":DKApiBase().time2Timestamps(self.fromdate),  # 开始时间戳
                "to":DKApiBase().nowtime2Timestamps(),  # 截至时间戳
                "resolution":"15"  # K线类型：1=1分/5=5分/15=15分/30=30分/1h=小时/1d=天/1m=月
                }
        r = request2DKApi(serverc, data).send()
        print(r)
        self.assertIsNotNone(r[2], "返回数据为空")

    def test_exchange_plate(self):
        """获取买卖盘口信息接口"""
        serverc = "market/exchange-plate"
        data = {"symbol": self.symbol}
        r = request2DKApi(serverc, data).send()
        print(r)
        self.assertRegexpMatches(r[2], "ask", "结果断言失败")

    def test_latest_trade(self):
        """获取最新实时成交记录接口"""
        serverc = "market/latest-trade"
        data = {"symbol":self.symbol,
                "size":"50"  # 记录数量
                }
        r = request2DKApi(serverc, data).send()
        print(r)
        self.assertRegexpMatches(r[2], self.symbol, "结果断言失败")

    def test_uc_asset_wallet(self):
        """资产查询接口，币种名称加在请求路径后面"""
        serverc = "uc/asset/wallet/" + self.coinName
        r = request2DKApi(serverc).send()
        print(r)
        self.assertRegexpMatches(r[2], "message", "结果断言失败")

    def test_uc_ancillary_system_help_all(self):
        """币种资料列表查询接口"""
        serverc = "uc/ancillary/system/help"
        data = {"sysHelpClassification":"COIN_INFO"}
        r = request2DKApi(serverc, data).send()
        print(r)
        self.assertRegexpMatches(r[2], "message", "结果断言失败")

    def test_uc_ancillary_system_help(self):
        """获取指定币种资料"""
        serverc = "uc/ancillary/system/help/" + self.coinId
        r = request2DKApi(serverc).send()
        print(r)
        self.assertRegexpMatches(r[2], '"id" : {}'.format(self.coinId), "结果断言失败")

    def test_uc_announcement_page(self):
        """公告列表查询接口"""
        serverc = "uc/announcement/page"
        data = {"pageNo":"1",
                "pageSize":"10"
                }
        r = request2DKApi(serverc, data).send()
        print(r)
        self.assertRegexpMatches(r[2], "message", "结果断言失败")

    def test_uc_announcement(self):
        """获取公告内容"""
        requestMark = "GET"
        serverc = "uc/announcement/" + self.announcementID
        r = request2DKApi(serverc).send(requestMark)
        print(r)
        self.assertRegexpMatches(r[2], '"id" : {}'.format(self.announcementID), "结果断言失败")

    def test_exchange_order_orderInfo(self):
        """订单明细查询接口"""
        serverc = "exchange/order/orderInfo"
        data = {"orderId":self.exchange_order_orderInfo
                }
        r = request2DKApi(serverc, data).send()
        print(r)
        self.assertRegexpMatches(r[2], self.exchange_order_orderInfo, "结果断言失败")

    def test_exchange_exchange_coin_base_symbol(self):
        """获取基币"""
        serverc = "exchange/exchange-coin/base-symbol"
        r = request2DKApi(serverc).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message":"SUCCESS"', "结果断言失败")

    def test_exchange_favor_find(self):
        """查询当前用户自选"""
        serverc = "exchange/favor/find"
        r = request2DKApi(serverc).send()
        print(r)
        if not r[2]:  # 判断r[2]返回结果不为空
            print("该用户未添加自选商品")
            self.assertIsNone(r[2], "该用户自选商品不为空")
        else:
            print("该用户的自选商品查询结果为：{}".format(r[2]))
            self.assertIsNotNone(r[2], "该用户自选商品为空")

    def test_exchange_order_detail(self):
        """查询委托成交明细"""
        serverc = "exchange/order/detail/" + self.exchange_order_orderInfo
        r = request2DKApi(serverc).send()
        print(r)
        if self.exchange_order_orderInfo not in r[2]:
            print("未查询到 {} 订单的成交明细".format(self.exchange_order_orderInfo))
            self.assertTrue(False, "未查询到该条订单明细{}".format(self.exchange_order_orderInfo))
        else:
            print("订单 {} 成交明细查询正确".format(self.exchange_order_orderInfo))
            self.assertRegexpMatches(r[2], self.exchange_order_orderInfo, "结果断言失败")





if __name__ == "__main__":
    unittest.main()
