# coding:utf-8
# @author : csl
# @date   : 2018/08/09 14:06
# c2c写入类接口

import unittest
import time
from common.request2DKApi import request2DKApi
from common.base import DKApiBase
from common.base_connect_mysql import connect_mysql
from common.baseDatas import *
from common.writelog_up import WriteLogger

logger = WriteLogger().getLogger()

class DKApiautoTest_c2c_in(unittest.TestCase):
    """c2c写入类接口"""

    @classmethod
    def setUpClass(cls):
        cls.jyPassword = DKApiBase().getSign("111111" + "hello, moto")  # 用户资金密码
        cls.advertcoin_CNYT = "CNYT"  # 广告币种
        cls.walletcion_SLU = "SLU"  # 钱包账户币种
        cls.advertPrice_USDT = 6.85  # 广告USDT价格
        cls.advertPrice_CNYT = 1  # 广告USDT价格
        cls.otc_coin_id_USDT = 2  # otc_coin表币种ID
        cls.otc_coin_id_CNYT = 13  # otc_coin表币种ID
        cls.otc_number = 1000
        cls.header = {"access-auth-token":COMMON_TOKEN_ANOTHER}  # c2c交易用户token,买币的用户需要开通支付方式
        cls.header_general = {"access-auth-token":COMMON_TOKEN_GENERAL_USER}  # c2c非认证商家广告方
        cls.header_general_user = {"access-auth-token":COMMON_TOKEN_GENERAL_USER_ANOTHER}  # c2c非认证商家交易方
        cls.amount = 100  # 交易数量

        # 查询商家认证状态
        cls.member_level_sql = '''SELECT member_level FROM member WHERE token = '{}';'''.format(COMMON_TOKEN_ANOTHER)

        # 查询商家钱包账户数据-CNYT
        cls.inquire_Merchant_wallet_CNYT_sql = '''SELECT coin_id, balance, frozen_balance, lock_balance 
        FROM member_wallet 
        WHERE member_id = (SELECT id FROM member WHERE token = '{}') AND coin_id = 'CNYT';'''.format(COMMON_TOKEN)
        # 查询商家钱包账户数据-SLU
        cls.inquire_Merchant_wallet_SLU_sql = '''SELECT coin_id, balance, frozen_balance, lock_balance 
        FROM member_wallet 
        WHERE member_id = (SELECT id FROM member WHERE token = '{}') AND coin_id = 'SLU';'''.format(COMMON_TOKEN)

        # 查询用户钱包账户数据
        cls.inquire_member_wallet_CNYT_sql = '''SELECT coin_id, balance, frozen_balance, lock_balance 
        FROM member_wallet 
        WHERE member_id = (SELECT id FROM member WHERE token = '{}') AND coin_id = 'CNYT';'''.format(COMMON_TOKEN_ANOTHER)

        # 查询可用C2C卖出USDT广告
        cls.Inquire_advertise_sql_sale = '''SELECT id, advertise_type, max_limit, min_limit, remain_amount, price, coin_id, member_id 
        FROM advertise 
        WHERE member_id = '74773' AND coin_id = 2 AND `status` = 0 AND advertise_type = 1;'''

        # 查询可用C2C买入USDT广告
        cls.Inquire_advertise_sql_buy = """SELECT id, advertise_type, max_limit, min_limit, remain_amount, price, coin_id, member_id 
        FROM advertise 
        WHERE member_id = '74773' AND coin_id = 2 AND `status` = 0 AND advertise_type = 0;"""

    def tearDown(self):

        pass

    def test_otc_advertise_create_update_on_buy_pay_release_off_delete(self):
        """创建买入广告and查询该条广告and修改and上架and卖出交易and确认付款and放币and下架and删除广告"""

        # 创建买入广告
        server = "otc/advertise/create"
        data = {"price":self.advertPrice_USDT,
                "advertiseType":"0",  # 0买，1卖
                "coin.id":self.otc_coin_id_USDT,
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
                "price": self.advertPrice_USDT,
                "coin.id": self.otc_coin_id_USDT,
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
                "coinId": self.otc_coin_id_USDT,  # 币种id，otc_coin表ID
                "price": self.advertPrice_USDT,  # 当前价格
                "money": self.advertPrice_USDT * self.amount,  # 金额
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

    def test_otc_advertise_merchant_sells(self):
        """认证商家卖出广告并核对用户账户数据变更：1.创建卖出广告2.查询该条广告3.上架4.买币交易5.确认付款6.放币7.下架广告8.删除广告"""

        # 查询商家认证状态：0为普通用户；1为实名认证用户；2为认证商家
        logger.info("------执行test_otc_advertise_merchant_sells------")
        try:
            user_member_lever = connect_mysql().connect2mysql(self.member_level_sql)[0][0]
        except Exception as e:
            print(e)
            logger.error(e)
            user_member_lever = 0

        if user_member_lever == 2:

            # 查询商家用户钱包账户数据
            inquire_Merchant_member_wallet = connect_mysql().connect2mysql(self.inquire_Merchant_wallet_CNYT_sql)
            inquire_Merchant_member_wallet_list = DKApiBase().mysqlResultFormat(inquire_Merchant_member_wallet, ["coin_id", "balance", "frozen_balance", "lock_balance"])

            # 创建卖出广告
            server = "otc/advertise/create"
            data = {
                    "price": self.advertPrice_CNYT,
                    "advertiseType": "1",  # 0买，1卖
                    "coin.id": self.otc_coin_id_CNYT,
                    "minLimit": "100",
                    "maxLimit": "1000",
                    "timeLimit": "30",
                    "country": "中国",
                    "priceType": "0",
                    "premiseRate": "",
                    "remark": "认证商家卖出广告,自动化脚本添加",
                    "number": self.otc_number,
                    "pay[]": "银联",
                    "auto": "1",  # 是否开启自动回复0否1是，默认否
                    "autoword": "先付款，后放币",
                    "needBindPhone": "1",  # 是否需要交易方已绑定手机号，0：不需要，1：需要
                    "needRealname": "1",  # 是否需要交易方已做实名认证，0：不需要，1：需要
                    "needTradeTimes": "10",  # 需要交易方至少完成过N笔交易（默认为0）
                    "needPutonDiscount": "1",  # 是否使用优惠币种支付，0：不使用，1：使用
                    "bindingResult": "",  # 绑定结果,非必传项
                    "jyPassword": self.jyPassword
                    }
            r_sale = request2DKApi(server, data).send()
            print(r_sale)

            # 查询商家账户数据，提交广告时不扣除账户币种数据
            inquire_Merchant_member_wallet = connect_mysql().connect2mysql(self.inquire_Merchant_wallet_CNYT_sql)
            inquire_Merchant_member_wallet_list_add = DKApiBase().mysqlResultFormat(inquire_Merchant_member_wallet, ["coin_id", "balance", "frozen_balance", "lock_balance"])

            # 判断添加广告后商家账户余额是否发生变动，如变动证明数据有问题则不执行后续操作
            if inquire_Merchant_member_wallet_list["balance"] == inquire_Merchant_member_wallet_list_add["balance"] \
                    and inquire_Merchant_member_wallet_list["frozen_balance"] == inquire_Merchant_member_wallet_list_add["frozen_balance"]:

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

                # 查询商家上架后账户数据，上架广告认证商家不扣除广告费用
                inquire_Merchant_member_wallet = connect_mysql().connect2mysql(self.inquire_Merchant_wallet_CNYT_sql)
                inquire_Merchant_member_wallet_list_shelf = DKApiBase().mysqlResultFormat(inquire_Merchant_member_wallet, ["coin_id", "balance", "frozen_balance", "lock_balance"])

                # 商家上架广告后可用余额计算：原可用余额-广告金额
                merchant_coin_shelf_balance = inquire_Merchant_member_wallet_list_add["balance"] - self.otc_number
                # 商家上架广告后冻结余额计算：原冻结余额+广告金额
                merchant_coin_shelf_forzen_balance = inquire_Merchant_member_wallet_list_add["frozen_balance"] + self.otc_number

                # 判断商家账户冻结等于广告冻结数量
                logger.info("上架前商家账户可用余额：{}".format(inquire_Merchant_member_wallet_list["balance"]))
                logger.info("上架后商家账户可用余额：{}".format(inquire_Merchant_member_wallet_list_shelf["balance"]))
                logger.info("上架前商家账户冻结余额：{}".format(inquire_Merchant_member_wallet_list["frozen_balance"]))
                logger.info("上架后商家账户冻结余额：{}".format(inquire_Merchant_member_wallet_list_shelf["frozen_balance"]))

                if inquire_Merchant_member_wallet_list_shelf["balance"] == merchant_coin_shelf_balance \
                        and inquire_Merchant_member_wallet_list_shelf["frozen_balance"] == merchant_coin_shelf_forzen_balance:

                    # 查询交易方用户交易前账户数据
                    inquire_user_member_wallet = connect_mysql().connect2mysql(self.inquire_member_wallet_CNYT_sql)
                    inquire_user_member_wallet_list = DKApiBase().mysqlResultFormat(inquire_user_member_wallet, ["coin_id", "balance", "frozen_balance", "lock_balance"])

                    # 买币交易，不能是广告创建用户自己
                    server = "otc/order/buy"
                    data = {"id":advertid_sale,  # 广告id
                            "coinId":self.otc_coin_id_CNYT,  # 币种id，otc_coin表ID
                            "price":self.advertPrice_CNYT,  # 当前价格
                            "money":self.advertPrice_CNYT * self.amount,  # 金额
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

                    # 查询交易方用户交易后账户
                    inquire_user_member_wallet = connect_mysql().connect2mysql(self.inquire_member_wallet_CNYT_sql)
                    inquire_user_member_wallet_list_shelf = DKApiBase().mysqlResultFormat(inquire_user_member_wallet, ["coin_id", "balance", "frozen_balance", "lock_balance"])
                    # 查询广告方交易后账户
                    inquire_Merchant_member_wallet = connect_mysql().connect2mysql(self.inquire_Merchant_wallet_CNYT_sql)
                    inquire_Merchant_member_wallet_list_transaction = DKApiBase().mysqlResultFormat(inquire_Merchant_member_wallet, ["coin_id", "balance", "frozen_balance", "lock_balance"])
                    # 根据订单号查询订单交易信息
                    otc_order_datas = connect_mysql().connect2mysql('''SELECT id, advertise_id, commission, number, member_id, customer_id, `status`  FROM otc_order WHERE order_sn = '120480325817208832';''')
                    otc_order_datas_list = DKApiBase().mysqlResultFormat(otc_order_datas, ["id", "advertise_id", "commission", "number", "member_id", "customer_id", "status"])

                    # 卖出广告广告方资金流向：账户冻结金额-订单金额-订单手续费
                    merchant_coin_after = inquire_Merchant_member_wallet_list_shelf["frozen_balance"] - otc_order_datas_list["commission"] - otc_order_datas_list["number"]
                    # 卖出广告交易方资金流向：账户余额+订单金额
                    user_coin_after = inquire_user_member_wallet_list["balance"] + otc_order_datas_list["number"]
                    # 判断放币后交易方及广告方账户数据
                    if inquire_Merchant_member_wallet_list_transaction["frozen_balance"] == merchant_coin_after and inquire_user_member_wallet_list_shelf["balance"] == user_coin_after:
                        logger.info("交易前商家冻结金额：{}；交易后商家冻结金额：{}".format(inquire_Merchant_member_wallet_list_shelf["frozen_balance"],
                                                                       inquire_Merchant_member_wallet_list_transaction["frozen_balance"]))
                        logger.info("交易前用户冻结金额：{}；交易后用户冻结金额：{}".format(inquire_user_member_wallet_list["balance"], inquire_user_member_wallet_list_shelf["balance"]))

                        # 查询广告剩余数量  advertid_sale
                        advert_datas = connect_mysql().connect2mysql('''SELECT remain_amount, `status` FROM advertise WHERE id = {};'''.format(advertid_sale))
                        advert_datas_list_num = DKApiBase().mysqlResultFormat(advert_datas, ["remain_amount", "status"])

                        # 下架广告
                        server = "otc/advertise/off/shelves"
                        data = {"id": advertid_sale}
                        r_off_sale = request2DKApi(server, data).send()
                        print(r_off_sale)

                        # 查询下架广告后商家账户数据,同下架广告前进行对比
                        merchant_coin_end_wallet = connect_mysql().connect2mysql(self.inquire_Merchant_wallet_CNYT_sql)
                        merchant_coin_end_wallet_list = DKApiBase().mysqlResultFormat(merchant_coin_end_wallet, ["coin_id", "balance", "frozen_balance", "lock_balance"])

                        # 商家可用余额计算：原可用余额+广告剩余数量
                        merchant_coin_end_balance = inquire_Merchant_member_wallet_list_transaction["balance"] + advert_datas_list_num["remain_amount"]
                        # 商家冻结余额计算：原冻结余额-广告剩余数量
                        merchant_coin_end_forzen_balance = inquire_Merchant_member_wallet_list_transaction["frozen_balance"] - advert_datas_list_num["remain_amount"]

                        # 查询下架后广告状态
                        advert_datas = connect_mysql().connect2mysql('''SELECT remain_amount, `status` FROM advertise WHERE id = {};'''.format(advertid_sale))
                        advert_datas_list_stauts = DKApiBase().mysqlResultFormat(advert_datas, ["remain_amount", "status"])

                        # 判断下架后商家账户数据，商家下架卖出广告资金流向：冻结金额-广告剩余数量；可用币数+广告剩余数量
                        if merchant_coin_end_wallet_list["balance"] == merchant_coin_end_balance and merchant_coin_end_wallet_list["frozen_balance"] == merchant_coin_end_forzen_balance:
                            if advert_datas_list_stauts["status"] == 1:
                                print("广告{}为下架状态，可执行最后一步删除操作".format(advertid_sale))
                            else:
                                logger.error("广告{}状态{}不正确，不能删除；0=上架/1=下架/2=已关闭（删除）".format(advertid_sale, advert_datas_list_stauts["status"]))
                                print("广告{}状态{}不正确，不能删除；0=上架/1=下架/2=已关闭（删除）".format(advertid_sale, advert_datas_list_stauts["status"]))
                        else:
                            logger.error("下架广告{}后发布者账户数据核对不正确".format(advertid_sale))
                            print("下架广告{}后发布者账户数据核对不正确".format(advertid_sale))
                    else:
                        logger.error("交易后账户数据不一致")
                        print("交易后账户数据不一致")
                else:
                    logger.error("上架广告后商家账户余额不正确")
                    print("上架广告后商家账户余额不正确")
            else:
                logger.error("添加广告后该商家账户余额已经发生变动，请检测")
                print("添加广告后该商家账户余额已经发生变动，请检测")
        else:
            logger.info("该用户不是认证商家")
            print("该用户不是认证商家")

        # 最后执行删除广告的业务，如果前面业务失败，则删除广告业务断言抛出异常
        server = "otc/advertise/delete"
        data = {"id": advertid_sale}  # 广告ID
        r_del_sale = request2DKApi(server, data).send()
        print(r_del_sale)
        self.assertRegexpMatches(r_del_sale[2], '"message" : "删除成功"', "结果断言失败")

    def test_otc_advertise_merchant_buy(self):
        """认证商家买入广告并核对用户账户数据变更：1.创建买入广告2.查询该条广告3.上架4.买币交易5.确认付款6.放币7.下架广告8.删除广告"""

        # 查询商家认证状态：0为普通用户；1为实名认证用户；2为认证商家
        logger.info("------执行test_otc_advertise_merchant_buy------")
        try:
            user_member_lever = connect_mysql().connect2mysql(self.member_level_sql)[0][0]
        except Exception as e:
            print(e)
            logger.error(e)
            user_member_lever = 0

        if user_member_lever == 2:

            # 查询商家用户钱包账户数据
            inquire_Merchant_member_wallet = connect_mysql().connect2mysql(self.inquire_Merchant_wallet_CNYT_sql)
            inquire_Merchant_member_wallet_list = DKApiBase().mysqlResultFormat(inquire_Merchant_member_wallet, ["coin_id", "balance", "frozen_balance", "lock_balance"])

            # 创建买入广告
            server = "otc/advertise/create"
            data = {
                    "price": self.advertPrice_CNYT,
                    "advertiseType": "0",  # 0买，1卖
                    "coin.id": self.otc_coin_id_CNYT,
                    "minLimit": "100",
                    "maxLimit": "1000",
                    "timeLimit": "30",
                    "country": "中国",
                    "priceType": "0",
                    "premiseRate": "",
                    "remark": "认证商家买入广告,自动化脚本添加",
                    "number": self.otc_number,
                    "pay[]": "银联",
                    "auto": "1",  # 是否开启自动回复0否1是，默认否
                    "autoword": "先付款，后放币",
                    "needBindPhone": "1",  # 是否需要交易方已绑定手机号，0：不需要，1：需要
                    "needRealname": "1",  # 是否需要交易方已做实名认证，0：不需要，1：需要
                    "needTradeTimes": "10",  # 需要交易方至少完成过N笔交易（默认为0）
                    "needPutonDiscount": "1",  # 是否使用优惠币种支付，0：不使用，1：使用
                    "bindingResult": "",  # 绑定结果,非必传项
                    "jyPassword": self.jyPassword
                    }
            r_sale = request2DKApi(server, data).send()
            print(r_sale)

            # 查询商家账户数据，提交广告时不扣除账户币种数据
            inquire_Merchant_member_wallet = connect_mysql().connect2mysql(self.inquire_Merchant_wallet_CNYT_sql)
            inquire_Merchant_member_wallet_list_add = DKApiBase().mysqlResultFormat(inquire_Merchant_member_wallet, ["coin_id", "balance", "frozen_balance", "lock_balance"])

            # 判断添加广告后商家账户余额是否发生变动，如变动证明数据有问题则不执行后续操作
            if inquire_Merchant_member_wallet_list["balance"] == inquire_Merchant_member_wallet_list_add["balance"] \
                    and inquire_Merchant_member_wallet_list["frozen_balance"] == inquire_Merchant_member_wallet_list_add["frozen_balance"]:
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

                # 查询商家上架后账户数据，上架广告认证商家不扣除广告费用
                inquire_Merchant_member_wallet = connect_mysql().connect2mysql(self.inquire_Merchant_wallet_CNYT_sql)
                inquire_Merchant_member_wallet_list_shelf = DKApiBase().mysqlResultFormat(inquire_Merchant_member_wallet, ["coin_id", "balance", "frozen_balance", "lock_balance"])

                # 判断认证商家上架买入广告后可用余额及冻结余额不变
                if inquire_Merchant_member_wallet_list["balance"] == inquire_Merchant_member_wallet_list_shelf["balance"] \
                        and inquire_Merchant_member_wallet_list["frozen_balance"] == inquire_Merchant_member_wallet_list_shelf["frozen_balance"]:

                    # 查询交易方用户交易前账户数据
                    inquire_user_member_wallet = connect_mysql().connect2mysql(self.inquire_member_wallet_CNYT_sql)
                    inquire_user_member_wallet_list = DKApiBase().mysqlResultFormat(inquire_user_member_wallet, ["coin_id", "balance", "frozen_balance", "lock_balance"])

                    # 卖币交易，不能是广告创建用户自己
                    server = "otc/order/sell"
                    data = {"id": advertid_sale,  # 广告id
                            "coinId": self.otc_coin_id_CNYT,  # 币种id，otc_coin表ID
                            "price": self.advertPrice_CNYT,  # 当前价格
                            "money": self.advertPrice_CNYT * self.amount,  # 金额
                            "amount": self.amount,  # 数量
                            "remark": "自动脚本测试卖币",  # 要求、备注，非必传
                            "mode": ""  # 计算方式，金额/价格=数量为0，数量*价格=金额为1，非必传，默认为0
                            }
                    r_sale = request2DKApi(server, data, self.header).send()
                    print(r_sale)
                    orderSn_sale = DKApiBase().str2json(r_sale[2])["data"]  # 下单结果获取交易订单号
                    if orderSn_sale is None:
                        self.assertRegexpMatches(r_sale[2], '"message" : "创建订单成功"', "创建订单失败")

                    # 查询交易方提交买币订单后的账户数据
                    inquire_user_member_wallet = connect_mysql().connect2mysql(self.inquire_member_wallet_CNYT_sql)
                    inquire_user_member_wallet_list_addorder = DKApiBase().mysqlResultFormat(inquire_user_member_wallet, ["coin_id", "balance", "frozen_balance", "lock_balance"])

                    # 交易方用户可用余额计算：原可用余额-交易数量
                    user_coin_balance = inquire_user_member_wallet_list["balance"] - self.amount
                    # 交易方用户冻结余额计算：原冻结余额+交易数量
                    user_coin_frozen_balance = inquire_user_member_wallet_list["frozen_balance"] + self.amount

                    # 判断交易用户提交卖出订单后账户冻结金额
                    if inquire_user_member_wallet_list_addorder["balance"] == user_coin_balance and inquire_user_member_wallet_list_addorder["frozen_balance"] == user_coin_frozen_balance:

                        # 广告商家确认付款
                        server = "otc/order/pay"
                        data = {"orderSn": orderSn_sale}
                        r_pay_sale = request2DKApi(server, data).send()
                        print(r_pay_sale)

                        # 交易用户放币
                        time.sleep(2)  # 等待2s避免订单状态更改不及时
                        server = "otc/order/release"
                        data = {"orderSn": orderSn_sale,
                                "jyPassword": self.jyPassword}
                        r_rel_sale = request2DKApi(server, data, self.header).send()
                        print(r_rel_sale)

                        # 查询放币后广告商家账户数据
                        inquire_Merchant_member_wallet = connect_mysql().connect2mysql(self.inquire_Merchant_wallet_CNYT_sql)
                        inquire_Merchant_member_wallet_list_transaction = DKApiBase().mysqlResultFormat(inquire_Merchant_member_wallet, ["coin_id", "balance", "frozen_balance", "lock_balance"])
                        # 查询放币后交易方账户数据
                        inquire_user_member_wallet = connect_mysql().connect2mysql(self.inquire_member_wallet_CNYT_sql)
                        inquire_user_member_wallet_list_transaction = DKApiBase().mysqlResultFormat(inquire_user_member_wallet, ["coin_id", "balance", "frozen_balance", "lock_balance"])
                        # 查询交易订单数据
                        otc_order_datas = connect_mysql().connect2mysql('''SELECT id, advertise_id, commission, number, member_id, customer_id, `status`  FROM otc_order WHERE order_sn = '{}';'''.format(orderSn_sale))
                        otc_order_datas_list = DKApiBase().mysqlResultFormat(otc_order_datas, ["id", "advertise_id", "commission",  "number", "member_id", "customer_id", "status"])

                        # 商家可用余额计算：原有可用余额+订单金额-交易手续费
                        merchant_coin_balance = inquire_Merchant_member_wallet_list["balance"] + otc_order_datas_list["number"] - otc_order_datas_list["commission"]
                        # 用户可用冻结余额计算：原有冻结余额-订单金额
                        user_coin_frozen_balance_after = inquire_user_member_wallet_list_addorder["frozen_balance"] - otc_order_datas_list["number"]

                        if inquire_Merchant_member_wallet_list_transaction["balance"] == merchant_coin_balance \
                                and inquire_user_member_wallet_list_transaction["frozen_balance"] == user_coin_frozen_balance_after:

                            # 下架广告
                            server = "otc/advertise/off/shelves"
                            data = {"id": advertid_sale}
                            r_off_sale = request2DKApi(server, data).send()
                            print(r_off_sale)

                            # 查询下架广告后商家账户数据,同下架广告前进行对比
                            merchant_coin_end_wallet = connect_mysql().connect2mysql(self.inquire_Merchant_wallet_CNYT_sql)
                            merchant_coin_end_wallet_list = DKApiBase().mysqlResultFormat(merchant_coin_end_wallet, ["coin_id", "balance", "frozen_balance", "lock_balance"])

                            # 下架卖出广告不影响商家账户可用余额和冻结金额
                            if inquire_Merchant_member_wallet_list_transaction["balance"] == merchant_coin_end_wallet_list["balance"] \
                                    and inquire_Merchant_member_wallet_list_transaction["frozen_balance"] == merchant_coin_end_wallet_list["frozen_balance"]:
                                print("下架买入广告后商家用户账户数据不变，可以继续后续操作")
                            else:
                                logger.error("下架买入广告后商家用户账户数据发生变化，错误")
                                print("下架买入广告后商家用户账户数据发生变化，错误")
                        else:
                            logger.error("放币后用户账户金额不正确")
                            print("放币后用户账户金额不正确")
                    else:
                        logger.error("交易用户冻结账户金额不正确")
                        print("交易用户冻结账户金额不正确")
                else:
                    logger.error("上架广告后商家账户余额不正确")
                    print("上架广告后商家账户余额不正确")
            else:
                logger.error("添加广告后该商家账户余额已经发生变动，请检测")
                print("添加广告后该商家账户余额已经发生变动，请检测")
        else:
            logger.info("该用户不是认证商家")
            print("该用户不是认证商家")

        # 最后走删除广告的业务，如果前面业务失败，则删除广告业务断言抛出异常
        server = "otc/advertise/delete"
        data = {"id": advertid_sale}  # 广告ID
        r_del_sale = request2DKApi(server, data).send()
        print(r_del_sale)
        self.assertRegexpMatches(r_del_sale[2], '"message" : "删除成功"', "结果断言失败")

    def test_otc_advertise_generaluser_sells(self):
        """普通用户卖出广告并核对用户账户数据：1.创建广告，2.上架广告，3.交易广告，4.商家放币，5.交易广告，6.用户申述，7.用户胜出，
        8.用户申述，9.广告方胜出，10.广告方申述，11.用户胜出，12.广告方申述，13.广告方胜出，14.下架广告，15.删除广告"""

        # 查询申述风险配置，如设置允许申述次数小于4次，会导致测试账号被锁，则需先修改后台风控配置再执行
        safe_mark = 0
        user_risk_config = connect_mysql().connect2mysql("""SELECT trigger_times FROM monitor_rule_config WHERE trigger_event = 11;""")
        for user_config in  user_risk_config:
            for user_risk in user_config:
                if user_risk <= 10:
                    safe_mark = 1
        if safe_mark == 1:
            # 执行数据库更新操作，安全设置
            connect_mysql().connect2mysql("""UPDATE monitor_rule_config SET trigger_times = 30 WHERE trigger_event = 11;""")
        else:
            print("申述失败次数设置大于10次，无需修改设置")


        # 查询普通用户广告手续费配置，如未配置上架优惠则不计算上币优惠
        coin_config = DKApiBase().mysqlResultFormat(connect_mysql().connect2mysql("""SELECT general_buy_min_balance, general_discount_coin_scale, 
        general_discount_coin_unit, general_discount_rate, general_fee, general_fee_coin_unit FROM otc_coin WHERE `name` = '{}';""".format(self.advertcoin_CNYT)),
                                                  ["general_buy_min_balance", "general_discount_coin_scale", "general_discount_coin_unit", "general_discount_rate", "general_fee", "general_fee_coin_unit"])
        # 判断设置广告上架费用是否为广告币种，否则将广告上架币种设置为广告币种
        if coin_config["general_fee_coin_unit"] == self.advertcoin_CNYT:
            logger.info("广告上架费用基础币种为：{}，与广告币种{}相同".format(coin_config["general_fee_coin_unit"], self.advertcoin_CNYT))
        else:
            connect_mysql().connect2mysql("""UPDATE otc_coin SET general_fee_coin_unit = '{}' WHERE `name` = '{}';""".format(self.advertcoin_CNYT, self.advertcoin_CNYT))
            logger.error("原广告上架费用基础币种为：{}，修改为广告币种{}".format(coin_config["general_fee_coin_unit"], self.advertcoin_CNYT))
            print("原广告上架费用基础币种为：{}，修改为广告币种{}".format(coin_config["general_fee_coin_unit"], self.advertcoin_CNYT))
        # 判断广告费优惠币种为SLU，否则修改为SLU
        if coin_config["general_discount_coin_unit"] == "SLU":
            logger.info("广告优惠币种：{}".format(coin_config["general_discount_coin_unit"]))
        else:
            connect_mysql().connect2mysql("""UPDATE otc_coin SET general_discount_coin_unit = 'SLU' WHERE `name` = '{}';""".format(self.advertcoin_CNYT))
            logger.error("原上架手续费优惠币种为{}，修改为：SLU".format(coin_config["general_discount_coin_unit"]))
            print("原上架手续费优惠币种为{}，修改为：SLU".format(coin_config["general_discount_coin_unit"]))
        # 判断广告上架SLU优惠比例设为0则为不开启优惠，如未0则开启设置为0.8
        if coin_config["general_discount_rate"] == 0:
            connect_mysql().connect2mysql("""UPDATE otc_coin SET general_discount_rate = 0.8 WHERE `name` = '{}';""".format(self.advertcoin_CNYT))
            logger.info("原上架手续费SLU优惠比例为：{},默认设置为：0.8".format(coin_config["general_discount_rate"]))
        # 判断商家手续费金额，如为0则默认设置为10
        if coin_config["general_fee"] == 0:
            connect_mysql().connect2mysql("""UPDATE otc_coin SET general_fee = 10 WHERE `name` = '{}';""".format(self.advertcoin_CNYT))
            logger.info("原上架手续费金额为：{}，默认设置为：10".format(coin_config["general_fee"]))
        # 完成设置后重新查询广告上架费用配置
        coin_config = DKApiBase().mysqlResultFormat(connect_mysql().connect2mysql("""SELECT general_buy_min_balance, general_discount_coin_scale, 
        general_discount_coin_unit, general_discount_rate, general_fee, general_fee_coin_unit FROM otc_coin WHERE `name` = '{}';""".format(self.advertcoin_CNYT)),
                                                  ["general_buy_min_balance", "general_discount_coin_scale", "general_discount_coin_unit", "general_discount_rate", "general_fee", "general_fee_coin_unit"])

        # 查询普通用户发布广告前账户数据
        wallet_sale_CNYT = DKApiBase().mysqlResultFormat(connect_mysql().connect2mysql("""SELECT balance, frozen_balance, lock_balance FROM member_wallet WHERE member_id = 
        (SELECT id FROM member WHERE token = '{}') AND coin_id = '{}';""".format(COMMON_TOKEN_GENERAL_USER, self.advertcoin_CNYT)), ["balance", "frozen_balance", "lock_balance"])
        wallet_sale_SLU = DKApiBase().mysqlResultFormat(connect_mysql().connect2mysql("""SELECT balance, frozen_balance, lock_balance FROM member_wallet WHERE member_id = 
        (SELECT id FROM member WHERE token = '{}') AND coin_id = '{}';""".format(COMMON_TOKEN_GENERAL_USER, self.walletcion_SLU)), ["balance", "frozen_balance", "lock_balance"])

        # 创建卖出广告，选择使用SLU优惠
        server = "otc/advertise/create"
        data = {
            "price": self.advertPrice_CNYT,
            "advertiseType": "1",  # 0买，1卖
            "coin.id": self.otc_coin_id_CNYT,
            "minLimit": "100",
            "maxLimit": "1000",
            "timeLimit": "30",
            "country": "中国",
            "priceType": "0",
            "premiseRate": "",
            "remark": "非认证商家卖出广告,自动化脚本添加",
            "number": self.otc_number,
            "pay[]": "银联",
            "auto": "1",  # 是否开启自动回复0否1是，默认否
            "autoword": "先付款，后放币",
            "needBindPhone": "0",  # 是否需要交易方已绑定手机号，0：不需要，1：需要
            "needRealname": "0",  # 是否需要交易方已做实名认证，0：不需要，1：需要
            "needTradeTimes": "0",  # 需要交易方至少完成过N笔交易（默认为0）
            "needPutonDiscount": "1",  # 是否使用优惠币种支付，0：不使用，1：使用
            "bindingResult": "",  # 绑定结果,非必传项
            "jyPassword": self.jyPassword
        }
        r_sale = request2DKApi(server, data, self.header_general).send()
        print(r_sale)

        # 查询个人所有广告获得最新创建广告
        server = "otc/advertise/all"
        r_Inquire_sale = request2DKApi(server, self.header_general).send()
        print(r_Inquire_sale)
        advertid_sale = DKApiBase().str2json(r_Inquire_sale[2])["data"][0]["id"]  # 从查询接口获取最新发布的这条广告ID

        # 上架广告
        server = "otc/advertise/on/shelves"
        data = {"id": advertid_sale}
        r_on_sale = request2DKApi(server, data, self.header_general).send()
        print(r_on_sale)

        # 查询广告方发布广告后账户数据
        wallet_sale_addadv_CNYT = DKApiBase().mysqlResultFormat(connect_mysql().connect2mysql("""SELECT balance, frozen_balance, lock_balance FROM member_wallet WHERE member_id = 
        (SELECT id FROM member WHERE token = '{}') AND coin_id = '{}';""".format(COMMON_TOKEN_GENERAL_USER,self.advertcoin_CNYT)), ["balance", "frozen_balance", "lock_balance"])
        wallet_sale_addadv_SLU = DKApiBase().mysqlResultFormat(connect_mysql().connect2mysql("""SELECT balance, frozen_balance, lock_balance FROM member_wallet WHERE member_id = 
        (SELECT id FROM member WHERE token = '{}') AND coin_id = '{}';""".format(COMMON_TOKEN_GENERAL_USER, self.walletcion_SLU)), ["balance", "frozen_balance", "lock_balance"])

        sale_change_balance_CNYT = wallet_sale_CNYT["balance"] - wallet_sale_addadv_CNYT["balance"]
        sale_change_frozen_balance_CNYT = wallet_sale_CNYT["frozen_balance"] - wallet_sale_addadv_CNYT["frozen_balance"]
        sale_change_balance_SLU = wallet_sale_SLU["balance"] - wallet_sale_addadv_SLU["balance"]
        logger.info("广告用户{}可用余额变化金额：{}；广告用户{}冻结变化金额{}；广告用户{}可用余额变化金额{}".format(self.advertcoin_CNYT, sale_change_balance_CNYT,
                                                                               self.advertcoin_CNYT, sale_change_frozen_balance_CNYT, self.walletcion_SLU, sale_change_balance_SLU))

        # 上架手续费计算
        try:
            # 获取CNYT对USDT价格
            price_CNYT_USDT = float(DKApiBase().str2json(request2DKApi("market/exchange-rate/usd/cnyt").send()[2])["data"])
            logger.info("获取CNYT对USDT价格：{}".format(price_CNYT_USDT))
            # 获取SLU对USDT价格
            price_SLU_USDT = float(DKApiBase().str2json(request2DKApi("market/exchange-rate/usd/slu").send()[2])["data"])
            logger.info("获取SLU对USDT价格：{}".format(price_SLU_USDT))
        except Exception as e:
            logger.error("获取CNYT/SLU对USDT价格失败：", e)

        # 手续费全部换算成SLU金额
        fee_2_SLU = float(coin_config["general_fee"]) * price_CNYT_USDT / price_SLU_USDT * 0.8
        if wallet_sale_SLU["balance"] == 0:
            if sale_change_balance_CNYT == self.otc_number + coin_config["general_fee"] and sale_change_frozen_balance_CNYT == self.otc_number:
                logger.info("用户SLU账户为：{}，全额扣除{}账户金额{}".format(wallet_sale_SLU["balance"], self.advertcoin_CNYT, coin_config["general_fee"]))
                print("用户SLU账户为：{}，全额扣除{}账户金额{}".format(wallet_sale_SLU["balance"], self.advertcoin_CNYT, coin_config["general_fee"]))
            else:
                logger.error("SLU账户为0时广告上架手续费扣除数据异常")
                print("SLU账户为0时广告上架手续费扣除数据异常")
        elif wallet_sale_SLU["balance"] >= fee_2_SLU:
            logger.info("广告上架全额扣除SLU优惠手续费：{}".format(fee_2_SLU))
            print("广告上架全额扣除SLU优惠手续费：{}".format(fee_2_SLU))
            if sale_change_balance_SLU == fee_2_SLU:
                logger.info("广告上架费用由SLU全额扣除正确：{}".format(fee_2_SLU))
                print("广告上架费用由SLU全额扣除正确：{}".format(fee_2_SLU))
            else:
                logger.error("SLU账户金额大于应付广告手续费时扣除数据异常")
                print("SLU账户金额大于应付广告手续费时扣除数据异常")
        else:
            logger.info("广告上架实际扣除SLU优惠部分手续费：{}".format(wallet_sale_SLU["balance"] ))
            print("广告上架实际扣除SLU优惠部分手续费：{}".format(wallet_sale_SLU["balance"]))
            # 部分扣除时CNYT应扣除广告费部分
            fee_CNYT = (fee_2_SLU - wallet_sale_SLU["balance"]) / 0.8 * price_SLU_USDT / price_CNYT_USDT
            if sale_change_balance_CNYT == self.otc_number + fee_CNYT and sale_change_frozen_balance_CNYT == self.otc_number:
                logger.info("部分使用SLU支付时，扣除原费用币种{}金额{}正确".format(self.advertcoin_CNYT, fee_CNYT))
                print("部分使用SLU支付时，扣除原费用币种{}金额{}正确".format(self.advertcoin_CNYT, fee_CNYT))
            else:
                logger.error("部分使用SLU支付时扣除广告费用金额异常")
                print("部分使用SLU支付时扣除广告费用金额异常")


    def test_otc_order_cancel_buy(self):
        """买币取消订单"""

        # # 查询账户余额及冻结余额
        # try:
        #     check_mysql = connect_mysql().connect2mysql(self.inquire_member_wallet_CNYT_sql)
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






