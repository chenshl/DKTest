# coding:utf-8
# author : csl
# date   : 2018/11/21 17:42
# 数据库添加疯狂游戏配置

import pymysql
import time


# 游戏投票开始时间
begin_time = "2018-11-23 18:06:00"


class connect_mysql():
    """连接数据库"""
    def __init__(self):

        # 连接数据库
        try:
            # 测试库
            self.connect = pymysql.Connect(
                host='172.16.0.66',
                port=3306,
                user='bjxy_db',
                passwd='Credit2016Admin',
                db='otc_sync',
                charset='utf8'
            )

        except Exception as e:
            # logger.error("连接数据库失败", e)
            print("连接数据库失败", e)

    # 连接操作
    def connect2mysql(self, complySql):

        try:
            # 获取游标
            self.cursor = self.connect.cursor()
            self.cursor.execute(complySql)
        except Exception as e:
            self.connect.rollback()
            # logger.error("数据库事务处理失败。。。", e)
            print("数据库事务处理失败。。。", e)
        else:
            self.connect.commit()
            self.mysql_result = self.cursor.fetchall()
            # logger.info("执行SQL：{}".format(complySql))
            print("执行SQL：{}".format(complySql))
            # print("数据库事务处理成功。。。")

            return self.mysql_result
        finally:
            # 关闭游标，关闭连接
            self.cursor.close()
            self.connect.close()





timeArray = time.strptime(begin_time, "%Y-%m-%d %H:%M:%S")
# 初始时间转换成时间戳
stime = int(round(time.mktime(timeArray)))
end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stime + 300))
open_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stime + 480))
prize_end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stime + 780))

# 查询配置表ID当成活动期数
config_id_sql = """SELECT id FROM pg_betting_config ORDER BY id DESC LIMIT 1;"""
config_id = connect_mysql().connect2mysql(config_id_sql)[0][0]

create_cofig_sql = """INSERT INTO pg_betting_config (
	`period`,
	`name`,
	`begin_time`,
	`end_time`,
	`open_time`,
	`prize_begin_time`,
	`prize_end_time`,
	`redpacket_begin_time`,
	`redpacket_end_time`,
	`status`,
	`remark`,
	`create_by`,
	`create_time`,
	`update_by`,
	`update_time`,
	`deleted`,
	`bet_symbol`,
	`lower_limit`,
	`guess_symbol`,
	`prize_symbol`,
	`redpacket_symbol`,
	`redpacket_grade_ratio`,
	`redpacket_use_num`,
	`redpacket_state`,
	`redpacket_open_limit`,
	`redpacket_prize_symbol`,
	`redpacket_coefficient_ratio`,
	`sms_symbol`,
	`sms_use_num`,
	`rebate_ratio`,
	`prize_ratio`,
	`back_ratio`,
	`redpacket_ratio`,
	`next_period_ratio`
)
VALUES
	(
		'{}',
		'疯狂的BTMC',
		'{}',
		'{}',
		'{}',
		'{}',
		'{}',
		'{}',
		'{}',
		0,
		'test',
		'root',
		'{}',
		NULL,
		NULL,
		0,
		'BTMC',
		10.00000000,
		'BTMC',
		'BTMC',
		'SLU',
		0.5000,
		5.00000000,
		1,
		20.00000000,
		'BTMC',
		0.7000,
		'SLU',
		1.00000000,
		0.1000,
		0.6500,
		0.1500,
		0.0500,
		0.0500
	);
""".format(config_id, begin_time, end_time, open_time, open_time, prize_end_time, open_time, prize_end_time, begin_time)
connect_mysql().connect2mysql(create_cofig_sql)

config_id_sql = """SELECT id FROM pg_betting_config ORDER BY id DESC LIMIT 1;"""
period_id = connect_mysql().connect2mysql(config_id_sql)[0][0]
create_range_sql1 = """INSERT INTO pg_betting_price_range (`period_id`, `group_name`, `begin_range`, `end_range`, `order_id`) VALUES ({}, 'A', 0.10001000, 0.30001000, 1);""".format(period_id)
create_range_sql2 = """INSERT INTO pg_betting_price_range (`period_id`, `group_name`, `begin_range`, `end_range`, `order_id`) VALUES ({}, 'B', 0.30002000, 0.40001000, 2);""".format(period_id)
create_range_sql3 = """INSERT INTO pg_betting_price_range (`period_id`, `group_name`, `begin_range`, `end_range`, `order_id`) VALUES ({}, 'C', 0.40002000, 0.50001000, 3);""".format(period_id)
create_range_sql4 = """INSERT INTO pg_betting_price_range (`period_id`, `group_name`, `begin_range`, `end_range`, `order_id`) VALUES ({}, 'D', 0.50002000, 0.60001000, 4);""".format(period_id)
create_range_sql5 = """INSERT INTO pg_betting_price_range (`period_id`, `group_name`, `begin_range`, `end_range`, `order_id`) VALUES ({}, 'E', 0.60002000, 0.80001000, 5);""".format(period_id)
create_range_list = [create_range_sql1, create_range_sql2, create_range_sql3, create_range_sql4, create_range_sql5]
for create_range in create_range_list:
    connect_mysql().connect2mysql(create_range)
print("数据添加成功")