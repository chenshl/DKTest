# coding:utf-8
# @author : csl
# @date   : 2018/10/30 11:19
# 调用接口处理线上未退还成功数据

import requests
import time

for id in range(1232, 1258):
    print(id)
    r = requests.get("https://api.silktrader.net/market/redo?id={}".format(id))
    time.sleep(0.1)
    print(r.text)
print("处理完成")