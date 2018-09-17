# coding:utf-8
# @author : csl
# @date   : 2018/08/09 14:06
# c2c写入类接口

import unittest
from common.request2DKApi import request2DKApi
from common.base import DKApiBase
import time
from common.base_connect_mysql import connect_mysql
from common.baseDatas import *

class DKApiautoTest_c2c_in(unittest.TestCase):
    """c2c写入类接口"""

    def setUp(self):
        self.jyPassword = DKApiBase().getSign("111111" + "hello, moto")  # 用户资金密码
        self.advertPrice = 6.85  # 广告USDT价格
        self.otc_coin_id = 2  # otc_coin表币种ID
        self.header = {"access-auth-token":COMMON_TOKEN_ANOTHER}  # c2c交易用户token,买币的用户需要开通支付方式
        self.amount = 20  # 交易数量

        # 查询用户钱包账户数据
        self.Inquire_member_wallet_sql = '''SELECT coin_id, balance, frozen_balance, lock_balance 
        FROM member_wallet 
        WHERE member_id = (SELECT id FROM member WHERE token = '{}') AND coin_id IN('Silubium', 'USDT');'''.format(COMMON_TOKEN_ANOTHER)

        # 查询可用C2C卖出USDT广告
        self.Inquire_advertise_sql_sale = '''SELECT id, advertise_type, max_limit, min_limit, remain_amount, price, coin_id, member_id 
        FROM advertise 
        WHERE member_id = '74773' AND coin_id = 2 AND `status` = 0 AND advertise_type = 1;'''

        # 查询可用C2C买入USDT广告
        self.Inquire_advertise_sql_buy = """SELECT id, advertise_type, max_limit, min_limit, remain_amount, price, coin_id, member_id 
        FROM advertise 
        WHERE member_id = '74773' AND coin_id = 2 AND `status` = 0 AND advertise_type = 0;"""

    def tearDown(self):

        pass

    def test_otc_advertise_create_update_on_buy_pay_release_off_delete(self):
        """创建买入广告and查询该条广告and修改and上架and卖出交易and确认付款and放币and下架and删除广告"""

        # 创建买入广告
        server = "otc/advertise/create"
        data = {"price":self.advertPrice,
                "advertiseType":"0",  # 0买，1卖
                "coin.id":self.otc_coin_id,
                "minLimit":"100",
                "maxLimit":"1000",
                "timeLimit":"15",
                "country":"中国",
                "priceType":"0",
                "premiseRate":"",
                "remark":"自动脚本添加",
                "number":"10000",
                "pay[]":"微信",
                "auto":"1",
                "autoword":"自动脚本添加",
                "jyPassword":self.jyPassword
                }
        r_buy = request2DKApi(server, data).send()
        print(r_buy)

        # 查询个人所有广告获得最新创建广告
        server = "otc/advertise/all"
        r_Inquire_buy = request2DKApi(server).send()
        print(r_Inquire_buy)
        advertid_buy = DKApiBase().str2json(r_Inquire_buy[2])["data"][0]["id"]  # 从查询接口获取最新发布的这条广告ID

        # 修改广告
        server = "otc/advertise/update"
        data = {"id": advertid_buy,
                "advertiseType": "1",  # 0买，1卖
                "price": self.advertPrice,
                "coin.id": self.otc_coin_id,
                "minLimit": "100",
                "maxLimit": "1000",
                "timeLimit": "20",
                "country": "中国",
                "priceType": "0",
                "premiseRate": "",
                "remark": "自动脚本添加",
                "number": "100000",
                "pay[]": "支付宝",
                "auto": "1",
                "autoword": "自动脚本添加",
                "jyPassword": self.jyPassword
                }
        r_update_buy = request2DKApi(server, data).send()
        print(r_update_buy)

        # 上架
        server = "otc/advertise/on/shelves"
        data = {"id":advertid_buy}
        r_on_buy = request2DKApi(server, data).send()
        print(r_on_buy)

        # 用户卖出
        time.sleep(3)
        server = "otc/order/sell"
        data = {"id": advertid_buy,  # 广告id
                "coinId": self.otc_coin_id,  # 币种id，otc_coin表ID
                "price": self.advertPrice,  # 当前价格
                "money": self.advertPrice * self.amount,  # 金额
                "amount": self.amount,  # 数量
                "remark": "自动脚本测试卖币",  # 要求、备注，非必传
                "mode": ""  # 计算方式，金额/价格=数量为0，数量*价格=金额为1，非必传，默认为0
                }
        r_sale_buy = request2DKApi(server, data, self.header).send()
        print(r_sale_buy)
        orderSn_buy = DKApiBase().str2json(r_sale_buy[2])["data"]  # 下单结果获取交易订单号
        if orderSn_buy is None:
            self.assertRegexpMatches(r_sale_buy[2], '"message" : "创建订单成功"', "创建订单失败")

        # 买家确认付款
        time.sleep(2)
        server = "otc/order/pay"
        data = {"orderSn": orderSn_buy}
        r_pay_buy = request2DKApi(server, data).send()
        print(r_pay_buy)

        # 卖家放币
        time.sleep(2)  # 等待2s避免订单状态更改不及时
        server = "otc/order/release"
        data = {"orderSn": orderSn_buy,
                "jyPassword": self.jyPassword}
        r_rel_buy = request2DKApi(server, data, self.header).send()
        print(r_rel_buy)

        # 下架
        server = "otc/advertise/off/shelves"
        data = {"id": advertid_buy}
        r_off = request2DKApi(server, data).send()
        print(r_off)
        # 删除广告
        server = "otc/advertise/delete"
        data = {"id":advertid_buy}  # 广告ID
        r_del = request2DKApi(server, data).send()
        print(r_del)
        self.assertRegexpMatches(r_del[2], '"message" : "删除成功"', "结果断言失败")

    def test_otc_advertise_create_on_sale_pay_release_off_delete(self):
        """创建卖出广告and查询该条广告and上架and买币交易and确认付款and放币and下架广告and删除广告"""

        # 创建卖出广告
        server = "otc/advertise/create"
        data = {"price": self.advertPrice,
                "advertiseType": "1",  # 0买，1卖
                "coin.id": self.otc_coin_id,
                "minLimit": "100",
                "maxLimit": "1000",
                "timeLimit": "15",
                "country": "中国",
                "priceType": "0",
                "premiseRate": "",
                "remark": "自动脚本添加",
                "number": "10000",
                "pay[]": "微信",
                "auto": "1",
                "autoword": "自动脚本添加",
                "jyPassword": self.jyPassword
                }
        r_sale = request2DKApi(server, data).send()
        print(r_sale)

        # 查询个人所有广告获得最新创建广告
        server = "otc/advertise/all"
        r_Inquire_sale = request2DKApi(server).send()
        print(r_Inquire_sale)
        advertid_sale = DKApiBase().str2json(r_Inquire_sale[2])["data"][0]["id"]  # 从查询接口获取最新发布的这条广告ID

        # 上架
        server = "otc/advertise/on/shelves"
        data = {"id": advertid_sale}
        r_on_sale = request2DKApi(server, data).send()
        print(r_on_sale)

        # 买币交易，不能是广告创建用户自己
        server = "otc/order/buy"
        data = {"id":advertid_sale,  # 广告id
                "coinId":self.otc_coin_id,  # 币种id，otc_coin表ID
                "price":self.advertPrice,  # 当前价格
                "money":self.advertPrice * self.amount,  # 金额
                "amount":self.amount,  # 数量
                "remark":"自动脚本测试买币",  # 要求、备注，非必传
                "mode":""  # 计算方式，金额/价格=数量为0，数量*价格=金额为1，非必传，默认为0
                }
        r_buy_sale = request2DKApi(server, data, self.header).send()
        print(r_buy_sale)
        orderSn_sale = DKApiBase().str2json(r_buy_sale[2])["data"]  # 下单结果获取交易订单号
        if orderSn_sale is None:
            self.assertRegexpMatches(r_buy_sale[2], '"message" : "创建订单成功"', "创建订单失败")

        # 买家确认付款
        server = "otc/order/pay"
        data = {"orderSn":orderSn_sale}
        r_pay_sale = request2DKApi(server, data, self.header).send()
        print(r_pay_sale)

        # 卖家放币
        time.sleep(2)  # 等待2s避免订单状态更改不及时
        server = "otc/order/release"
        data = {"orderSn":orderSn_sale,
                "jyPassword":self.jyPassword}
        r_rel_sale = request2DKApi(server, data).send()
        print(r_rel_sale)

        # 下架广告
        server = "otc/advertise/off/shelves"
        data = {"id": advertid_sale}
        r_off_sale = request2DKApi(server, data).send()
        print(r_off_sale)

        # 删除广告
        server = "otc/advertise/delete"
        data = {"id": advertid_sale}  # 广告ID
        r_del_sale = request2DKApi(server, data).send()
        print(r_del_sale)
        self.assertRegexpMatches(r_del_sale[2], '"message" : "删除成功"', "结果断言失败")

    def test_otc_order_cancel_buy(self):
        """买币取消订单"""

        # # 查询账户余额及冻结余额
        # try:
        #     check_mysql = connect_mysql().connect2mysql(self.Inquire_member_wallet_sql)
        #     parameter_name = ["coin_id", "balance", "frozen_balance", "lock_balance"]  # 查询字段名称拼装成字典形式内容
        #     before_member_wallet = DKApiBase().mysqlResultFormat(check_mysql, parameter_name)
        #     # print(before_member_wallet)
        #     before_Silubium_balance = before_member_wallet[0]["balance"]  # 变动前slb余额
        #     before_Silubium_frozen_balance = before_member_wallet[0]["frozen_balance"]  # 变动前slb冻结余额
        #     berore_USDT_balance = before_member_wallet[1]["balance"]  # 变动前USDT余额
        # except Exception as e:
        #     print("账户信息查询出错{}".format(e))

        # 查询可用c2c卖出USDT广告
        try:
            using_advertise = connect_mysql().connect2mysql(self.Inquire_advertise_sql_sale)
            # 处理查询结果
            parameter_name = ["id", "advertise_type", "max_limit", "min_limit", "remain_amount", "price", "coin_id", "member_id"]
            advertise_data = DKApiBase().mysqlResultFormat(using_advertise, parameter_name)[0]
        except Exception as e:
            print("可用C2C广告信息查询出错{}".format(e))
            self.assertTrue(False, "查询可用广告失败")

        # 用户买入订单
        server = "otc/order/buy"
        data = {"id":advertise_data["id"],  # 广告id
                "coinId":advertise_data["coin_id"],  # 币种id，otc_coin表ID
                "price":advertise_data["price"],  # 当前价格
                "money":self.amount * advertise_data["price"],  # 金额
                "amount":self.amount,  # 数量
                "remark":"自动脚本测试买币",  # 要求、备注，非必传
                "mode":""  # 计算方式，金额/价格=数量为0，数量*价格=金额为1，非必传，默认为0
                }
        r_cancel_buy = request2DKApi(server, data, self.header).send()
        print(r_cancel_buy)

        # 用户取消买入订单
        orderSn_cancel_buy = DKApiBase().str2json(r_cancel_buy[2])["data"]  # 下单结果获取交易订单号
        server = "otc/order/cancel"
        data = {"orderSn": orderSn_cancel_buy}
        r_cancel = request2DKApi(server, data, self.header).send()
        print(r_cancel)
        self.assertRegexpMatches(r_cancel[2], '"message" : "取消成功"', "结果断言失败")

    def test_otc_order_cancel_sale(self):
        """卖币取消订单"""

        # 查询可用c2c买入USDT广告
        try:
            using_advertise = connect_mysql().connect2mysql(self.Inquire_advertise_sql_buy)
            # 处理查询结果
            parameter_name = ["id", "advertise_type", "max_limit", "min_limit", "remain_amount", "price", "coin_id", "member_id"]
            advertise_data = DKApiBase().mysqlResultFormat(using_advertise, parameter_name)[0]
        except Exception as e:
            print("可用C2C广告信息查询出错{}".format(e))
            self.assertTrue(False, "查询可用广告失败")

        # 用户卖出订单
        server = "otc/order/sell"
        data = {"id":advertise_data["id"],  # 广告id
                "coinId":advertise_data["coin_id"],  # 币种id，otc_coin表ID
                "price":advertise_data["price"],  # 当前价格
                "money":advertise_data["price"] * self.amount,  # 金额
                "amount":self.amount,  # 数量
                "remark":"测试卖币",  # 要求、备注，非必传
                "mode":""  # 计算方式，金额/价格=数量为0，数量*价格=金额为1，非必传，默认为0
                }
        r_cancel_sale = request2DKApi(server, data, self.header).send()
        print(r_cancel_sale)

        # 用户取消买入订单（发起买入USDT的商家）
        orderSn_cancel_sale = DKApiBase().str2json(r_cancel_sale[2])["data"]  # 下单结果获取交易订单号
        server = "otc/order/cancel"
        data = {"orderSn": orderSn_cancel_sale}
        r_cancel = request2DKApi(server, data).send()
        print(r_cancel)
        self.assertRegexpMatches(r_cancel[2], '"message" : "取消成功"', "结果断言失败")




