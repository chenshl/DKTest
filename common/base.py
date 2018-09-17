# coding:utf-8
# @author : csl
# @date   : 2018/07/24 14:30
"""
基础方法封装
"""

import time
import hashlib
import json

class DKApiBase(object):

    # 指定时间转换为毫秒时间戳,返回str tdtime="2018-05-29 10:22:22"
    def time2Timestamps(self, tdtime):
        self.timeArray = time.strptime(tdtime, "%Y-%m-%d %H:%M:%S")
        self.stime = int(round(time.mktime(self.timeArray) * 1000))
        return str(self.stime)

    # 当前时间转换为毫秒时间戳，返回str
    def nowtime2Timestamps(self):
        self.stime = int(round(time.time() * 1000))
        return str(self.stime)

    # 参数拼接
    def data2str(self, data):
        self.params = copy.deepcopy(data)  # 深度拷贝data
        self.paramslist = sorted(self.params.items())  # 按照params的key值排序
        self.datastr = ""
        for i in self.paramslist:
            self.datastr += i[0] + "=" + i[1] + "&"
        return self.datastr.rstrip("&")  # 删除末尾"&"
        # return self.datastr

    # MD5签名串
    def getSign(self, str):
        self.paramsignstr = str
        m = hashlib.md5()  # 生成一个md5 hash对象
        m.update(self.paramsignstr.encode('utf-8'))  # 生成hash对象后，用update方法对字符串进行md5加密的更新处理
        self.md5str = m.hexdigest()  # 16进制的加密结果字符串
        return self.md5str

    # 将字符串转换为json格式
    def str2json(self, str):
        str2json = json.loads(str)
        return str2json

    # 格式化mysql查询结果,将元组转换为字典格式
    def mysqlResultFormat(self, data=((),), parameter_name=[]):
        result = []
        if isinstance(data, tuple) and data:  # 判断data是一个元组并且不为空
            for tuple_data in data:
                if isinstance(tuple_data, tuple) and tuple_data:  # 判断元组中的参数不为空
                    chid_result = {}
                    if len(tuple_data) == len(parameter_name):
                        if isinstance(parameter_name, list) and parameter_name:  # 判断parameter_name是一个列表并且不为空
                            for i in range(len(parameter_name)):
                                chid_result[parameter_name[i]] = tuple_data[i]
                        else:
                            print("{}为空".format(parameter_name))
                            break
                        result.append(chid_result)
                    else:
                        print("{}和{}的参数长度不一致，请核对后传入！！！".format(tuple_data, parameter_name))
                        break
                else:
                    print("{}中有为空的参数".format(data))
                    break
        else:
            print("{}为空或者不为一个元组，请核对后传入！！！".format(data))

        return result







# if __name__ == "__main__":
#     print(DKApiBase().mysqlResultFormat())
#     jsonstr = DKApiBase().str2json('{"code":0,"message":"success","data":null}')
#     print(type(jsonstr), jsonstr)
#     str = '''{
#           "code" : 0,
#           "message" : "SUCCESS",
#           "data" : [ {
#             "id" : 107,
#             "advertiseType" : 1,
#             "minLimit" : 100.00,
#             "maxLimit" : 1000.00,
#             "status" : 1,
#             "remainAmount" : 10000.00000000,
#             "coinUnit" : "USDT",
#             "price" : 6.82,
#             "createTime" : "2018-08-02 14:02:08",
#             "country" : {
#               "zhName" : "中国",
#               "enName" : "China",
#               "areaCode" : "86",
#               "language" : "zh_CN",
#               "localCurrency" : "CNY",
#               "sort" : 0
#             },
#             "priceType" : 0,
#             "premiseRate" : "null"
#           } ]
#         }'''
#     jsonstr = DKApiBase().str2json(str)
#     print(jsonstr["data"][0]["id"])
