# coding:utf-8
# @author : csl
# @date   : 2018/08/17 10:12
"""后台管理"""

from common.request2DKApi import request2DKApi
from common.base import DKApiBase

class reqApi_admin_1_0(object):

    """1.1 锁仓大活动"""
    def admin_activitieProject_page_query(self):
        """
        1.1.1 分页查询
        :return: 
        """
        server = "admin/activitieProject/page-query"
        data = {"pageNo":"1",
                "pageSize":"10"}
        r = request2DKApi(server, data).send()
        print(r)

    # 1.1.2 添加锁仓活动配置（admin/activitieProject/create）
    # 1.1.3 修改活动（admin/activitieProject/update）

    def admin_activitieProject_detail(self):
        """
        1.1.4 某个活动详情
        :return: 
        """
        server = "admin/activitieProject/detail"
        data = {"id":"35"}
        r = request2DKApi(server, data).send()
        print(r)

    def admin_activitieProject_list(self):
        """
        1.1.5 获取所有未生效的活动
        :return: 
        """
        server = "admin/activitieProject/list"
        data = {"type":"3"}
        r = request2DKApi(server, data).send()
        print(r)

    def admin_lockCoinActivitie_page_query(self):
        """
        1.2 锁仓活动配置
        1.2.1 分页查询
        :return: 
        """
        server = "admin/lockCoinActivitie/page-query"
        data = {"pageNo":"1",
                "pageSize":"10"}
        r = request2DKApi(server, data).send()
        print(r)

    # 1.2.2 添加锁仓活动配置（admin/lockCoinActivitie/create）
    # 1.2.3 修改锁仓充值（admin/lockCoinActivitie/update）

    def admin_lockCoinActivitie_detail(self):
        """
        1.2.4详情
        :return: 
        """
        server = "admin/lockCoinActivitie/detail"
        data = {"id":"49"}
        r = request2DKApi(server, data).send()
        print(r)

    def admin_lockCoinActivitie_coinPrice(self):
        """
        1.2.5 获取币种价格
        :return: 
        """
        server = "admin/lockCoinActivitie/coinPrice"
        data = {"unit":"SLB"}
        r = request2DKApi(server, data).send()
        print(r)

    def admin_lockCoinRecharge_page_query(self):
        """
        1.3 锁仓充值配置
        1.3.1 分页查询
        :return: 
        """
        server = "admin/lockCoinRecharge/page-query"
        data = {"pageNo":"1",
                "pageSize":"10"}
        r = request2DKApi(server, data).send()
        print(r)

    def admin_lockCoinRecharge_list(self):
        """
        1.3.2 锁仓配置信息列表查询
        :return: 
        """
        server = "admin/lockCoinRecharge/list"
        data = {}
        r = request2DKApi(server, data).send()
        print(r)


    # 1.3.3 添加锁仓充值（admin/lockCoinRecharge/create）
    # 1.3.4 修改锁仓充值（admin/lockCoinRecharge/update）

    def admin_lockCoinRecharge_detail(self):
        """
        1.3.5 详情
        :return: 
        """
        server = "admin/lockCoinRecharge/detail"
        data = {"id":"47"}
        r = request2DKApi(server, data).send()
        print(r)

    def admin_lockDetail_page_query(self):
        """
        1.4 锁仓
        1.4.1 锁仓分页查询
        :return: 
        """
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

    def admin_member_member_application_pass(self):
        """
        4.1.6 实名审核系统审核人工确认
        :return: 
        """
        id = "2182"
        server = "admin/member/member-application/{}/pass".format(id)
        data = {}
        r = request2DKApi(server, data).send("PATCH")


if __name__ == "__main__":
    reqApi_admin_1_0().admin_lockDetail_page_query()