# coding:utf-8
# @author : csl
# @date   : 2018/07/27
"""币币交易通用接口"""

from common.request2DKApi import request2DKApi

"""1、交易币"""
# 1.1、获取基币
# serverc = "exchange/exchange-coin/base-symbol"
# data = {}

"""2、自选"""
# 2.1、添加自选
# serverc = "exchange/favor/add"
# data = {"symbol":"SLB/USDT"}

# 2.2、查询当前用户自选
# serverc = "exchange/favor/find"
# data = {}

# 2.3、删除自选
# serverc = "exchange/favor/delete"
# data = {"symbol":"SLB/USDT"}

"""3、healthy"""
# 3.1、负载均衡健康检查接口
# sleepTime = "10"
# serverc = "exchange/healthy/sleep/" + sleepTime
# data = {}

"""4、委托订单处理类"""
# 4.1、添加委托订单
# serverc = "exchange/order/add"
# data = {
#         "symbol":"SLB/USDT",
#         "price":"0.08",
#         "amount":"100",
#         "direction":"1",  # 买卖方向，0=BUY（买）/1=SELL（卖）
#         "type":"1"  # 交易类型，1=LIMIT_PRICE(限价交易)
#         }

# 4.2、历史委托
# serverc = "exchange/order/history"
# data = {"symbol":"SLB/USDT",
#         "pageNo":"0",
#         "pageSize":"10"
#         }

# 4.3、当前委托（从只读库中获取数据）
# serverc = "exchange/order/current"
# data = {"symbol":"SLB/USDT",
#         "pageNo":"0",  # 请求开始页码，从0开始
#         "pageSize":"100"  # 请求数量
#         }

# 4.4、查询订单明细
# serverc = "exchange/order/orderInfo"
# data = {"orderId":"E211124413854060544"
#         }

# 4.5、查询委托成交明细
# orderId = "E214388705424510976"
# serverc = "exchange/order/detail/" + orderId
# data = {}
# E208961450858713088   E208959272001671168

# 4.6、取消委托
# orderId = "E214053570116259840"
# serverc = "exchange/order/cancel/" + orderId
# data = {}




r = request2DKApi(serverc, data).send()
print(r)