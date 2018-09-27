# coding:utf-8
# @author : csl
# @date   : 2018/07/24 13:50
"""
用于手动接口探测币币交易
"""

from common.request2DKApi import request2DKApi
from common.base import DKApiBase

# 1、登录接口
# serverc = "uc/login"
# platformPassword = "csl53241csl"
# data = {"username":"17723159468",
#         "password":DKApiBase().getSign(platformPassword + "hello, moto")}

# 2、订单委托接口
# serverc = "exchange/order/add"
# data = {
#         "symbol":"SLB/USDT",
#         "price":"0.00016115",
#         "amount":"1",
#         "direction":"0",  # 买卖方向，0=BUY（买）/1=SELL（卖）
#         "type":"1"  # 交易类型，1=LIMIT_PRICE(限价交易)
#         }

# 3、查询当前委托订单接口
# serverc = "exchange/order/current"
# data = {"symbol":"SLB/USDT",
#         "pageNo":"0",  # 请求开始页码，从0开始
#         "pageSize":"100"  # 请求数量
#         }

# 4、查询历史委托订单接口
# serverc = "exchange/order/history"
# data = {"symbol":"SLU/USDT",
#         "pageNo":"0",
#         "pageSize":"10"
#         }

# 5、撤销委托订单接口,撤销订单添加到请求地址后面,无请求参数
# orderNo = "E216192287807311872"
# serverc = "exchange/order/cancel/" + orderNo
# data = {}

# 6、获取指定交易对的配置信息接口
# serverc = "market/symbol-info"
# data = {"symbol":"SLB/USDT"}

# 7、获取所有交易对信息接口
# serverc = "market/symbol"
# data = {}

# 8、获取所有交易对的当前行情信息接口
# serverc = "market/symbol-thumb"
# data = {}

# 9、获取K线数据接口
# fromdate = "2018-07-26 00:00:00"
# # todate = "2018-07-24 00:00:00"
# serverc = "market/history"
# data = {"symbol":"SLB/USDT",
#         "from":DKApiBase().time2Timestamps(fromdate),  # 开始时间戳
#         "to":DKApiBase().nowtime2Timestamps(),  # 截至时间戳
#         "resolution":"1"  # K线类型：1=1分/5=5分/15=15分/30=30分/1h=小时/1d=天/1m=月
#         }

# 10、获取买卖盘口信息接口
# serverc = "market/exchange-plate"
# data = {"symbol":"SLB/USDT"}

# 11、获取最新实时成交记录接口
# serverc = "market/latest-trade"
# data = {"symbol":"SLB/USDT",
#         "size":"50"  # 记录数量
#         }

# 12、资产查询接口，币种名称加在请求路径后面
# coinName = "SLB"
# serverc = "uc/asset/wallet/" + coinName
# data = {}

# 13、币种资料列表查询接口
# serverc = "uc/ancillary/system/help"
# data = {"sysHelpClassification":"COIN_INFO"}

# 14、获取指定币种资料
# coinId = "6"
# serverc = "uc/ancillary/system/help/" + coinId
# data = {}

# 15、公告列表查询接口
# serverc = "uc/announcement/page"
# data = {"pageNo":"1",
#         "pageSize":"10"
#         }

# 16、获取公告内容
# requestMark = "GET"
# announcementID = "8"
# serverc = "uc/announcement/" + announcementID
# data = {}

# 17、订单明细查询接口
# serverc = "exchange/order/orderInfo"
# data = {"orderId":"E211127401079312384"
#         }

# 18、用户钱包信息
# serverc = "uc/asset/wallet"
# data = {}


# 19、疯狂的比特游戏领取奖励
# serverc = "guess-api/guessActivity/receiveAward"
# data = {"periodId":"4"}

# 20、疯狂的比特游戏领取红包
serverc = "guess-api/guessActivity/openRedPacket"
data = {"id":"74773",
        "periodId":"4"}

# r = request2DKApi(serverc, data).send(requestMark)
r = request2DKApi(serverc, data).send()
print(r)