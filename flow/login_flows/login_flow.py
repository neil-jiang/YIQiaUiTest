# -*- coding: utf-8 -*-# 
# ------------------------------------------------------
# @Time :      2021/1/14 10:57 
# @Author :    Neil.Jiang
# @project:    YiQiaUiTest
# @File :      login_flow.py
# @Email :     jiang.nell@qq.com
# @Description: 
# @命名规范：文件名全小写+下划线，类名大写字母开头，方法和变量小写+下划线连接，常量大写

# -------------------------------------------------------
from page.services_pages.login_page import LoginPage
from base.config import CompanyConfig
import time
from base.base import my_log
import os


class LoginFlow(LoginPage):

    def __init__(self, url, browser):
        super().__init__(url=url, browser=browser)

    def login_flow(self, username, password, company):
        """

        :param username:登录的用户名
        :param password: 登录密码
        :param company: 登录的公司
        :return:
        """
        self.locate_username().send_keys(username)
        self.locate_password().send_keys(password)
        self.locate_submit().click()
        my_log().info("进入公司选择页面")

        try:
            self.locate_search_box().send_keys(company)
        except:

            self.screen_shot(os.getcwd().split("YiQiaUiTest")[0] +
                             r"YiQiaUiTest\data\error_img\login_img\登录失败%s.png" % time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
            errro_img = os.getcwd().split("YiQiaUiTest")[0] + r"YiQiaUiTest\data\error_img\login_img\登录失败%s.png" % time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
            my_log().error("输入公司失败,已添加截图:%s" % errro_img)
            return errro_img
        self.driver.execute_script("arguments[0].click();", self.locate_company())


if __name__ == '__main__':
    # print(time.localtime())
    # print(os.getcwd().split("YiQiaUiTest")[0])
    # print(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
    url , browser = CompanyConfig.online_521889_bf()[0:2]

    loginflow = LoginFlow(url, browser)
    loginflow.login_flow(username="1377811995041", password="199566", company="2151")


