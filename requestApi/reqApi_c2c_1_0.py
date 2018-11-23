# coding:utf-8
# @author : csl
# @date   : 2018/08/01 09:16
"""C2C通用接口"""

from common.request2DKApi import request2DKApi
from common.base import DKApiBase

class reqApi_c2c_1_0(object):

    """1 广告"""
    def otc_advertise_create(self):
        """
        1.1 创建广告
        :return: 
        """
        jyPassword = "111111"
        server = "otc/advertise/create"
        data = {"price":"1",
                "advertiseType":"1",  # 0买，1卖
                "coin.id":"13",
                "minLimit":"100",
                "maxLimit":"1000",
                "timeLimit":"30",
                "country":"中国",
                "priceType":"0",
                "premiseRate":"",
                "remark":"测试广告,自动化脚本添加",
                "number":"1000",
                "pay[]":"银联",
                "auto":"1",  # 是否开启自动回复0否1是，默认否
                "autoword":"先付款，后放币",
                "needBindPhone":"1",  # 是否需要交易方已绑定手机号，0：不需要，1：需要
                "needRealname":"1",   # 是否需要交易方已做实名认证，0：不需要，1：需要
                "needTradeTimes":"10",  # 需要交易方至少完成过N笔交易（默认为0）
                "needPutonDiscount":"1",  # 是否使用优惠币种支付，0：不使用，1：使用
                "bindingResult":"",  # 绑定结果,非必传项
                "jyPassword":DKApiBase().getSign(jyPassword + "hello, moto")
                }
        r = request2DKApi(server, data,).send()
        print(r)

    def otc_advertise_all(self):
        """
        1.2 个人所有广告
        :return: 
        """
        server = "otc/advertise/all"
        data = {}
        r = request2DKApi(server, data).send()
        print(r)

    def otc_advertise_self_all(self):
        """
        1.3 个人所有广告
        :return: 
        """
        server = "otc/advertise/self/all"
        data = {}
        r = request2DKApi(server, data).send()
        print(r)

    def otc_advertise_detail(self):
        """
        1.4 广告详情
        :return: 
        """
        server = "otc/advertise/detail"
        data = {"id":"107"}
        r = request2DKApi(server, data).send()
        print(r)

    def otc_advertise_update(self):
        """
        1.5 修改广告
        :return: 
        """
        jyPassword = "111111"
        server = "otc/advertise/update"
        data = {"id":"94",
                "advertiseType":"1",
                "price":"6.82",
                "coin.id":"1",
                "minLimit":"100",
                "maxLimit":"1000",
                "timeLimit":"20",
                "country":"中国",
                "priceType":"0",
                "premiseRate":"",
                "remark":"备注信息",
                "number":"100000",
                "pay[]":"支付宝",
                "auto":"1",
                "autoword":"自动回复",
                "jyPassword":DKApiBase().getSign(jyPassword + "hello, moto")
                }
        r = request2DKApi(server, data).send()
        print(r)

    def otc_advertise_on_shelves(self):
        """
        1.6 广告上架(上架前需要修改广告卖出数量)
        :return: 
        """
        server = "otc/advertise/on/shelves"
        data = {"id":"94"}
        r = request2DKApi(server, data).send()
        print(r)

    def otc_advertise_off_shelves(self):
        """
        .7 广告下架
        :return: 
        """
        server = "otc/advertise/off/shelves"
        data = {"id":"291"}
        r = request2DKApi(server, data).send()
        print(r)

    def otc_advertise_delete(self):
        """
        1.8 删除广告
        :return: 
        """
        server = "otc/advertise/delete"
        data = {"id":"116"}  # 广告ID
        r = request2DKApi(server, data).send()
        print(r)

    def otc_advertise_excellent(self):
        """
        1.9 查询优质广告
        :return: 
        """
        server = "otc/advertise/excellent"
        data = {"advertiseType":"1"}  # 广告类型0买入1卖出
        r = request2DKApi(server, data).send()
        print(r)

    def otc_advertise_page(self):
        """
        1.10 分页查询广告
        :return: 
        """
        server = "otc/advertise/page"
        data = {"pageNo":"0",  # 非必传
                "pageSize":"5",  # 非必传
                "advertiseType":"1",  # 条件：0买、1卖
                "id":"13",  # 币种id  otc_coin表
                "isCertified":"0"  # 是否只显示认证商家.1:是0：否  # 非必传
                }
        r = request2DKApi(server, data).send()
        print(r)

    def otc_advertise_page_by_unit(self):
        """
        1.11 根据币种分页查询广告
        :return: 
        """
        server = "otc/advertise/page-by-unit"
        data = {"pageNo":"2",
                "pageSize":"10",
                "advertiseType":"0",  # 条件：0买、1卖  #必传
                "unit":"USDT",  # 币种string  必传
                "isCertified":"0"  # 是否只显示认证商家.1:是0：否
                }
        r = request2DKApi(server, data).send()
        print(r)

    def otc_advertise_member(self):
        """
        1.12 会员广告查询
        :return: 
        """
        server = "otc/advertise/member"
        data = {"name":"测试1"}  # 用户名
        r = request2DKApi(server, data).send()
        print(r)

    """2 healthy"""
    def otc_healthy_sleep_sleepTime(self):
        """
        2.1 负载均衡健康检查接口
        :return: 
        """
        sleepTime = "1"
        server = "otc/healthy/sleep/" + sleepTime
        data = {}
        r = request2DKApi(server, data).send()
        print(r)

    """3 交易"""
    def otc_order_pre(self):
        """
        3.1 买入，卖出详细信息
        :return: 
        """
        server = "otc/order/pre"
        data = {"id":"98"}  # 广告id
        r = request2DKApi(server, data).send()
        print(r)

    def otc_order_buy(self):
        """
        3.2 买币，生成订单
        :return: 
        """
        server = "otc/order/buy"
        data = {"id":"109",  # 广告id
                "coinId":"2",  # 币种id，otc_coin表ID
                "price":"6.82",  # 当前价格
                "money":"136.4",  # 金额
                "amount":"20",  # 数量
                "remark":"测试买币",  # 要求、备注，非必传
                "mode":""  # 计算方式，金额/价格=数量为0，数量*价格=金额为1，非必传，默认为0
                }
        r = request2DKApi(server, data).send()
        print(r)

    def otc_order_sell(self):
        """
        3.3 卖币
        :return: 
        """
        server = "otc/order/sell"
        data = {"id":"110",  # 广告id
                "coinId":"2",  # 币种id，otc_coin表ID
                "price":"6.85",  # 当前价格
                "money":"137",  # 金额
                "amount":"20",  # 数量
                "remark":"测试卖币",  # 要求、备注，非必传
                "mode":""  # 计算方式，金额/价格=数量为0，数量*价格=金额为1，非必传，默认为0
                }
        r = request2DKApi(server, data).send()
        print(r)

    def otc_order_self(self):
        """
        3.4 我的订单
        :return: 
        """
        server = "otc/order/self"
        data = {"status":"0",  # 订单状态， 0=已取消/1=未付款/2=已付款/3=已完成/4=申诉中
                "pageNo":"0",  # 页数,非必传
                "pageSize":"10",  # 每页数目，非必传
                "orderSn":"81390709814464512"  # 订单号
                }
        r = request2DKApi(server, data).send()
        print(r)

    def otc_order_detail(self):
        """
        3.5 订单详情
        :return: 
        """
        server = "otc/order/detail"
        data = {"orderSn":"91259656642629632"}
        r = request2DKApi(server, data).send()
        print(r)

    def otc_order_cancel(self):
        """
        3.6 取消订单（由付款方发起取消订单，买币由用户发起取消、卖币由商家发起取消）
        :return: 
        """
        server = "otc/order/cancel"
        data = {"orderSn":"81386985150877696"}
        r = request2DKApi(server, data).send()
        print(r)

    def otc_order_pay(self):
        """
        3.7 确认付款(由付款方发起付款完成，买币由用户发起付款确认、卖币由商家发起付款确认)
        :return: 
        """
        server = "otc/order/pay"
        data = {"orderSn":"81398165328236544"}
        r = request2DKApi(server, data).send()
        print(r)

    def otc_order_release(self):
        """
        3.8 订单放行（由卖方发起放行，买币由商家发起方形、卖币由用户发起放行）
        :return: 
        """
        jyPassword = "111111"
        header={"access-auth-token":"7d614fe74466a03ca3c8e7522321b2b3"}
        server = "otc/order/release"
        data = {"orderSn":"81395587148288000",
                "jyPassword":DKApiBase().getSign(jyPassword + "hello, moto")}
        r = request2DKApi(server, data, header).send()
        print(r)

    def otc_order_appeal(self):
        """
        3.9 申诉（付款方确认付款后的订单才可以发起申述，已取消和已完成的订单不可发起申述，支付完成30分钟后才可申述）
        :return: 
        """
        server = "otc/order/appeal"
        data = {"orderSn":"81398165328236544",
                "remark":"测试投诉"
                }
        r = request2DKApi(server, data).send()
        print(r)

    """4 OtcCoin"""
    def otc_coin_pcall(self):
        """
        4.1 取得正常的币种
        :return: 
        """
        server = "otc/coin/pcall"
        data = {"memberId":"80068"}
        r = request2DKApi(server, data).send()
        print(r)

    def otc_coin_all(self):
        """
        4.2 APP端取得正常的币种
        :return: 
        """
        server = "otc/coin/all"
        data = {}
        r = request2DKApi(server, data).send()
        print(r)



if __name__ == "__main__":
    reqApi_c2c_1_0().otc_advertise_page()
    # reqApi_c2c_1_0().otc_advertise_create()