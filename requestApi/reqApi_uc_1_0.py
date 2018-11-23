# coding:utf-8
# @author : csl
# @date   : 2018/07/27 17:18
"""用户中心通用接口"""

from common.request2DKApi import request2DKApi
from common.base import DKApiBase
from common.base_creatTestCase import creatTestCase
from common.base_connect_mysql import connect_mysql

class reqApi_uc_1_0(object):
        """用户中心通用接口封装成单个方法调用，免去注释/打开"""

        def uc_activity_lockActivityProject(self):
                """
                1.锁仓活动
                1.1 获取所有活动列表
                :return: 
                """
                server = "uc/activity/lockActivityProject"
                data = {"activitieType": "3"}  # 0:锁仓活动;1:理财锁仓;2:其他;3:量化投资产品;不传默认查询全部
                r = request2DKApi(server, data).send()
                print(r)

        def uc_activity_lockActivityProject_activityid(self):
                """
                1.2 获取单个活动详情
                :return: 
                """
                activityid = "35"
                server = "uc/activity/lockActivityProject/" + activityid
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_activity_lockActivitySetting_activitieId(self):
                """
                1.3 获取活动配置所有详情
                :return: 
                """
                activitieId = "35"
                server = "uc/activity/lockActivitySetting/" + activitieId
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_activity_oneLockActivitySetting_activitieId(self):
                """
                1.4获取某个活动配置
                :return: 
                """
                activitieId = "49"
                server = "uc/activity/oneLockActivitySetting/" + activitieId
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_activity_joinActivity(self):
                """
                1.5、参加锁仓活动
                :return: 
                """
                jyPassword = "111111"
                server = "uc/activity/joinActivity"
                data = {"id":"46",  # 锁仓活动配置表主键
                        "boughtAmount":"10",
                        "jyPassword":DKApiBase().getSign(jyPassword + "hello, moto")
                        }
                r = request2DKApi(server, data).send()
                print(r)

        def uc_activity_unLockActivity(self):
                """
                1.6、用户手动申请解锁锁仓活动
                :return: 
                """
                jyPassword = "111111"
                server = "uc/activity/unLockActivity"
                data = {"id":"508",  # 锁仓详情主键
                        "jyPassword":DKApiBase().getSign(jyPassword + "hello, moto")
                        }
                r = request2DKApi(server, data).send()
                print(r)

        def uc_activity_joinFinancialLock(self):
                """
                1.7 参加理财锁仓活动
                :return: 
                """
                jyPassword = "111111"
                server = "uc/activity/joinFinancialLock"
                data = {"id":"46",
                        "usdtNum":"100",
                        "jyPassword":DKApiBase().getSign(jyPassword + "hello, moto")}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_activity_unLockFinancialLock(self):
                """
                1.8 用户手动申请解锁理财锁仓活动
                :return: 
                """
                jyPassword = "111111"
                server = "uc/activity/unLockFinancialLock"
                data = {"id":"509",  # 锁仓详情主键
                        "settlementType":"1",  # 理财结算类型:0:活动币种结算;1：USDT结算
                        "jyPassword":DKApiBase().getSign(jyPassword + "hello, moto")
                        }
                r = request2DKApi(server, data).send()
                print(r)

        def uc_activity_lockCoinDial(self):
                """
                1.9 获取用户某个活动的锁仓记录
                :return: 
                """
                server = "uc/activity/lockCoinDial"
                data = {
                        "pageNo":"1",
                        "pageSize":"2",
                        "activityId":"35",  # lock_coin_activitie_setting表activitie_id
                        "lockType":"2"  # 锁仓类型:0:商家保证金;1:手动锁仓;2:锁仓活动;3:理财锁仓;4:SLB节点产品
                        }
                r = request2DKApi(server, data).send()
                print(r)

        def uc_activity_allLockCoinDial(self):
                """
                1.10 获取用户的所有锁仓记录
                :return: 
                """
                server = "uc/activity/allLockCoinDial"
                data = {
                        "pageNo":"1",
                        "pageSize":"3",
                        "lockType":"2"}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_activity_oneLockCoinDial(self):
                """
                1.11 获取用户的单条锁仓记录
                :return: 
                """
                server = "uc/activity/oneLockCoinDial"
                data = {"id":"510"}  # 锁仓详情id
                r = request2DKApi(server, data).send()
                print(r)

        def uc_activity_handleLockCoinDial(self):
                """
                1.12 获取手动充值锁仓记录
                :return: 
                """
                server = "uc/activity/handleLockCoinDial"
                data = {"pageNo":"1",
                        "pageSize":"20"}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_activity_handleLockCoinDial(self):
                """
                1.13 获取手动充值解锁记录
                :return: 
                """
                server = "uc/activity/handleLockCoinDial"
                data = {"pageNo":"1",
                        "pageSize":"20",
                        "lockCoinDetailId":"570"  # 锁仓详情id
                        }
                r = request2DKApi(server, data).send()
                print(r)

        def uc_activity_joinQuantifyLock(self):
                """
                1.14 参加SLB节点产品
                :return: 
                """
                jyPassword = "111111"
                server = "uc/activity/joinQuantifyLock"
                data = {"id":"46",  # 活动ID
                        "cnyAmount":"10000",
                        "jyPassword":DKApiBase().getSign(jyPassword + "hello, moto")}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_activity_quantify_user_cny_get(self):
                """
                1.15 获取SLB节点产品用户累计等级查询
                :return: 
                """
                server = "uc/activity/quantify/user-cny/get"
                data = {"memberId":"74773",
                        "activityId":"35"}  # 这个参数实际没有用处
                r = request2DKApi(server, data).send()
                print(r)

        def uc_ancillary_website_info(self):
                """
                2 站点帮助广告等
                2.1 站点信息
                :return: 
                """
                server = "uc/ancillary/website/info"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_ancillary_system_advertise(self):
                """
                2.2 系统广告
                :return: 
                """
                server = "uc/ancillary/system/advertise"
                data = {"sysAdvertiseLocation":"1"}  # 系统广告位置  0:app首页轮播/1：PC首页轮播/2：pc分类广告
                r = request2DKApi(server, data).send()
                print(r)

        def uc_ancillary_system_help(self):
                """
                2.3 系统帮助
                :return: 
                """
                server = "uc/ancillary/system/help"
                data = {"sysHelpClassification":"0"}  # 系统帮助类别：0：新手入门1：常见问题2：充值指南3：交易指南 4：app下载  非必传（默认查全部）
                r = request2DKApi(server, data).send()
                print(r)

        def uc_ancillary_system_help_helpid(self):
                """
                2.4 系统帮助详情
                :return: 
                """
                helpid = "1"
                server = "uc/ancillary/system/help/" + helpid
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_ancillary_system_agreement(self):
                """
                2.5 系统协议获取接口
                :return: 
                """
                server = "uc/ancillary/system/agreement"
                data = {"sysHelpClassification":"1"}  # 系统帮助类别：0：新手入门   1：常见问题2：充值指南   3：交易指南 4：app下载  非必传，实测参数无效
                r = request2DKApi(server, data).send()
                print(r)

        def uc_ancillary_system_agreement_agreementid(self):
                """
                2.6 系统详情获取接口
                :return: 
                """
                agreementid = "24"
                server = "uc/ancillary/system/agreement/" +agreementid
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_ancillary_system_app_version_platformid(self):
                """
                2.7 移动版本号
                :return: 
                """
                platformid = "1"
                server = "uc/ancillary/system/app/version/" + platformid
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_announcement_page(self):
                """
                3 公告
                3.1 公告分页
                :return: 
                """
                server = "uc/announcement/page"
                data = {"pageNo":"1",
                        "pageSize":"3"
                        }
                r = request2DKApi(server, data).send()
                print(r)

        def uc_announcement_announcementid(self):
                """
                3.2 公告详情
                :return: 
                """
                announcementid = "5"
                server = "uc/announcement/" + announcementid
                r = request2DKApi(server).send("GET")
                print(r)

        def uc_approve_change_avatar(self):
                """
                4 用户中心认证
                4.1 设置或更改用户头像（好像无此功能）
                :return: 
                """
                server = "uc/approve/change/avatar"
                data = {"url":"http://www.baidu.com"}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_change_username(self):
                """
                4.2 修改用户名（好像只允许修改一次）
                :return: 
                """
                header={"access-auth-token":"7d614fe74466a03ca3c8e7522321b2b3"}
                server = "uc/approve/change/username"
                data = {"newUserName":"三"}
                r = request2DKApi(server, data,header).send()
                print(r)

        def uc_approve_security_open(self):
                """
                4.3 开启安全设置
                :return: 
                """
                server = "uc/approve/security/open"
                data = {"isOpenPhoneLogin":"0",  # 是否开启手机登录认证0 :否；1：是
                        "isOpenGoogleLogin":"0",
                        "isOpenPhoneUpCoin":"0",
                        "isOpenGoogleUpCoin":"0"}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_security_setting(self):
                """
                4.4 安全设置
                :return: 
                """
                server = "uc/approve/security/setting"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_business_material(self):
                """
                4.5 商家认证材料检查
                :return: 
                """
                server = "uc/approve/business/material"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_transaction_password(self):
                """
                4.6 设置资金密码（已设置则会返回code：500，不可重复设置）
                :return: 
                """
                server = "uc/approve/transaction/password"
                data = {"jyPassword":"111111",
                        "code":"429389",
                        "codeType":"0"  # 0手机，1邮箱
                        }
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_transaction_password_batch(self):
                """
                4.6.1 批量设置资金密码
                :return: 
                """
                server = "uc/approve/transaction/password"
                data = {"jyPassword":"111111"}
                sql_result = connect_mysql().connect2mysql("SELECT token FROM member WHERE token LIKE '1111%';")
                result = DKApiBase().mysqlResultFormat(sql_result, ["token"])
                print(result)
                for token in result:
                        print({"access-auth-token":token["token"]})
                        r = request2DKApi(server, data, {"access-auth-token":token["token"]}).send()
                        print(r)
                print("设置完毕")

        def uc_approve_update_transaction_password(self):
                """
                4.7 修改资金密码（修改第一次成功，修改后的继续修改报资金密码错误）（建议手动回归验证）
                :return: 
                """
                oldPassword = "111111"
                server = "uc/approve/update/transaction/password"
                data = {"oldPassword":DKApiBase().getSign(oldPassword + "hello, moto"),
                        "newPassword":"222222"}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_reset_transaction_password(self):
                """
                4.8 重置资金密码（建议手动回归验证）
                :return: 
                """
                server = "uc/approve/reset/transaction/password"
                data = {"newPassword":"",
                        "code":""  # 短信验证码，要在内存中去找，如参加自动化则要自动去查找验证码
                        }
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_bind_phone(self):
                """
                4.9 绑定手机号（建议手动回归验证）
                :return: 
                """
                server = "uc/approve/bind/phone"
                data = {"countryName":"",  # 城市名
                        "password":"",  # 登录密码
                        "phone":"",  # 手机号
                        "code":""  # 手机验证码
                        }
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_update_password(self):
                """
                4.10 更改登录密码（建议手动回归验证）
                :return: 
                """
                server = "uc/approve/update/password"
                data = {"newPassword":"",  # 登录密码
                        "code":""  # 短信验证码
                        }
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_bind_email(self):
                """
                4.11 绑定邮箱（建议手动回归验证）
                :return: 
                """
                server = "uc/approve/bind/email"
                data = {"password":"",  # 登录密码
                        "email":"",  # 邮箱
                        "code":""  # 邮箱验证码
                        }
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_real_name(self):
                """
                4.12 实名认证（建议手动回归验证）
                :return: 
                """
                server = "uc/approve/real/name"
                data = {"realName":"",  # 姓名
                        "idCard":"",  # 身份证号
                        "idCardFront":"",  # 身份证正面照片
                        "idCardBack":"",  # 身份证反面
                        "handHeldIdCard":""  # 手持身份证照片
                        }
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_real_detail(self):
                """
                4.13 查询实名认证情况
                :return: 
                """
                server = "uc/approve/real/detail"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_account_setting(self):
                """
                4.14 账户设置（需要先实名认证，和设置资金密码）
                :return: 
                """
                server = "uc/approve/account/setting"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_bind_bank(self):
                """
                4.15 设置银行卡（已设置返回code：500，提示请勿重复设置）
                :return: 
                """
                jyPassword = "111111"
                server = "uc/approve/bind/bank"
                data = {"bank":"中国工商银行",
                        "branch":"沙坪坝支行",
                        "jyPassword":DKApiBase().getSign(jyPassword + "hello, moto"),
                        "realName":"测试",
                        "cardNo":"6222023100025344073"}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_update_bank(self):
                """
                4.16 更改银行卡
                :return: 
                """
                jyPassword = "111111"
                server = "uc/approve/update/bank"
                data = {"bank":"中国工商银行",
                        "branch":"沙坪坝支行",
                        "jyPassword":DKApiBase().getSign(jyPassword + "hello, moto"),
                        "realName":"测试",
                        "cardNo":"6222023100025344073"}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_bind_ali(self):
                """
                4.17 绑定阿里(手动调用，绑定过的账户不能重复绑定)
                :return: 
                """
                server = "uc/approve/bind/ali"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_update_ali(self):
                """
                4.18 修改支付宝（待调试）
                :return: 
                """
                jyPassword = "111111"
                server = "uc/approve/update/ali"
                data = {"ali":"17712345678",
                        "jyPassword":DKApiBase().getSign(jyPassword + "hello, moto"),
                        "realName":"测试",
                        "qrCodeUrl":"http://silktraderpriv.oss-cn-hongkong.aliyuncs.com/2018/08/14/b91b0da1-567a-441a-926f-83fe7f3c129f.jpg?Expires=1534237113&OSSAccessKeyId=LTAIWYxtSxH9BJ7T&Signature=2UEP5GyDbJNaSUQVmk80ryAtQEY%3D"
                        }
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_bind_wechat(self):
                """
                4.19 绑定微信（手动调用，绑定过的账户不能重复绑定）
                :return: 
                """
                server = "uc/approve/bind/wechat"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_update_wechat(self):
                """
                4.20修改微信（待调试）
                :return: 
                """
                jyPassword = "111111"
                server = "uc/approve/update/wechat"
                data = {"wechat":"188888888889",
                        "jyPassword":DKApiBase().getSign(jyPassword + "hello, moto"),
                        "realName":"测试",
                        "qrCodeUrl":"http://silktraderpriv.oss-cn-hongkong.aliyuncs.com/2018/08/14/4c12dafb-96c7-4d64-a809-b2f5656ec85e.jpg?Expires=1534238183&OSSAccessKeyId=LTAIWYxtSxH9BJ7T&Signature=wR9M27m9vS5aCBuhrLfDuRrV%2BUY%3D"
                        }
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_certified_business_status(self):
                """
                4.21 认证商家申请状态
                :return: 
                """
                server = "uc/approve/certified/business/status"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_business_auth_deposit_list(self):
                """
                4.22 认证商家申请，已发送邮件
                :return: 
                """
                server = "uc/approve/business-auth-deposit/list"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_certified_business_apply(self):
                """
                4.23 认证商家申请（待调试）
                :return: 
                """
                jyPassword = "111111"
                server = "uc/approve/certified/business/apply"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_cancel_business(self):
                """
                4.24 申请取消认证商家（待调试）
                :return: 
                """
                jyPassword = "111111"
                server = "uc/approve/cancel/business"
                data = {"reason":"申请退保原因",
                        "jyPassword":DKApiBase().getSign(jyPassword + "hello, moto")}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_change_phone(self):
                """
                4.25 更换手机（待调试）
                :return: 
                """
                server = "uc/approve/change/phone"
                data = {"password":"",
                        "phone":"",
                        "code":""}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_change_email(self):
                """
                4.26 更换邮箱（待调试）
                :return: 
                """
                server = "uc/approve/change/email"
                data = {"jyPassword":"",
                        "email":"",
                        "code":""}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_change_email_code(self):
                """
                4.27 更换邮箱发送验证码
                :return: 
                """
                server = "uc/approve/change/email/code"
                data = {"email":"35643856@qq.com"}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_approve_lock_coin_detail_customer(self):
                """
                4.28 查询商家锁仓记录
                :return: 
                """
                server = "uc/approve/lock-coin-detail/customer"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_asset_wallet(self):
                """
                5 用户资产
                5.1 用户钱包信息
                :return: 
                """
                server = "uc/asset/wallet"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_asset_wallet_getCoinAddr(self):
                """
                5.2 获取用户新币的地址
                :return: 
                """
                server = "uc/asset/wallet/getCoinAddr"
                data = {"coinName":"Silubium"}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_asset_transaction(self):
                """
                5.3 查询特定类型的记录
                :return: 
                """
                server = "uc/asset/transaction"
                data = {"pageNo":"1",
                        "pageSize":"20",
                        "type":"3"  # TransactionType交易类型：充值0，提现1，转账2，币币交易3，法币买入4，法币卖出5，人工充值10，币币交易返佣12，币币交易合伙人奖励13，商家认证保证金14，理财锁仓18，SLB节点产品20
                        }
                r = request2DKApi(server, data).send()
                print(r)

        def uc_asset_transaction_all(self):
                """
                5.4 查询所有记录
                :return: 
                """
                server = "uc/asset/transaction/all"
                data = {"pageNo":"1",
                        "pageSize":"20"
                        }
                r = request2DKApi(server, data).send()
                print(r)

        def uc_asset_wallet_symbol_unit(self):
                """
                5.5 根据币种查询钱包信息
                :return: 
                """
                symbol_unit = "SLB"  # 币种简称
                server = "uc/asset/wallet/" + symbol_unit
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_asset_wallet_match_check(self):
                """
                5.6 币种转化检查（业务参数： GCC配对GCX，特殊用途，其他项目可以不管）
                :return: 
                """
                server = "uc/asset/wallet/match-check"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_asset_wallet_match(self):
                """
                5.7 币种转化检查（待调试，功能及参数待确认）
                :return: 
                """
                server = "uc/asset/wallet/match"
                data = {"amount":"10"}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_asset_wallet_reset_address(self):
                """
                5.8 重置钱包地址（待调试）
                :return: 
                """
                server = "uc/asset/wallet/reset-address"
                data = {"unit":"SLB"}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_coin_legal(self):
                """
                6 coin
                6.1 重置钱包地址（待调试）
                :return: 
                """
                server = "uc/coin/legal"
                r = request2DKApi(server).send("GET")
                print(r)

        def uc_coin_legal_page(self):
                """
                6.2 分页查询所有合法币（待调试）
                :return: 
                """
                server = "uc/coin/legal/page?pageNo=1&pageSize=10"
                data = {}
                r = request2DKApi(server, data).send("GET")
                print(r)

        # 6.3 查询币种
        def uc_coin_supported(self):
                """
                6.3 查询币种
                :return: 
                """
                server = "uc/coin/supported"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_feedback(self):
                """
                7 反馈
                7.1 提交反馈意见
                :return: 
                """
                server = "uc/feedback"
                data = {"remark":"测试提交反馈意见！"}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_start_captcha(self):
                """
                8 初始化极验证
                8.1 初始化极验证（待调试）
                :return: 
                """
                server = "uc/start/captcha"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_google_yzgoogle(self):
                """
                9 Google验证
                9.1 验证Google（待调试）
                :return: 
                """
                server = "uc/google/yzgoogle"
                data = {"codes":""}  # 验证码
                r = request2DKApi(server, data).send()
                print(r)

        def uc_google_sendgoogle(self):
                """
                9.2 生成谷歌认证码（待调试）
                :return: 
                """
                server = "uc/google/sendgoogle"
                r = request2DKApi(server).send("GET")
                print(r)

        def uc_google_jcgoogle(self):
                """
                9.3 谷歌解绑（待调试）
                :return: 
                """
                server = "uc/google/jcgoogle"
                data = {"password":"",  # 密码
                        "codes":""  # 验证
                        }
                r = request2DKApi(server, data).send()
                print(r)

        def uc_google_googleAuth(self):
                """
                9.4 绑定谷歌（待调试）
                :return: 
                """
                server = "uc/google/googleAuth"
                data = {"secret":"",  # 密钥
                        "codes":""  # 验证码
                        }
                r = request2DKApi(server, data).send()
                print(r)

        def uc_healthy(self):
                """
                10 healthy
                10.1 负载均衡健康检查接口（待调试）
                :return: 
                """
                server = "uc/healthy"
                data = {"sleepTime":"3"}  # 睡眠时间
                r = request2DKApi(server, data).send()
                print(r)

        def uc_legal_wallet_recharge(self):
                """
                11 会员充值
                11.1 会员充值（待调试）
                :return: 
                """
                server = "uc/legal-wallet-recharge"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_legal_wallet_recharge(self):
                """
                11.2 带条件分页（待调试）
                :return: 
                """
                server = "uc/legal-wallet-recharge"
                data = {"state":"0",
                        "screen":"Silubium"}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_legal_wallet_recharge(self):
                """
                11.3 详情（待调试）
                :return: 
                """
                server = "uc/legal-wallet-recharge/74773"
                r = request2DKApi(server).send("GET")
                print(r)

        def uc_legal_wallet_withdraw(self):
                """
                12 提现
                12.1 分页（待调试）
                :return: 
                """
                server = "uc/legal-wallet-withdraw"
                data = {"pageNo":"1",
                        "pageSize":"10",
                        "state":"0"}
                r = request2DKApi(server, data).send()
                print(r)

        # 12.2 提现（待调试）

        # 12.3 详情（待调试）

        def uc_location_get(self):
                """
                13 归属地信息
                13.1 获得归属地信息（待调试）
                :return: 
                """
                server = "uc/location/get"
                r = request2DKApi(server).send("GET")
                print(r)

        def uc_login(self):
                """
                14 登录
                14.1 登录
                :return: 
                """
                server = "uc/login"
                data = {"username":"17700000041",
                        "password":DKApiBase().getSign("cs111111" + "hello, moto"),
                        "type":0}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_logout(self):
                """
                14.2 登出（待调试）
                :return: 
                """
                server = "uc/logout"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_check_login(self):
                """
                14.3 检查是否登录
                :return: 
                """
                server = "uc/check/login"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_loginHistory(self):
                """
                14.4 查看登录历史
                :return: 
                """
                server = "uc/loginHistory"
                data = {"pageNo":"1",
                        "pageSize":"20"}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_partner_appUserInfo(self):
                """
                15 合伙人信息
                15.1 通过APP查看合伙人信息（待调试）
                :return: 
                """
                server = "uc/partner/appUserInfo"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_partner_userInfo(self):
                """
                15.2 查看合伙人信息
                :return: 
                """
                server = "uc/partner/userInfo"
                data = {"id":"74773"}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_partner_businessTotal(self):
                """
                15.3 查看合伙人业务累计收益数据
                :return: 
                """
                server = "uc/partner/businessTotal"
                data = {"areaId":"50"}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_partner_businessMonthTotal(self):
                """
                15.4 查看合伙人业务月统计数据（待调试）
                :return: 
                """
                server = "uc/partner/businessMonthTotal"
                data = {"areaId":"50",
                        "collectTime":"2018-08-17"}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_partner_businessDetail(self):
                """
                15.5 查看合伙人业务月收益详细数据（待调试）
                :return: 
                """
                server = "uc/partner/businessDetail"
                data = {"pageNo":"1",
                        "pageSize":"20",
                        "memberId":"",
                        "startTime":"",
                        "endTime":""}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_partner_allArea(self):
                """
                15.6 获取区域组织架构信息
                :return: 
                """
                server = "uc/partner/allArea"
                data = {"areaId":"50"}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_partner_partnerStatus(self):
                """
                15.7 合伙人等级
                :return: 
                """
                server = "uc/partner/partnerStatus"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_partner_page_query(self):
                """
                15.8 分页查询用户合伙人（待调试）
                :return: 
                """
                server = "uc/partner/page-query"
                data = {"pageNo":"",
                        "pageSize":"",
                        "areaId":"50",
                        "level":"M1"}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_promotion_record(self):
                """
                16 推广
                16.1 推广记录查询
                :return: 
                """
                server = "uc/promotion/record"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        # 16.2 推广奖励记录
        def uc_promotion_reward_record(self):
                """
                16.2 推广奖励记录
                :return: 
                """
                server = "uc/promotion/reward/record"
                data = {"pageNo":"1",
                        "pageSize":"20"}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_support_country(self):
                """
                17 会员注册
                17.1 注册支持的国家
                :return: 
                """
                server = "uc/support/country"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_register_check_username(self):
                """
                17.2 检查用户名是否重复
                :return: 
                """
                server = "uc/register/check/username"
                data = {"username":"测试"}
                r = request2DKApi(server, data).send()
                print(r)

        # 17.3 激活邮箱（uc/register/active）
        # 17.4 邮箱注册（uc/register/email）
        # 17.5 邮箱验证码的方式注册（uc/register/email4Code）

        def uc_register_email_code(self):
                """
                17.6 发送邮件注册验证码（uc/register/email/code）
                :return: 
                """
                server = "uc/register/email/code"
                data = {"email":"chen___007@163.com"
                        }
                r = request2DKApi(server, data).send()
                print(r)



        # 17.7 手机注册（uc/register/phone）
        def uc_register_phone():
                """17.7 用户手机号注册"""
                server = "uc/register/phone"



        # 17.8 发送绑定邮箱验证码（uc/bind/email/code）
        # 17.9 增加提币地址验证码（uc/add/address/code）
        # 17.10 忘记密码邮箱验证码（uc/reset/email/code）
        # 17.11 忘记密码后重置密码（uc/reset/login/password）

        # 18.1 获取短信验证码（uc/mobile/code）
        # 18.2 重置交易密码验证码（uc/mobile/transaction/code）
        # 18.3 绑定手机号验证码（uc/mobile/bind/code）
        # 18.4 更改登录密码验证码（uc/mobile/update/password/code）
        # 18.5 添加提币地址手机验证码（uc/mobile/add/address/code）
        # 18.6 忘记密码验证码（uc/mobile/reset/code）
        # 18.7 更改手机验证码（uc/mobile/change/code）
        # 18.8 登录、提币手机验证码（uc/mobile/validation/code）
        # 18.9 更换手机号码时发送验证码（uc/mobile/change/phone/code）
        # 18.10 手机登录验证码核查（uc/mobile/codeCheck）

        def uc_transfer_address(self):
                """
                19 转账
                19.1 根据币种查询转账地址等信息
                :return: 
                """
                server = "uc/transfer/address"
                data = {"unit":"SLB"}
                r = request2DKApi(server, data).send()
                print(r)

        # 19.2 转账申请（uc/transfer/apply）

        def uc_transfer_record(self):
                """
                19.3 转账记录
                :return: 
                """
                server = "uc/transfer/record"
                data = {"pageNo":"1",
                        "pageSize":"20"}
                r = request2DKApi(server, data).send()
                print(r)

        # 20.1 上传图片到阿里云OSS（uc/upload/oss/image）
        # 20.2 上传本地图片（uc/upload/local/image）
        # 20.3 上传base64处理后的图片（uc/upload/oss/base64）

        # """21 提现"""
        # 21.1 增加提现地址（uc/withdraw/address/add）
        # 21.2 删除提现地址（uc/withdraw/address/delete）
        # 21.3 提现地址分页信息（uc/withdraw/address/page）

        # 21.4 支持提现的地址
        def uc_withdraw_support_coin(self):
                """
                21.4 支持提现的地址
                :return: 
                """
                server = "uc/withdraw/support/coin"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_withdraw_support_coin_info(self):
                """
                21.5 提现币种详细信息
                :return: 
                """
                server = "uc/withdraw/support/coin/info"
                data = {}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_withdraw_support_coin_one(self):
                """
                21.6 单一提现币种详细信息
                :return: 
                """
                server = "uc/withdraw/support/coin/one"
                data = {"unit":"SLU"}
                r = request2DKApi(server, data).send()
                print(r)

        def uc_withdraw_apply(self):
                """
                21.7 申请提币
                :return: 
                """
                server = "uc/withdraw/apply"
                data = {"unit":"SLB",
                        "address":"",  # 提币地址
                        "amount":"",  # 总数量
                        "fee":"",  # 手续费
                        "remark":"",  # 备注
                        "jyPassword":""
                        }
                r = request2DKApi(server, data).send()
                print(r)

        def uc_withdraw_record(self):
                """
                21.8 提币记录
                :return: 
                """
                server = "uc/withdraw/record"
                data = {"page":"1",
                        "pageSize":"20"}
                r = request2DKApi(server, data).send()
                print(r)


        def uc_activity_autoUnLockFinancialLock(self):
                """
                SLB理财解锁接口
                :return: 
                """
                jyPassword = "111111"
                server = "uc/activity/autoUnLockFinancialLock"
                data = {"id":"",
                        "jyPassword":DKApiBase().getSign(jyPassword + "hello, moto"),
                        "settlementType":""  # 0为SLB解锁，1为USDT
                        }
                r = request2DKApi(server, data).send()
                print(r)


        # 自动脚本生成请求参数
        # parmas = creatTestCase(data).creat_beseTestCase()
        # for senddata in parmas:
        #     r = request2DKApi(server, senddata).send()
        #     print(r)

        # r = request2DKApi(server, data).send()
        # print(r)

if __name__ == "__main__":
        reqApi_uc_1_0().uc_login()
        # reqApi_uc_1_0().uc_check_login()