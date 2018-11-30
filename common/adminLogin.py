# coding:utf-8
# @author : csl
# @date   : 2018/11/30 16:52

import requests
import os
from common.base_imageCode2str import imageCode2str

reqsession = requests.Session()

class adminLogin(object):
    """管理后台登录"""

    # 获取图片验证码地址
    codeurl = ""
    # 验证图片验证码地址
    checkurl = ""
    # 验证手机验证码地址
    loginurl = ""

    def adminLogin(self):
        """
        @descreption: 后台登录接口
        :return: 登录后的requests.sessions.Session object类
        """
        # 获取二维码
        PATH = os.path.abspath(os.path.join(os.path.dirname('.'), os.path.pardir))
        imagePATH = str(PATH) + '\\datas\\imageCode\\captcha.png'  # 拼接日志目录
        if "DKTest" not in imagePATH:
            imagePATH = str(PATH) + "\\DKTest\\datas\\imageCode\\captcha.png"

        while True:
            # 保存图片
            reqimage = reqsession.get(self.codeurl)
            f_image = open(imagePATH, "wb")
            f_image.write(reqimage.content)
            f_image.close()

            # 二维码返回str
            code = imageCode2str().image2str()

            data = {"username": "root",
                    "password": "roots",
                    "captcha": code}
            r = reqsession.post(self.checkurl, data)
            if "验证码不正确" in r.text:
                continue
            elif "SUCCESS" in r.text:
                break

        # 验证手机码
        logindata = {"code": "a"}
        reqsession.post(self.loginurl, logindata)

        return reqsession




if __name__ == "__main__":
    rrr = adminLogin().adminLogin()
    print(5,rrr)