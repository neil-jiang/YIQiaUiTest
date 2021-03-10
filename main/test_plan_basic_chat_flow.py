# -*- coding: utf-8 -*-# 
# ------------------------------------------------------
# @Time :      2021/1/29 17:55 
# @Author :    Neil.Jiang
# @project:    YiQiaUiTest
# @File :      test_plan_basic_chat_flow.py
# @Email :     jiang.nell@qq.com
# @Description: 
# @命名规范：文件名全小写+下划线，类名大写字母开头，方法和变量小写+下划线连接，常量大写

# -------------------------------------------------------
from BeautifulReport.BeautifulReport import BeautifulReport
from test_flow.test_chat_flows.test_basic_chat_flows import TestBasicChatFlows
import os
import unittest
import time
from base.base import OpMail

def run(html_name, description, sender, receiver, subject,text):
    filename="%s_%s.html" % (html_name, time.strftime("%Y_%m_%d_%H_%M"))
    report_dir = os.path.split(os.getcwd())[0]+r"\data\report\\"
    suit = unittest.TestLoader().loadTestsFromTestCase(TestBasicChatFlows)
    BeautifulReport(suit).report(
                                 filename=filename,
                                 report_dir=report_dir,
                                 description=description)
    myemail = OpMail()
    myemail.set_base_info(sender=sender, receiver=receiver, subject=subject, text=text)
    print(report_dir+os.sep+filename)
    myemail.add_attr(report_dir+os.sep+filename)
    myemail.send_eail(receiver=receiver)


if __name__ == '__main__':
    os.chdir(r'D:\YiQiaUiTest\test_flow\test_chat_flows\\')
    run(html_name="Basic_chat_flows_report", description="Basic_chat_flows",
        sender="952618746@qq.com", receiver=["627359686@qq.com","jiang.neil@qq.com"],
        subject="Basic_chat_flows", text="Basic_chat_flowsT第一轮测试")