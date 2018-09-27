# coding:utf-8
# @author : csl
# @date   : 2018/09/26 11:45
# 疯狂的比特游戏测试数据核对

from common.base_connect_mysql import connect_mysql

class crazy_BTCGame(object):

    """
    :descreption: 疯狂的比特游戏奖池分配测试数据核对
    """

    # 游戏期数
    configid = 1
    # 用户单注投注金额
    user_bet_money = 200
    # 是否开启红包：1-是，0-否
    isredpackge = 1

    # 当期用户总投币数
    all_bet_num = float(connect_mysql().connect2mysql("SELECT SUM(bet_num) FROM pg_betting_record WHERE period_id = {};".format(configid))[0][0])
    print("当期用户总投币数: {}".format(all_bet_num))

    # 上期奖池余额
    try:
        before_money = float(connect_mysql().connect2mysql("SELECT SUM(jackpot_balance + redpacket_balance) FROM pg_jackpot WHERE period_id = {};".format(configid - 1))[0][0])
    except Exception as e:
        # print(e)
        before_money = 0
    print("上期奖池余额: {}".format(before_money))

    # 当期奖池总金额
    all_money = all_bet_num + before_money
    print("当期奖池总金额: {}".format(all_money))

    # 当期分佣金额
    try:
        push_money = float(connect_mysql().connect2mysql("SELECT SUM(amount) FROM pg_branch_record WHERE period_id = {} AND business_type = 1;".format(configid))[0][0])
    except Exception as e:
        # print(e)
        push_money = 0
    print("当期分佣金额: {}".format(push_money))

    # 当期回购金额
    repurchase_money = all_money * 0.15
    print("当期回购金额：{}".format(repurchase_money))

    # 当期中奖金额
    try:
        happy_money = float(connect_mysql().connect2mysql("SELECT SUM(bet_num) FROM pg_betting_record WHERE period_id = {} AND `status` = 2;".format(configid))[0][0])
    except Exception as e:
        # print(e)
        happy_money = 0
    print("当期中奖金额: {}".format(happy_money))

    # 当期已领取红包金额
    try:
        received_redpacket_money = float(connect_mysql().connect2mysql("SELECT SUM(reward_num) FROM pg_reward WHERE period_id = {} AND business_type = 1 AND `status` = 4;".format(configid))[0][0])
    except Exception as e:
        # print(e)
        received_redpacket_money = 0
    print("当期已领取红包金额: {}".format(received_redpacket_money))

    # 当期已领取的奖励
    try:
        received_money = float(connect_mysql().connect2mysql("SELECT SUM(reward_num) FROM pg_reward WHERE period_id = {} AND business_type = 0 AND `status` = 1;".format(configid))[0][0])
    except Exception as e:
        # print(e)
        received_money = 0
    print("当期已领取的奖励: {}".format(received_money))

    # 本期累计到下期奖池总金额
    try:
        this_follow_money = float(connect_mysql().connect2mysql("SELECT SUM(jackpot_balance + redpacket_balance) FROM pg_jackpot WHERE period_id = {};".format(configid))[0][0])
    except Exception as e:
        # print(e)
        this_follow_money = 0
    print("本期累计到下期奖池总金额: {}".format(this_follow_money))

    # 本期分配红包总金额
    # this_redpacket_money = all_bet_num * 0.05
    if isredpackge == 1:
        this_redpacket_money = all_money * 0.05
    elif isredpackge == 0:
        this_redpacket_money = 0
    print("本期分配红包总金额: {}".format(this_redpacket_money))

    # 奖金计算
    # 当期奖池金额
    if isredpackge == 1:
        this_money = all_money - all_bet_num * 0.25 - push_money
    elif isredpackge == 0:
        this_money = all_money - all_bet_num * 0.2 - push_money
    print("当期奖池金额: {}".format(this_money))

    # 用户奖励计算
    if received_money == 0:
        print("当期中奖金额为0,不产生奖励")
        user_get_money = 0
    else:
        if isredpackge == 1:
            # user_get_money = (all_money - all_bet_num * 0.25 - push_money) / happy_money * user_bet_money
            user_get_money = (all_money - all_money * 0.25 - push_money) / happy_money * user_bet_money
        elif isredpackge == 0:
            user_get_money = (all_money - all_money * 0.2 - push_money) / happy_money * user_bet_money
    print("******")
    # print("(当期奖池总金额{} - 25%当期用户总投币数{} - 当期分佣金额{}) / 当期中奖金额{} * 用户单注投注金额{} = {}".format(all_money, all_money * 0.25, push_money, happy_money, user_bet_money, user_get_money))
    print("用户获取奖励：{}".format(user_get_money))

    # 下期奖池沉淀计算  下期结余=奖池金额+本期沉淀-已经领取的奖励
    follow_money = this_money + all_bet_num * 0.05 - received_money
    # print("当期奖池金额{} + 5%下期沉淀{} - 当期已领取的奖励{} = {}".format(this_money, all_bet_num * 0.05, received_money, follow_money))
    print("下期奖池沉淀计算: {}".format(follow_money))

    # 累计到下期的红包金额
    follow_redpacket_money = this_redpacket_money - received_redpacket_money
    print("累计到下期的红包金额: {}".format(follow_redpacket_money))

    # 总金额核对  本期投票金额+上期总结余金额 = 本期已领取分佣金额 + 本期已红包领取金额 + 本期回购金额 + 本期已领取奖励金额 + 累计到下期奖池（奖励+红包）
    # result = push_money + received_redpacket_money + repurchase_money + received_money + this_follow_money
    if result == all_money:
        print("本期共进金额：{}=本期共出金额：{}".format(all_money, result))
    else:
        print("本期共进金额：{}!=本期共出金额：{}".format(all_money, result))



if __name__ == "__main__":
    crazy_BTCGame()