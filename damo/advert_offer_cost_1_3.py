# coding:utf-8
# @author : csl
# @date   : 2018/11/05 09:48
# 交易平台v1.3迭代广告上架费用SLU支付优惠及提币手续费SLU支付优惠

class advert_offer_cost(object):
    """广告上架SLU支付优惠及提币手续费SLU支付优惠"""

    def advert_cost(self, coin, SLU):
        """
        @description: SLU优惠广告上架费用计算
        :param coin: 广告费用基币
        :param SLU: 用户SLU账户金额
        :return: 
        """
        baseCoin = 10  # 基础手续费数量
        baseCoin_USDT = 1  # 基币兑USDT价格
        baseCoin_precision = 5  # 基币设置精度
        SLU_USDT = 7.1  # SLU兑USDT价格
        discountRatio = 0.8  # 优惠比例
        discounted_price = baseCoin * baseCoin_USDT / SLU_USDT * discountRatio  # 采用SLU优惠支付时应支付的SLU数量
        print("基础广告上架费：{}{}".format(baseCoin, coin))
        print("换算成SLU优惠时应支付广告上架费：{}SLU".format(discounted_price))

        if discounted_price <= SLU:
            print("全部SLU优惠支付时广告上架费：{}SLU".format(discounted_price))
        if discounted_price > SLU:
            # SLU_num = str(SLU)[:-(8-baseCoin_precision)]
            SLU_num = SLU
            print("SLU优惠广告上架费部分：{}SLU".format(SLU_num))
            baseCoin_num = baseCoin - SLU_num * SLU_USDT / discountRatio /baseCoin_USDT
            print("SLU优惠后扣除基币广告上架费部分：{}{}".format(baseCoin_num, coin))


    def put_coin_cost(self, coin, SLU):
        """
        @description: SLU优惠提币手续费计算
        :param coin: 
        :param SLU: 
        :return: 
        """
        baseCoin = 10  # 基础手续费数量
        baseCoin_USDT = 219.8  # 基币兑CNYT价格
        baseCoin_precision = 5  # 基币设置精度
        SLU_USDT = 7.1  # SLU兑CNYT价格
        discountRatio = 0.8  # 优惠比例
        discounted_price = baseCoin * baseCoin_USDT / SLU_USDT * discountRatio  # 采用SLU优惠支付时应支付的SLU数量
        print("基础提币手续费：{}{}".format(baseCoin, coin))
        print("换算成SLU优惠时应提币手续费：{}SLU".format(discounted_price))

        if discounted_price <= SLU:
            print("全部SLU优惠支付时提币手续费：{}SLU".format(discounted_price))
        if discounted_price > SLU:
            # SLU_num = str(SLU)[:-(8 - baseCoin_precision)]
            SLU_num = SLU
            print("SLU优惠提币手续费部分：{}SLU".format(SLU_num))
            baseCoin_num = baseCoin - float(SLU_num) * SLU_USDT / discountRatio / baseCoin_USDT
            print("SLU优惠后扣除基币提币手续费部分：{}{}".format(baseCoin_num, coin))

if __name__ == "__main__":
    # advert_offer_cost().advert_cost("USDT", 0.44444444)
    advert_offer_cost().put_coin_cost("ETH", 100.00000000)