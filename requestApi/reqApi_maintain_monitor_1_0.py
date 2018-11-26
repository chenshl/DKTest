# coding:utf-8
# @author : csl
# @date   : 2018/10/30 10:57
# 撮合器管理接口（维护人员）

import requests

class reqApi_maintain_monitor_1_0(object):
    """
    @description: 撮合器管理接口（维护人员）
    """

    def extrade_monitor_plate_reset(self):
        """
        @description: 重置盘口数据（注意，重置盘口数据的时候会暂停交易，即下单后会被取消订单）
        参数：
        symbol 交易对，必填
        direction 购买方向，可选。direction=SELL/BUY(选一)
        日志查看的关键字：“resetTradePlate：”
        查看交易盘口地址：http://www.400.pro/#/exchangemore/slu_cnyt
        :return: 
        """
        url = ""
        r = requests.get(url)
        print(r.status_code, r.text)


    def extrade_monitor_stopTrader(self):
        """
        @description: 停止撮合器（发出停止命令后需要发送下单来触发停止）
        参数：
        symbol 交易对，必填
        :return: 
        """
        url = ""
        r = requests.get(url)
        print(r.status_code, r.text)


    def extrade_monitor_resetTrader(self):
        """
        @description: 启动、重置撮合器（重置交易撮合器，根据ExchangeCoin的启用状态进行相应的启动或者暂停交易对）
        参数：
        symbol 交易对，必填
        :return: 
        """
        url = ""
        r = requests.get(url)
        print(r.status_code, r.text)


    def extrade_monitor_cancelAllOrder(self):
        """
        @description: 撤销指定撮合器中所有订单
        参数：
        symbol 交易对，必填
        日志查看的关键字：“cancelAllOrder：”
        :return: 
        """
        url = ""
        r = requests.get(url)
        print(r.status_code, r.text)


if __name__ == "__main__":
    reqApi_maintain_monitor_1_0().extrade_monitor_cancelAllOrder()