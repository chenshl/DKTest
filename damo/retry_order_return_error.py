# coding:utf-8
# 调用接口处理线上未退还成功数据

import requests
import time

for id in range(1035, 1135):
    print(id)
    r = requests.get("https://api.silktrader.net/market/redo?id={}".format(id))
    time.sleep(2)
    print(r.text)
print("处理完成")