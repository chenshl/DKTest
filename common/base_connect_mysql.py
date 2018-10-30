# coding:utf-8
# @author : csl
# @date   : 2018/07/26 09:03
# 数据库查询封装

import pymysql

class connect_mysql():

    def __init__(self):

        # 连接数据库
        try:
            # 测试库
            self.connect = pymysql.Connect(
                host='172.16.0.66',
                port=3306,
                user='***',
                passwd='***',
                db='***',
                charset='utf8'
            )


        except Exception as e:
            print("连接数据库失败", e)

    # 连接操作
    def connect2mysql(self, complySql):

        try:
            # 获取游标
            self.cursor = self.connect.cursor()
            self.cursor.execute(complySql)
        except Exception as e:
            self.connect.rollback()
            print("数据库事务处理失败。。。", e)
        else:
            self.connect.commit()
            self.mysql_result = self.cursor.fetchall()
            # print("执行SQL：{}".format(complySql))
            # print("数据库事务处理成功。。。")

            return self.mysql_result
        finally:
            # 关闭游标，关闭连接
            self.cursor.close()
            self.connect.close()

if __name__ == "__main__":
    sql = '''SELECT id FROM member ORDER BY id DESC LIMIT 1;
    '''
    result = connect_mysql().connect2mysql(sql)
    print(type(result))
    print(result)
    print(len(result))
    print(result[0][0])
    print(int(result[0][0]) + 10)

    # print(type(result))