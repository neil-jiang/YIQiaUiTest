# -*- coding: utf-8 -*-# 
# ------------------------------------------------------
# @Time :      2021/3/1 17:41 
# @Author :    Neil.Jiang
# @project:    YiQiaUiTest
# @File :      test2.py
# @Email :     jiang.nell@qq.com
# @Description: 
# @命名规范：文件名全小写+下划线，类名大写字母开头，方法和变量小写+下划线连接，常量大写

# -------------------------------------------------------
from base.config import CompanyConfig
from base.config import VisConfig
import os
from selenium import webdriver
import json
import openpyxl
from base.base import OpExcel
from PIL import Image
import requests
import time
from  base.base import OpMail

if __name__ == '__main__':
    sender = "627359686@qq.com"
    receiver = ["952618746@qq.com"]
    subject = "Basic_chat_flows"
    while True:
        text = "dasdsadsa测试发邮件现在时间是：%s" % time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())
        print(text)
        myemail = OpMail(smtp_user="627359686@qq.com", smtp_password="lcioruzvrwxbbfhi")
        myemail.set_base_info(sender=sender, receiver=receiver, subject=subject, text=text)
        myemail.add_attr('D:\YiQiaUiTest\data\screenshot_img\chat_img\访客端访客目标图片截图_2021_02_19_17_51_28.png')
        myemail.send_eail(receiver=receiver)
        time.sleep(2)