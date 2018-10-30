# coding:utf-8
# @author : csl
# @date   : 2018/10/23 09:30
# 疯狂的比特游戏接口

from common.request2DKApi import request2DKApi
from common.base import DKApiBase

class reqApi_crazy_BTGame_1_3(object):
    """疯狂的BTMC游戏"""

    def guess_api_guessActivity_betting(self):
        """
        投票活动
        :return: 
        """
        server = "guess-api/guessActivity/betting"
        platformPassword = "111111"
        header = [{"access-auth-token":"d809615e96176085a1152f74c8a47b78800141539678969628"}, {"access-auth-token":"f2794f54e17720d34aa505e3556724f3"}, {"access-auth-token":"492675514ec5f4d8ee249f26b15a4746"}]
        for i in range (0, 20):
            for hd in header:
                data = {"periodId":"8",  # 期数id
                        "coinNum":"11",  # 投注数
                        "rangeId":"25",  # 投注区间范围id
                        "jyPassword":DKApiBase().getSign(platformPassword + "hello, moto"),  # 资金密码
                        "useSms":"0"  # 是否用短信0否，1是
                        }
                r = request2DKApi(server, data, hd).send()
                print(r)


    def guess_api_guessActivity_receiveAward(self):
        """
        中奖，领取奖励
        :return: 
        """
        for i in  range (0, 5):
            server = "guess-api/guessActivity/receiveAward"
            data = {"periodId":"8"}
            r = request2DKApi(server, data).send()
            print(r)


    def guess_api_guessActivity_openRedPacket(self):
        """
        开启红包
        :return: 
        """
        for i in range (0, 5):
            server = "guess-api/guessActivity/openRedPacket"
            data = {"id":"74773",  # userId
                    "periodId":"8"}

            r = request2DKApi(server, data).send()
            print(r)


if __name__ == "__main__":
    reqApi_crazy_BTGame_1_3().guess_api_guessActivity_receiveAward()