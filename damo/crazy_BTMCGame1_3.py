# coding:utf-8
# @author : csl
# @date   : 2018/10/18 15:14

from common.base_connect_mysql import connect_mysql

class crazy_BTMCGame_up(object):
    """
    @descreption: 疯狂的比特游戏新规则数据核对
    展示数据：总奖池累计；中奖用户数；本期中奖奖池；BTMC中奖价格；本期红包奖励总数；本期推荐分红总数；本期回购总数；
    本期沉淀总数；本期用户投币总数；本期中奖系数；本期已分佣BTMC数量；本期已领取奖励BTMC数量；本期已领取红包BTMC数量；
    本期单个用户中奖BTMC计算；本期分配后累计到下期BTMC数量；本期红包领取后剩余数量；本期共进BTMC及本期共出BTMC数量
    """

    # 游戏期数
    configid = 34
    # 用户单注投注金额
    user_bet_money = 100

    # 数据库基础数据查询
    print("************由数据库查询获得的基础数据************")
    # 上期奖池总结余=上期分配结余+上期红包结余
    try:
        before_money = float(connect_mysql().connect2mysql("SELECT SUM(jackpot_balance + redpacket_balance) FROM pg_jackpot WHERE period_id = {};".format(configid - 1))[0][0])
    except Exception as e:
        # print(e)
        before_money = 0
        # before_money = 35380.44968840 + 2527.17497775
    print("上期奖池余额：{}".format(before_money))

    # 本期用户总投币数
    all_bet_num = float(connect_mysql().connect2mysql(
        "SELECT SUM(bet_num) FROM pg_betting_record WHERE period_id = {};".format(configid))[0][0])
    print("本期用户总投币数：{}".format(all_bet_num))

    # 本期总奖池累计=上期奖池总结余+本期用户总投币数
    all_money = all_bet_num + before_money
    print("本期奖池总金额：{}".format(all_money))

    # 本期已分配的分佣金额
    try:
        push_money = float(connect_mysql().connect2mysql("SELECT SUM(amount) FROM pg_branch_record WHERE period_id = {} AND business_type = 1;".format(configid))[0][0])
    except Exception as e:
        # print(e)
        push_money = 0
    print("本期已分配的分佣金额：{}".format(push_money))

    # 本期中奖BTMC总数
    try:
        happy_money = float(connect_mysql().connect2mysql(
            "SELECT SUM(bet_num) FROM pg_betting_record WHERE period_id = {} AND `status` = 2;".format(configid))[0][0])
    except Exception as e:
        # print(e)
        happy_money = 0
    print("本期中奖BTMC总数：{}".format(happy_money))

    # 本期中奖用户数
    try:
        this_winning_user = float(connect_mysql().connect2mysql("SELECT COUNT(*) FROM pg_betting_record WHERE period_id = {} AND `status` = 2;".format(configid))[0][0])
    except Exception as e:
        this_winning_user = 0
    print("本期中奖用户数：{}".format(this_winning_user))

    # 本期参与总人数
    try:
        this_user_num = float(connect_mysql().connect2mysql("SELECT count(distinct member_id) FROM pg_betting_record WHERE period_id = {};".format(configid))[0][0])
        print("本期参与总人数：{}".format(this_user_num))
    except Exception as e:
        print("本期参与总人数查询结果错误：{}".format(e))

    # 本期投票总次数
    try:
        this_vote_num = float(connect_mysql().connect2mysql("SELECT COUNT(*) FROM pg_betting_record WHERE period_id = {};".format(configid))[0][0])
        print("本期投票总次数：{}".format(this_vote_num))
    except Exception as e:
        print("本期投票总次数查询结果错误：{}".format(e))

    # 本期参与新用户数
    try:
        this_new_user_num = connect_mysql().connect2mysql("""SELECT COUNT(*) FROM member m RIGHT JOIN 
        (SELECT distinct pr.member_id memberID, pc.begin_time bgt, pc.end_time edt FROM pg_betting_config pc LEFT JOIN pg_betting_record pr ON pc.id = pr.period_id WHERE pr.period_id = {}) b 
        ON m.id = b.memberID WHERE m.registration_time >= b.bgt AND m.registration_time <= b.edt;""".format(configid))[0][0]
        print("本期参与新用户数：{}".format(this_new_user_num))
    except Exception as e:
        print("本期参与新用户数查询结果错误：{}".format(e))

    # 本期新用户投票总次数
    try:
        this_new_user_vote_num = connect_mysql().connect2mysql("""SELECT COUNT(*) FROM pg_betting_record WHERE member_id IN (SELECT id FROM member m RIGHT JOIN 
        (SELECT distinct pr.member_id memberID, pc.begin_time bgt, pc.end_time edt FROM pg_betting_config pc LEFT JOIN pg_betting_record pr ON pc.id = pr.period_id WHERE pr.period_id = {}) b 
        ON m.id = b.memberID WHERE m.registration_time >= b.bgt AND m.registration_time <= b.edt) AND period_id = {};""".format(configid, configid))[0][0]
        print("本期新用户投票总次数：{}".format(this_new_user_vote_num))
    except Exception as e:
        print("本期新用户投票总次数查询结果错误：{}".format(e))

    # 本期新用户投票总额
    try:
        this_new_user_vote_amount = connect_mysql().connect2mysql("""SELECT SUM(bet_num) FROM pg_betting_record WHERE member_id IN (SELECT id FROM member m RIGHT JOIN 
        (SELECT distinct pr.member_id memberID, pc.begin_time bgt, pc.end_time edt FROM pg_betting_config pc LEFT JOIN pg_betting_record pr ON pc.id = pr.period_id WHERE pr.period_id = {}) b 
        ON m.id = b.memberID WHERE m.registration_time >= b.bgt AND m.registration_time <= b.edt) AND period_id = {};""".format(configid, configid))[0][0]
        if this_new_user_vote_amount is None:
            print("本期新用户投票总额：{}".format(0))
        else:
            print("本期新用户投票总额：{}".format(float(this_new_user_vote_amount)))
    except Exception as e:
        print("本期新用户投票总额查询结果错误：{}".format(e))

    # 本期新用户中奖人数
    try:
        this_new_user_winner = connect_mysql().connect2mysql("""SELECT COUNT(*) FROM pg_betting_record WHERE member_id IN (SELECT id FROM member m RIGHT JOIN 
        (SELECT distinct pr.member_id memberID, pc.begin_time bgt, pc.end_time edt FROM pg_betting_config pc LEFT JOIN pg_betting_record pr ON pc.id = pr.period_id WHERE pr.period_id = {} AND pr.`status` = 2) b 
        ON m.id = b.memberID WHERE m.registration_time >= b.bgt AND m.registration_time <= b.edt) AND period_id = {};""".format(configid, configid))[0][0]
        print("本期新用户中奖人数：{}".format(this_new_user_winner))
    except Exception as e:
        print("本期新用户中奖人数查询结果错误：{}".format(e))

    # 本期新用户中奖金额
    try:
        this_new_user_winning_num = connect_mysql().connect2mysql("""SELECT SUM(bet_num) FROM pg_betting_record WHERE member_id IN (SELECT id FROM member m RIGHT JOIN 
        (SELECT distinct pr.member_id memberID, pc.begin_time bgt, pc.end_time edt FROM pg_betting_config pc LEFT JOIN pg_betting_record pr ON pc.id = pr.period_id WHERE pr.period_id = {} AND pr.`status` = 2) b 
        ON m.id = b.memberID WHERE m.registration_time >= b.bgt AND m.registration_time <= b.edt) AND period_id = {};""".format(configid, configid))[0][0]
        if this_new_user_winning_num is None:
            print("本期新用户中奖金额：{}".format(0))
        else:
            print("本期新用户中奖金额：{}".format(float(this_new_user_winning_num)))
    except Exception as e:
        print("本期新用户中奖金额查询结果错误：{}".format(e))

    # 本期老用户中奖人数
    try:
        this_old_user_winner = connect_mysql().connect2mysql("""SELECT COUNT(*) FROM pg_betting_record WHERE member_id IN (SELECT id FROM member m RIGHT JOIN 
        (SELECT distinct pr.member_id memberID, pc.begin_time bgt, pc.end_time edt FROM pg_betting_config pc LEFT JOIN pg_betting_record pr ON pc.id = pr.period_id WHERE pr.period_id = {} AND pr.`status` = 2) b 
        ON m.id = b.memberID WHERE m.registration_time <= b.bgt or m.registration_time >= b.edt) AND period_id = {};""".format(configid, configid))[0][0]
        print("本期老用户中奖人数：{}".format(this_old_user_winner))
    except Exception as e:
        print("本期老用户中奖人数查询结果错误：{}".format(e))

    # 本期老用户中奖金额=中奖金额-新用户中奖金额
    if this_new_user_winning_num is None:
        this_old_user_winning_num = all_money * 0.65 - 0
    else:
        this_old_user_winning_num = all_money * 0.65 - float(this_new_user_winning_num)
    print("本期老用户中奖金额：{}".format(this_old_user_winning_num))

    # 本期已领取中奖奖励
    try:
        received_money = float(connect_mysql().connect2mysql(
            "SELECT SUM(reward_num) FROM pg_reward WHERE period_id = {} AND business_type = 0 AND `status` = 1;".format(configid))[0][0])
    except Exception as e:
        # print(e)
        received_money = 0
    print("本期已领取的中奖奖励：{}".format(received_money))

    # 本期已领取红包金额
    try:
        received_redpacket_money = float(connect_mysql().connect2mysql("SELECT SUM(reward_num) FROM pg_reward WHERE period_id = {} AND business_type = 1 AND `status` = 4;".format(configid))[0][0])
    except Exception as e:
        # print(e)
        received_redpacket_money = 0
    print("本期已领取红包金额：{}".format(received_redpacket_money))

    # 计算数据
    print("************计算获得数据************")
    # 本期中奖奖池=总奖池*0.65
    this_winning_pool = all_money * 0.65
    print("本期中奖奖池：{}".format(this_winning_pool))

    # 本期红包奖励总数=总奖池*0.05
    this_red_envelope = all_money * 0.05
    print("本期红包奖励：{}".format(this_red_envelope))

    # 本期推荐分红总数=总奖池*0.1
    this_recommended_dividends = all_money * 0.1
    print("本期推荐分红：{}".format(this_recommended_dividends))

    # 本期回购总数=总奖池*0.15
    this_repurchase = all_money * 0.15
    print("本期SLU回购：{}".format(this_repurchase))

    # 本期沉淀总数=总奖池*0.05
    this_precipitation = all_money * 0.05
    print("本期奖池沉淀：{}".format(this_precipitation))

    # 本期中奖系数=中奖奖池/本期中奖BTMC总数
    if happy_money != 0:
        this_winning_factor = this_winning_pool / happy_money
    else:
        this_winning_factor = 0
    print("本期中奖系数：{}".format(this_winning_factor))

    # 本期单个用户中奖数额计算=本期中奖系数*投注金额
    this_user_wins_num = this_winning_factor * user_bet_money
    print("本期单个用户中奖数额计算：{}".format(this_user_wins_num))

    # 下期奖池沉淀总数=5%总奖池固定沉淀+中奖用户未领取部分+红包未领取部分
    next_pool_precipitation = this_precipitation + (this_winning_pool - received_money) + (this_red_envelope - received_redpacket_money)
    print("下期奖池沉淀总数：{}".format(next_pool_precipitation))

    # 本期奖池剩余=5%总奖池固定沉淀+中奖用户未领取部分
    next_pool_money = this_precipitation + (this_winning_pool - received_money)
    print("本期奖池剩余：{}".format(next_pool_money))

    # 本期红包剩余
    next_redpacket_money = this_red_envelope - received_redpacket_money
    print("本期红包剩余：{}".format(next_redpacket_money))

    # 本期回购总金额=15%总奖池固定回购+无推荐用户的分佣部分
    this_total_repurchase = this_repurchase + (this_recommended_dividends - push_money)
    print("本期回购总金额：{}".format(this_total_repurchase))

    # 本期支出总金额=下期奖池沉淀+本期回购总金额+本期已分配的分佣金额+本期已领取中奖奖励+本期已领取红包金额
    this_total_expenditure = next_pool_precipitation + this_total_repurchase + push_money + received_money + received_redpacket_money
    if this_total_expenditure == all_money:
        print("本期支出金额总数：{} = 本期收入总金额：{}".format(this_total_expenditure, all_money))
    else:
        print("本期支出金额总数：{} != 本期收入总金额：{}".format(this_total_expenditure, all_money))


if __name__ == "__main__":
    crazy_BTMCGame_up()

