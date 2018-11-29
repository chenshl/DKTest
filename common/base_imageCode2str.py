# coding:utf-8
# @author : csl
# @date   : 2018/11/28 17:33
# 需安装tesseract-ocr

import requests
import os
import pytesseract
from PIL import Image

class imageCode2str(object):
    """图片二维码转换为str"""

    def __init__(self, url):
        self.url = url

        # 设置错误字符修正
        self.correctStr = {"}":"j",
                           "\\":"l",
                           ")":"l",
                           "&":"4",
                           "(":"l",
                           "[":"l",
                           "{":"i"}

    def saveImage(self,):
        """
        @description: 保存图片
        :param url: 
        :return: 
        """
        # 获取文件路径
        PATH = os.path.abspath(os.path.join(os.path.dirname('.'), os.path.pardir))
        self.imagePATH = str(PATH) + '\\datas\\imageCode\\captcha.png'  # 拼接日志目录
        if "DKTest" not in self.imagePATH:
            self.imagePATH = str(PATH) + "\\DKTest\\datas\\imageCode\\captcha.png"

        # 保存图片
        reqimage = requests.get(self.url)
        f_image = open(self.imagePATH, "wb")
        f_image.write(reqimage.content)
        f_image.close()

    def image2str(self):
        """图片二维码提取"""
        self.saveImage()
        image = Image.open(self.imagePATH)
        vcode = pytesseract.image_to_string(image).replace(" ", "")  # 获得字符串并去除空格

        for errorStr in self.correctStr:
            if errorStr in vcode:
                vcodeStr = vcode.replace(errorStr, self.correctStr[errorStr])
                return vcodeStr

        return vcode



if __name__ == "__main__":
    r = imageCode2str("http://?cid=ADMIN_LOGIN").image2str()
    print(r)