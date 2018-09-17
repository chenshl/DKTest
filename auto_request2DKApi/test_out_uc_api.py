# coding:utf-8
# @author : csl
# @date   : 2018/08/21 09:23
# uc查询类接口

import unittest
from common.request2DKApi import request2DKApi
from common.base import DKApiBase
from common.base_connect_mysql import connect_mysql
from common.baseDatas import *

class DKApiautoTest_uc_out(unittest.TestCase):
    """uc查询类接口"""

    @classmethod
    def setUpClass(cls):
        # @classmethod修饰setUpClass(cls):类方法，让setUpClass(cls):只需要执行一次，setUp(self)则会在每一个def test_*(self)开始前执行
        # 如setUpClass(cls):抛出异常则不会执行tearDownclass(cls):

        # 预定义的参数
        cls.symbol = "SLU"  # 币种名称
        cls.symbol_base = "USDT"  # 基币名称

        # 获取活动查询结果
        try:
            cls.activitie_id_sql = """SELECT id, `name`, activitie_id FROM lock_coin_activitie_setting WHERE coin_symbol = 'SLU' AND damages_calc_type = 1 ORDER BY id DESC;"""
            cls.activitie_result = DKApiBase().mysqlResultFormat(connect_mysql().connect2mysql(cls.activitie_id_sql), ["id", "name", "activitie_id"])
        except Exception as e:
            print("数据库查询错误：{}".format(e))

        # 查询用户全部锁仓记录
        try:
            cls.LockCoin_sql = """SELECT id, coin_unit, member_id, type, `status` FROM lock_coin_detail 
            WHERE coin_unit = 'SLU' AND member_id = (SELECT id FROM member WHERE token = '{}') ORDER BY id DESC;""".format(COMMON_TOKEN)
            cls.LockCoin_result = DKApiBase().mysqlResultFormat(connect_mysql().connect2mysql(cls.LockCoin_sql), ["id", "coin_unit", "member_id", "type", "status"])
        except Exception as e:
            print("数据库查询错误：{}".format(e))

    def tearDown(self):

        pass


    def test_uc_activity_lockActivityProject(self):
        """获取所有活动列表"""
        server = "uc/activity/lockActivityProject"
        data = {"activitieType":"3"}  # 0:锁仓活动;1:理财锁仓;2:其他;3:量化投资产品;不传默认查询全部
        r = request2DKApi(server, data).send()
        print(r)
        if "id" not in r[2]:
            print("活动列表为空或' '")
            self.assertIsNotNone(r[2], "活动列表为空")
        else:
            self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_uc_activity_lockActivityProject(self):
        """获取单个活动详情"""
        activityid = str(self.activitie_result[0]["activitie_id"])  # 获取锁仓活动ID
        server = "uc/activity/lockActivityProject/" +activityid
        r = request2DKApi(server).send()
        print(r)
        if activityid not in r[2]:
            print("返回结果错误")
            self.assertTrue(False, "返回结果错误")
        else:
            self.assertRegexpMatches(r[2], activityid, "返回结果错误")

    def test_uc_activity_lockActivitySetting(self):
        """获取活动配置所有详情"""
        activitieId = str(self.activitie_result[0]["activitie_id"])
        server = "uc/activity/lockActivitySetting/" + activitieId
        r = request2DKApi(server).send()
        print(r)
        activitie_result_name = str(self.activitie_result[0]["name"])
        print(activitie_result_name)
        if str(self.activitie_result[0]["id"]) not in r[2]:
            print("返回结果错误")
            self.assertTrue(False, "返回结果错误")
        else:
            self.assertRegexpMatches(r[2], activitie_result_name, "结果断言失败")

    def test_uc_activity_oneLockActivitySetting(self):
        """获取某个活动配置"""
        activitieId = str(self.activitie_result[0]["id"])
        server = "uc/activity/oneLockActivitySetting/" + activitieId
        r = request2DKApi(server).send()
        print(r)
        activitie_result_name = str(self.activitie_result[0]["name"])
        if activitieId not in r[2]:
            print("返回结果错误")
            self.assertTrue(False, "返回结果错误")
        else:
            self.assertRegexpMatches(r[2], activitie_result_name, "结果断言失败")

    def test_uc_activity_lockCoinDial(self):
        """获取用户某个活动的锁仓记录"""
        server = "uc/activity/lockCoinDial"
        data = {
            "pageNo": "1",
            "pageSize": "2",
            "activityId": str(self.activitie_result[0]["activitie_id"]),  # lock_coin_activitie_setting表activitie_id
            "lockType": "4"  # 锁仓类型:0:商家保证金;1:手动锁仓;2:锁仓活动;3:理财锁仓;4:SLB节点产品
        }
        r = request2DKApi(server, data).send()
        print(r)
        if self.symbol not in r[2]:
            print("该用户无 {} 锁仓记录".format(self.symbol))
            self.assertTrue(False, "该用户无 {} 锁仓记录".format(self.symbol))
        else:
            self.assertRegexpMatches(r[2], '"message" : "success"', "结果断言失败")

    def test_uc_activity_allLockCoinDial(self):
        """获取用户的所有锁仓记录"""
        server = "uc/activity/allLockCoinDial"
        data = {
            "pageNo": "1",
            "pageSize": "3",
            "lockType": "2"}
        r = request2DKApi(server, data).send()
        print(r)
        if self.symbol not in r[2]:
            print("该用户无 {} 锁仓记录".format(self.symbol))
            self.assertTrue(False, "该用户无 {} 锁仓记录".format(self.symbol))
        else:
            self.assertRegexpMatches(r[2], '"message" : "success"', "结果断言失败")

    def test_uc_activity_oneLockCoinDial(self):
        """获取用户的单条锁仓记录"""
        server = "uc/activity/oneLockCoinDial"
        data = {"id": self.LockCoin_result[0]["id"]}  # 锁仓详情id
        r = request2DKApi(server, data).send()
        print(r)
        if self.symbol not in r[2]:
            print("该用户无 {} 锁仓记录".format(self.symbol))
            self.assertTrue(False, "该用户无 {} 锁仓记录".format(self.symbol))
        else:
            self.assertRegexpMatches(r[2], '"message" : "success"', "结果断言失败")

    def test_uc_activity_handleLockCoinDial(self):
        """获取手动充值锁仓记录"""
        server = "uc/activity/handleLockCoinDial"
        data = {"pageNo": "1",
                "pageSize": "20"}
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "success"', "结果断言失败")  # 该接口只断言请求发送成功，不判断数据

    def test_uc_activity_handleLockCoinDial(self):
        """获取手动充值解锁记录"""
        server = "uc/activity/handleLockCoinDial"
        data = {"pageNo": "1",
                "pageSize": "20",
                "lockCoinDetailId": self.LockCoin_result[0]["id"]  # 锁仓详情id
                }
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "success"', "结果断言失败")  # 该接口只断言请求发送成功，不判断数据

    def test_uc_activity_quantify_user_cny_get(self):
        """获取SLB节点产品用户累计等级查询"""
        server = "uc/activity/quantify/user-cny/get"
        data = {"memberId": self.LockCoin_result[0]["member_id"],
                "activityId": "35"}  # 这个参数实际没有用处
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_uc_ancillary_website_info(self):
        """站点信息"""
        server = "uc/ancillary/website/info"
        r = request2DKApi(server).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_uc_ancillary_system_advertise(self):
        """系统广告"""
        server = "uc/ancillary/system/advertise"
        data = {"sysAdvertiseLocation": "1"}  # 系统广告位置  0:app首页轮播/1：PC首页轮播/2：pc分类广告
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_uc_ancillary_system_help(self):
        """系统帮助"""
        server = "uc/ancillary/system/help"
        data = {"sysHelpClassification": "0"}  # 系统帮助类别：0：新手入门1：常见问题2：充值指南3：交易指南 4：app下载  非必传（默认查全部）
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_uc_ancillary_system_help_detail(self):
        """系统帮助详情"""
        helpid = "1"
        server = "uc/ancillary/system/help/" + helpid
        r = request2DKApi(server).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_uc_ancillary_system_agreement(self):
        """系统协议获取接口"""
        server = "uc/ancillary/system/agreement"
        data = {"sysHelpClassification": "1"}  # 系统帮助类别：0：新手入门   1：常见问题2：充值指南   3：交易指南 4：app下载  非必传，实测参数无效
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_uc_ancillary_system_agreement_detail(self):
        """系统详情获取接口"""
        agreementid = "24"
        server = "uc/ancillary/system/agreement/" + agreementid
        r = request2DKApi(server).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_uc_ancillary_system_app_version(self):
        """移动版本号"""
        platformid = "1"
        server = "uc/ancillary/system/app/version/" + platformid
        r = request2DKApi(server).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_uc_announcement_page(self):
        """公告分页"""
        server = "uc/announcement/page"
        data = {"pageNo": "1",
                "pageSize": "3"}
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_uc_announcement_detail(self):
        """公告详情"""
        announcementid = "5"
        server = "uc/announcement/" + announcementid
        r = request2DKApi(server).send("GET")
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_uc_asset_wallet(self):
        """用户钱包信息"""
        server = "uc/asset/wallet"
        r = request2DKApi(server).send()
        print(r)
        self.assertRegexpMatches(r[2], self.symbol, "结果断言失败")

    def test_uc_asset_transaction(self):
        """查询特定类型的记录"""
        server = "uc/asset/transaction"
        data = {"pageNo": "1",
                "pageSize": "20",
                "type": "3"# TransactionType交易类型：充值0，提现1，转账2，币币交易3，法币买入4，法币卖出5，人工充值10，币币交易返佣12，币币交易合伙人奖励13，商家认证保证金14，理财锁仓18，SLB节点产品20
                }
        r = request2DKApi(server, data).send()
        print(r)
        if self.symbol_base not in r[2]:
            print("该用户无 {} 交易记录".format(self.symbol_base))
            self.assertTrue(False, "该用户无 {} 交易记录".format(self.symbol_base))
        else:
            self.assertRegexpMatches(r[2], self.symbol_base, "结果断言失败")

    def test_uc_asset_transaction_all(self):
        """查询所有记录"""
        server = "uc/asset/transaction/all"
        data = {"pageNo": "1",
                "pageSize": "20"
                }
        r = request2DKApi(server, data).send()
        print(r)
        if self.symbol_base not in r[2]:
            print("该用户无 {} 交易记录".format(self.symbol_base))
            self.assertTrue(False, "该用户无 {} 交易记录".format(self.symbol_base))
        else:
            self.assertRegexpMatches(r[2], self.symbol_base, "结果断言失败")

    def test_uc_asset_wallet_symbol_unit(self):
        """根据币种查询钱包信息"""
        symbol_unit = self.symbol  # 币种简称
        server = "uc/asset/wallet/" + symbol_unit
        r = request2DKApi(server).send()
        print(r)
        self.assertRegexpMatches(r[2], self.symbol, "结果断言失败")

    def test_uc_coin_supported(self):
        """查询币种"""
        server = "uc/coin/supported"
        r = request2DKApi(server).send()
        print(r)
        self.assertRegexpMatches(r[2], "USDT", "结果断言失败")

    def test_uc_check_login(self):
        """检查是否登录"""
        server = "uc/check/login"
        r = request2DKApi(server).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_uc_loginHistory(self):
        """查看登录历史"""
        server = "uc/loginHistory"
        data = {"pageNo": "1",
                "pageSize": "20"}
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "success"', "结果断言失败")

    def test_uc_partner_businessTotal(self):
        """查看合伙人业务累计收益数据"""
        server = "uc/partner/businessTotal"
        data = {"areaId": "50"}
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_uc_partner_allArea(self):
        """获取区域组织架构信息"""
        server = "uc/partner/allArea"
        data = {"areaId": "50"}
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "success"', "结果断言失败")

    def test_uc_partner_partnerStatus(self):
        """合伙人等级"""
        server = "uc/partner/partnerStatus"
        r = request2DKApi(server).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "success"', "结果断言失败")

    def test_uc_promotion_record(self):
        """推广记录查询"""
        server = "uc/promotion/record"
        r = request2DKApi(server).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "success"', "结果断言失败")

    def test_uc_promotion_reward_record(self):
        """推广奖励记录"""
        server = "uc/promotion/reward/record"
        data = {"pageNo": "1",
                "pageSize": "20"}
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_uc_support_country(self):
        """会员注册支持的国家"""
        server = "uc/support/country"
        r = request2DKApi(server).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_uc_register_check_username(self):
        """检查用户名是否重复"""
        server = "uc/register/check/username"
        data = {"username": "测试"}
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_uc_withdraw_support_coin(self):
        """支持提现的地址"""
        server = "uc/withdraw/support/coin"
        r = request2DKApi(server).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_uc_withdraw_support_coin_info(self):
        """提现币种详细信息"""
        server = "uc/withdraw/support/coin/info"
        r = request2DKApi(server).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_uc_withdraw_support_coin_one(self):
        """单一提现币种详细信息"""
        server = "uc/withdraw/support/coin/one"
        data = {"unit": self.symbol}
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "SUCCESS"', "结果断言失败")

    def test_uc_withdraw_record(self):
        """提币记录"""
        server = "uc/withdraw/record"
        data = {"page": "1",
                "pageSize": "20"}
        r = request2DKApi(server, data).send()
        print(r)
        self.assertRegexpMatches(r[2], '"message" : "success"', "结果断言失败")

if __name__ == "__main__":
    unittest.main()