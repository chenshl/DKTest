# coding:utf-8
# @author : csl
# @date   : 2018/08/17 10:12
"""后台管理"""

from common.request2DKApi import request2DKApi
from common.base import DKApiBase

"""1 activitie"""
"""1.1 锁仓大活动"""
# 1.1.1 分页查询
# server = "admin/activitieProject/page-query"
# data = {"pageNo":"1",
#         "pageSize":"10"}

# 1.1.2 添加锁仓活动配置（admin/activitieProject/create）
# 1.1.3 修改活动（admin/activitieProject/update）

# 1.1.4 某个活动详情
# server = "admin/activitieProject/detail"
# data = {"id":"35"}

# 1.1.5 获取所有未生效的活动
# server = "admin/activitieProject/list"
# data = {"type":"3"}

"""1.2 锁仓活动配置"""
# 1.2.1 分页查询
# server = "admin/lockCoinActivitie/page-query"
# data = {"pageNo":"1",
#         "pageSize":"10"}

# 1.2.2 添加锁仓活动配置（admin/lockCoinActivitie/create）
# 1.2.3 修改锁仓充值（admin/lockCoinActivitie/update）

# 1.2.4详情
# server = "admin/lockCoinActivitie/detail"
# data = {"id":"49"}

# 1.2.5 获取币种价格
# server = "admin/lockCoinActivitie/coinPrice"
# data = {"unit":"SLB"}

"""1.3 锁仓充值配置"""
# 1.3.1 分页查询
# server = "admin/lockCoinRecharge/page-query"
# data = {"pageNo":"1",
#         "pageSize":"10"}

# 1.3.2 锁仓配置信息列表查询
# server = "admin/lockCoinRecharge/list"
# data = {}

# 1.3.3 添加锁仓充值（admin/lockCoinRecharge/create）
# 1.3.4 修改锁仓充值（admin/lockCoinRecharge/update）

# 1.3.5 详情
# server = "admin/lockCoinRecharge/detail"
# data = {"id":"47"}

"""1.4 锁仓"""
# 1.4.1 锁仓分页查询
server = "admin/lockDetail/page-query"
data = {"endTime":"",
        "startTime":"",
        "status":"1",  # LOCKED("已锁定"),//0 UNLOCKED("已解锁"), //1 CANCLE("已撤销");//2
        "coinUnit":"",
        "userName":"",
        "pageNo":"1",
        "pageSize":"10"}



r = request2DKApi(server, data).send()
print(r)