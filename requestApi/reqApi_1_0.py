# coding:utf-8
# @author : csl
# @date   : 2018/07/24 13:50
"""用于手动接口探测币币交易"""

from common.request2DKApi import request2DKApi
from common.base import DKApiBase

class reqApi_1_0(object):

        def uc_login(self):
                """
                1、登录接口
                :return: 
                """
                serverc = "uc/login"
                platformPassword = "csl53241csl"
                data = {"username":"17723159468",
                        "password":DKApiBase().getSign(platformPassword + "hello, moto")}
                r = request2DKApi(serverc, data).send()
                print(r)

        def exchange_order_add(self):
                """
                2、订单委托接口
                :return: 
                """
                serverc = "exchange/order/add"
                data = {
                        "symbol":"SLB/USDT",
                        "price":"0.00016115",
                        "amount":"1",
                        "direction":"0",  # 买卖方向，0=BUY（买）/1=SELL（卖）
                        "type":"1"  # 交易类型，1=LIMIT_PRICE(限价交易)
                        }
                r = request2DKApi(serverc, data).send()
                print(r)

        def exchange_order_add_batch(self):
                """
                2.1、批量订单委托接口，创建订单深度
                @description: 查看交易盘口地址：http://www.400.pro/#/exchangemore/slu_cnyt
                :return: 
                """
                for i in range (50386, 50537):
                        serverc = "exchange/order/add"
                        data = {
                                "symbol": "SLU/CNYT",
                                "price": i / 100000,
                                "amount": "1",
                                "direction": "0",  # 买卖方向，0=BUY（买）/1=SELL（卖）
                                "type": "1"  # 交易类型，1=LIMIT_PRICE(限价交易)
                        }
                        r = request2DKApi(serverc, data).send()
                        print(r)


        def exchange_order_current(self):
                """
                3、查询当前委托订单接口
                :return: 
                """
                serverc = "exchange/order/current"
                data = {"symbol":"SLB/USDT",
                        "pageNo":"0",  # 请求开始页码，从0开始
                        "pageSize":"100"  # 请求数量
                        }
                r = request2DKApi(serverc, data).send()
                print(r)

        def exchange_order_history(self):
                """
                4、查询历史委托订单接口
                :return: 
                """
                serverc = "exchange/order/history"
                data = {"symbol":"SLU/USDT",
                        "pageNo":"0",
                        "pageSize":"10"
                        }
                r = request2DKApi(serverc, data).send()
                print(r)

        def exchange_order_cancel_orderNo(self):
                """
                5、撤销委托订单接口,撤销订单添加到请求地址后面,无请求参数
                :return: 
                """
                orderNo = "E216192287807311872"
                serverc = "exchange/order/cancel/" + orderNo
                data = {}
                r = request2DKApi(serverc, data).send()
                print(r)

        def market_symbol_info(self):
                """
                6、获取指定交易对的配置信息接口
                :return: 
                """
                serverc = "market/symbol-info"
                data = {"symbol":"SLB/USDT"}
                r = request2DKApi(serverc, data).send()
                print(r)

        def market_symbol(self):
                """
                7、获取所有交易对信息接口
                :return: 
                """
                serverc = "market/symbol"
                data = {}
                r = request2DKApi(serverc, data).send()
                print(r)

        def market_symbol_thumb(self):
                """
                8、获取所有交易对的当前行情信息接口
                :return: 
                """
                serverc = "market/symbol-thumb"
                data = {}
                r = request2DKApi(serverc, data).send()
                print(r)

        def market_history(self):
                """
                9、获取K线数据接口
                :return: 
                """
                fromdate = "2018-07-26 00:00:00"
                # todate = "2018-07-24 00:00:00"
                serverc = "market/history"
                data = {"symbol":"SLB/USDT",
                        "from":DKApiBase().time2Timestamps(fromdate),  # 开始时间戳
                        "to":DKApiBase().nowtime2Timestamps(),  # 截至时间戳
                        "resolution":"1"  # K线类型：1=1分/5=5分/15=15分/30=30分/1h=小时/1d=天/1m=月
                        }
                r = request2DKApi(serverc, data).send()
                print(r)

        def market_exchange_plate(self):
                """
                10、获取买卖盘口信息接口
                :return: 
                """
                serverc = "market/exchange-plate"
                data = {"symbol":"SLB/USDT"}
                r = request2DKApi(serverc, data).send()
                print(r)

        def market_latest_trade(self):
                """
                11、获取最新实时成交记录接口
                :return: 
                """
                serverc = "market/latest-trade"
                data = {"symbol":"SLB/USDT",
                        "size":"50"  # 记录数量
                        }
                r = request2DKApi(serverc, data).send()
                print(r)

        def uc_asset_wallet_coinName(self):
                """
                12、资产查询接口，币种名称加在请求路径后面
                :return: 
                """
                coinName = "SLB"
                serverc = "uc/asset/wallet/" + coinName
                data = {}
                r = request2DKApi(serverc, data).send()
                print(r)

        def uc_ancillary_system_help(self):
                """
                13、币种资料列表查询接口
                :return: 
                """
                serverc = "uc/ancillary/system/help"
                data = {"sysHelpClassification":"COIN_INFO"}
                r = request2DKApi(serverc, data).send()
                print(r)

        def uc_ancillary_system_help_coinId(self):
                """
                14、获取指定币种资料
                :return: 
                """
                coinId = "6"
                serverc = "uc/ancillary/system/help/" + coinId
                data = {}
                r = request2DKApi(serverc, data).send()
                print(r)

        def uc_announcement_page(self):
                """
                15、公告列表查询接口
                :return: 
                """
                serverc = "uc/announcement/page"
                data = {"pageNo":"1",
                        "pageSize":"10"
                        }
                r = request2DKApi(serverc, data).send()
                print(r)

        def uc_announcement_announcementID(self):
                """
                16、获取公告内容
                :return: 
                """
                requestMark = "GET"
                announcementID = "8"
                serverc = "uc/announcement/" + announcementID
                data = {}
                r = request2DKApi(serverc, data).send()
                print(r)

        def exchange_order_orderInfo(self):
                """
                17、订单明细查询接口
                :return: 
                """
                serverc = "exchange/order/orderInfo"
                data = {"orderId":"E211127401079312384"
                        }
                r = request2DKApi(serverc, data).send()
                print(r)

        def uc_asset_wallet(self):
                """
                18、用户钱包信息
                :return: 
                """
                serverc = "uc/asset/wallet"
                data = {}
                r = request2DKApi(serverc, data).send()
                print(r)


        def guess_api_guessActivity_receiveAward(self):
                """
                19、疯狂的比特游戏领取奖励
                :return: 
                """
                serverc = "guess-api/guessActivity/receiveAward"
                data = {"periodId":"4"}
                r = request2DKApi(serverc, data).send()
                print(r)

        def guess_api_guessActivity_openRedPacket(self):
                """
                20、疯狂的比特游戏领取红包
                :return: 
                """
                serverc = "guess-api/guessActivity/openRedPacket"
                data = {"id":"74773",
                        "periodId":"4"}
                r = request2DKApi(serverc, data).send()
                print(r)

        def uc_activity_joinStoLock(self):
                """
                @description: CNYT锁仓，模拟多个用户锁仓
                :return: 
                """
                user_mobile = ["17700000020", "17700000021"]
                for username in user_mobile:
                        server = "uc/login"
                        data = {"username": username,
                                "password": DKApiBase().getSign("cs111111" + "hello, moto"),
                                "type": 0}
                        r = request2DKApi(server, data).send()
                        print(r)

                        serverc = "uc/activity/joinStoLock"
                        jyPassword = "111111"
                        header = {"access-auth-token": "{}".format(username)}
                        data = {"id":"50",
                                "cnyAmount":"1000",
                                "jyPassword":DKApiBase().getSign(jyPassword + "hello, moto")}
                        r = request2DKApi(serverc, data, header).send()
                        print(r)


if __name__ == "__main__":
        reqApi_1_0().uc_activity_joinStoLock()