# coding:utf-8
# @author : csl
# @date   : 2018/07/27
"""币币交易通用接口"""

from common.request2DKApi import request2DKApi

class reqApi_exchange_1_0(object):

    """1、交易币"""
    def exchange_exchange_coin_base_symbol(self):
        """
        1.1、获取基币
        :return: 
        """
        serverc = "exchange/exchange-coin/base-symbol"
        data = {}
        r = request2DKApi(serverc, data).send()
        print(r)

    """2、自选"""
    def exchange_favor_add(self):
        """
        2.1、添加自选
        :return: 
        """
        serverc = "exchange/favor/add"
        data = {"symbol":"SLB/USDT"}
        r = request2DKApi(serverc, data).send()
        print(r)

    def exchange_favor_find(self):
        """
        2.2、查询当前用户自选
        :return: 
        """
        serverc = "exchange/favor/find"
        data = {}
        r = request2DKApi(serverc, data).send()
        print(r)

    def exchange_favor_delete(self):
        """
        2.3、删除自选
        :return: 
        """
        serverc = "exchange/favor/delete"
        data = {"symbol":"SLB/USDT"}
        r = request2DKApi(serverc, data).send()
        print(r)

    """3、healthy"""
    def exchange_healthy_sleep_sleepTime(self):
        """
        3.1、负载均衡健康检查接口
        :return: 
        """
        sleepTime = "10"
        serverc = "exchange/healthy/sleep/" + sleepTime
        data = {}
        r = request2DKApi(serverc, data).send()
        print(r)

    """4、委托订单处理类"""
    def exchange_order_add(self):
        """
        4.1、添加委托订单
        :return: 
        """
        serverc = "exchange/order/add"
        data = {
                "symbol":"SLB/USDT",
                "price":"0.08",
                "amount":"100",
                "direction":"1",  # 买卖方向，0=BUY（买）/1=SELL（卖）
                "type":"1"  # 交易类型，1=LIMIT_PRICE(限价交易)
                }
        r = request2DKApi(serverc, data).send()
        print(r)

    def exchange_order_history(self):
        """
        4.2、历史委托
        :return: 
        """
        serverc = "exchange/order/history"
        data = {"symbol":"SLB/USDT",
                "pageNo":"0",
                "pageSize":"10"
                }
        r = request2DKApi(serverc, data).send()
        print(r)

    def exchange_order_current(self):
        """
        4.3、当前委托（从只读库中获取数据）
        :return: 
        """
        serverc = "exchange/order/current"
        data = {"symbol":"SLB/USDT",
                "pageNo":"0",  # 请求开始页码，从0开始
                "pageSize":"100"  # 请求数量
                }
        r = request2DKApi(serverc, data).send()
        print(r)

    def exchange_order_orderInfo(self):
        """
        4.4、查询订单明细
        :return: 
        """
        serverc = "exchange/order/orderInfo"
        data = {"orderId":"E211124413854060544"
                }
        r = request2DKApi(serverc, data).send()
        print(r)

    def exchange_order_detail(self):
        """
        4.5、查询委托成交明细
        :return: 
        """
        orderId = "E214388705424510976"
        serverc = "exchange/order/detail/" + orderId
        data = {}
        r = request2DKApi(serverc, data).send()
        print(r)
        # E208961450858713088   E208959272001671168

    def exchange_order_cancel_orderId(self):
        """
        4.6、取消委托
        :return: 
        """
        orderId = "E214053570116259840"
        serverc = "exchange/order/cancel/" + orderId
        data = {}
        r = request2DKApi(serverc, data).send()
        print(r)


if __name__ == "__main__":
    reqApi_exchange_1_0().exchange_order_detail()