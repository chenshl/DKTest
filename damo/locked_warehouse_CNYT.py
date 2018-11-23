# coding:utf-8
# @author : csl
# @date   : 2018/11/05 17:08
# CNYT锁仓活动数据

from common.base_connect_mysql import connect_mysql

class locked_warehouse_CNYT(object):
    """CNYT锁仓活动用户数据及推荐奖励"""

    locked_money = 100.000  # 锁仓金额
    locked_phone = "17700000020"  # 锁仓用户

    # 一级推荐人
    referrer_first = connect_mysql().connect2mysql("SELECT inviter_id FROM member WHERE mobile_phone = '{}';".format(locked_phone))[0][0]
    print("用户{}的一级推荐人：{}".format(locked_phone, referrer_first))
    print("一级推荐人{}推荐返佣金额为：{}".format(referrer_first, locked_money * 0.03 * 0.15))

    # 二级推荐人
    referrer_second = connect_mysql().connect2mysql("SELECT inviter_id FROM member WHERE id = {};".format(referrer_first))[0][0]
    if referrer_second is None:
        print("用户{}无二级推荐人！！！".format(locked_phone))
    else:
        print("用户{}的二级推荐人为：{}".format(locked_phone, referrer_second))
        print("二级推荐人{}推荐返佣金额为：{}".format(referrer_second, locked_money * 0.03 * 0.09))

        # 三级推荐人
        referrer_third = connect_mysql().connect2mysql("SELECT inviter_id FROM member WHERE id = {};".format(referrer_second))[0][0]
        if referrer_third is None:
            print("用户{}无三级推荐人！！！".format(locked_phone))
        else:
            print("用户{}的三级推荐人为：{}".format(locked_phone, referrer_third))
            print("三级推荐人{}推荐返佣金额为：{}".format(referrer_third, locked_money * 0.03 * 0.06))


if __name__ == "__main__":
    locked_warehouse_CNYT()