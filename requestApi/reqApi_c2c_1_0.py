# coding:utf-8
# @author : csl
# @date   : 2018/08/01 09:16
"""C2C通用接口"""

from common.request2DKApi import request2DKApi
from common.base import DKApiBase

"""1 广告"""
# 1.1 创建广告
# jyPassword = "111111"
# server = "otc/advertise/create"
# data = {"price":"6.82",
#         "advertiseType":"1",
#         "coin.id":"2",
#         "minLimit":"100",
#         "maxLimit":"1000",
#         "timeLimit":"15",
#         "country":"中国",
#         "priceType":"0",
#         "premiseRate":"",
#         "remark":"测试广告",
#         "number":"10000",
#         "pay[]":"微信",
#         "auto":"1",
#         "autoword":"先付款，后放币",
#         "jyPassword":DKApiBase().getSign(jyPassword + "hello, moto")
#         }

# 1.2 个人所有广告
# server = "otc/advertise/all"
# data = {}

# 1.3 个人所有广告
# server = "otc/advertise/self/all"
# data = {}

# 1.4 广告详情
# server = "otc/advertise/detail"
# data = {"id":"107"}

# 1.5 修改广告
# jyPassword = "111111"
# server = "otc/advertise/update"
# data = {"id":"94",
#         "advertiseType":"1",
#         "price":"6.82",
#         "coin.id":"1",
#         "minLimit":"100",
#         "maxLimit":"1000",
#         "timeLimit":"20",
#         "country":"中国",
#         "priceType":"0",
#         "premiseRate":"",
#         "remark":"备注信息",
#         "number":"100000",
#         "pay[]":"支付宝",
#         "auto":"1",
#         "autoword":"自动回复",
#         "jyPassword":DKApiBase().getSign(jyPassword + "hello, moto")
#         }

# 1.6 广告上架(上架前需要修改广告卖出数量)
# server = "otc/advertise/on/shelves"
# data = {"id":"94"}

# 1.7 广告下架
# server = "otc/advertise/off/shelves"
# data = {"id":"94"}

# 1.8 删除广告
# server = "otc/advertise/delete"
# data = {"id":"116"}  # 广告ID

# 1.9 查询优质广告
# server = "otc/advertise/excellent"
# data = {"advertiseType":"1"}  # 广告类型0买入1卖出

# 1.10 分页查询广告
# server = "otc/advertise/page"
# data = {"pageNo":"0",  # 非必传
#         "pageSize":"10",  # 非必传
#         "advertiseType":"0",  # 条件：0买、1卖
#         "id":"2",  # 币种id  otc_coin表
#         "isCertified":"0"  # 是否只显示认证商家.1:是0：否  # 非必传
#         }

# 1.11 根据币种分页查询广告
# server = "otc/advertise/page-by-unit"
# data = {"pageNo":"2",
#         "pageSize":"10",
#         "advertiseType":"0",  # 条件：0买、1卖  #必传
#         "unit":"USDT",  # 币种string  必传
#         "isCertified":"0"  # 是否只显示认证商家.1:是0：否
#         }

# 1.12 会员广告查询
# server = "otc/advertise/member"
# data = {"name":"测试1"}  # 用户名

"""2 healthy"""
# 2.1 负载均衡健康检查接口
# sleepTime = "1"
# server = "otc/healthy/sleep/" + sleepTime
# data = {}

"""3 交易"""
# 3.1 买入，卖出详细信息
# server = "otc/order/pre"
# data = {"id":"98"}  # 广告id

# 3.2 买币，生成订单
# server = "otc/order/buy"
# data = {"id":"109",  # 广告id
#         "coinId":"2",  # 币种id，otc_coin表ID
#         "price":"6.82",  # 当前价格
#         "money":"136.4",  # 金额
#         "amount":"20",  # 数量
#         "remark":"测试买币",  # 要求、备注，非必传
#         "mode":""  # 计算方式，金额/价格=数量为0，数量*价格=金额为1，非必传，默认为0
#         }

# 3.3 卖币
# server = "otc/order/sell"
# data = {"id":"110",  # 广告id
#         "coinId":"2",  # 币种id，otc_coin表ID
#         "price":"6.85",  # 当前价格
#         "money":"137",  # 金额
#         "amount":"20",  # 数量
#         "remark":"测试卖币",  # 要求、备注，非必传
#         "mode":""  # 计算方式，金额/价格=数量为0，数量*价格=金额为1，非必传，默认为0
#         }

# 3.4 我的订单
# server = "otc/order/self"
# data = {"status":"0",  # 订单状态， 0=已取消/1=未付款/2=已付款/3=已完成/4=申诉中
#         "pageNo":"0",  # 页数,非必传
#         "pageSize":"10",  # 每页数目，非必传
#         "orderSn":"81390709814464512"  # 订单号
#         }

# 3.5 订单详情
# server = "otc/order/detail"
# data = {"orderSn":"91259656642629632"}

# 3.6 取消订单（由付款方发起取消订单，买币由用户发起取消、卖币由商家发起取消）
# server = "otc/order/cancel"
# data = {"orderSn":"81386985150877696"}

# 3.7 确认付款(由付款方发起付款完成，买币由用户发起付款确认、卖币由商家发起付款确认)
# server = "otc/order/pay"
# data = {"orderSn":"81398165328236544"}

# 3.8 订单放行（由卖方发起放行，买币由商家发起方形、卖币由用户发起放行）
# jyPassword = "111111"
# header={"access-auth-token":"7d614fe74466a03ca3c8e7522321b2b3"}
# server = "otc/order/release"
# data = {"orderSn":"81395587148288000",
#         "jyPassword":DKApiBase().getSign(jyPassword + "hello, moto")}
# r = request2DKApi(server, data, header).send()
# print(r)

# 3.9 申诉（付款方确认付款后的订单才可以发起申述，已取消和已完成的订单不可发起申述，支付完成30分钟后才可申述）
# server = "otc/order/appeal"
# data = {"orderSn":"81398165328236544",
#         "remark":"测试投诉"
#         }

"""4 OtcCoin"""
# 4.1 取得正常的币种
# server = "otc/coin/pcall"
# data = {"memberId":"74773"}

# 4.2 APP端取得正常的币种
# server = "otc/coin/all"
# data = {}

r = request2DKApi(server, data).send()
print(r)