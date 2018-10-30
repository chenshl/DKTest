# coding:utf-8
# @author : csl
# @date   : 2018/10/24 15:43

from common.base_connect_mysql import connect_mysql
from common.writelog_up import WriteLogger


logger = WriteLogger().getLogger()

class batch_register(object):
    """
    @description: 测试环境批量注册用户
    测试账号盐值、密码可传相同数值；推荐码为“U”+member表主键ID+两位随机字符或数字
    """
    # 开始写入前查询member表中已经注册过的测试手机号最大数值和memberID，注：默认批量添加过程中不被别人插入数据
    sql_select_registerd_test_phone = "SELECT mobile_phone FROM member WHERE mobile_phone LIKE '17700%' ORDER BY mobile_phone DESC LIMIT 1;"
    sql_select_registerd_test_memberID = "SELECT id FROM member ORDER BY id DESC LIMIT 1;"
    registerd_test_phone = connect_mysql().connect2mysql(sql_select_registerd_test_phone)[0][0]  # 手机号
    registerd_test_memberID = connect_mysql().connect2mysql(sql_select_registerd_test_memberID)[0][0]  # memberID
    print("起始手机号：{}--起始memberID：{}".format(registerd_test_phone, registerd_test_memberID))
    defualt_password = "fabd9d2d960bd3642704d65c66231db7"  # 默认密码cs111111
    defualt_salt = "3836313237363938373730303036303136"  # 默认盐值
    defualt_coin_id = ["BCH", "Bitcoin", "BTMC", "CALL", "CNYT", "DARING5920", "Dogecoin", "EOS", "ETC", "Ethereum", "Litecoin", "mmb", "NB", "Silubium", "SLU", "SOG"]

    # 写入member表用户数据
    def insert_member_and_memberwallet(self):
        """
        @description: 写入member表及memberwallet表用户数据
        :return: 
        """

        for index in range(1, 10001):

            try:
                # 注册手机号
                mobile_phone = str(int(self.registerd_test_phone) + index)
                # 注册推荐码
                promotion_code = "U" + str(int(self.registerd_test_memberID) + index) + "AT"
                # 用户memberID
                member_id = int(self.registerd_test_memberID) + index

                sql_insert_member = """INSERT INTO member (appeal_success_times, appeal_times, certified_business_status, first_level, country, login_count, member_level, mobile_phone, 
                `password`, promotion_code, real_name_status, registration_time, salt, second_level, `status`, third_level, transactions, username, `local`, google_state, publish_advertise, 
                transaction_status, sign_in_ability, ip) 
                VALUES 
                (0, 0, 0, 0, '中国', 0, 0, {}, '{}', '{}', 0, '2018-10-24 15:57:00', {}, 
                0, 0, 0, 0, {}, '中国', 0, 1, 1, 1, '172.16.1.74');""".format(mobile_phone, self.defualt_password, promotion_code, self.defualt_salt, mobile_phone)
                connect_mysql().connect2mysql(sql_insert_member)
                logger.info("写入member表成功：{}".format(mobile_phone))
                print("写入member表成功：{}".format(mobile_phone))

                for coin_id in self.defualt_coin_id:
                    sql_insert_memberwallet = """INSERT INTO member_wallet (balance, frozen_balance, member_id, version, coin_id, is_lock, lock_balance, enabled_in, enabled_out) 
                    VALUES 
                    (0.00000000, 0.00000000, {}, 0, '{}', 0, 0.00000000, 1, 1);""".format(member_id, coin_id)
                    connect_mysql().connect2mysql(sql_insert_memberwallet)
                    logger.info("写入member_wallet表成功：{}-{}".format(member_id, coin_id))
                    print("写入member_wallet表成功：{}-{}".format(member_id, coin_id))
            except Exception as e:
                logger.error("写入数据库错误：{}".format(e))
                print("写入数据库错误：{}".format(e))
                break





if __name__ == "__main__":
    batch_register().insert_member_and_memberwallet()