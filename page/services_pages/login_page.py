# -*- coding: utf-8 -*-# 
# ------------------------------------------------------
# @Time :      2021/1/14 10:38 
# @Author :    Neil.Jiang
# @project:    YiQiaUiTest
# @File :      login_page.py
# @Email :     jiang.nell@qq.com
# @Description: 
# @命名规范：文件名全小写+下划线，类名大写字母开头，方法和变量小写+下划线连接，常量大写

# -------------------------------------------------------
from base.base import Base
import os


class LoginPage(Base):
    def __init__(self, url, browser="chrome"):
        super().__init__(url=url, browser=browser)

    def locate_username(self):
        return self.find_ele(ele_type="id", ele='username')

    def locate_password(self):
        return self.find_ele(ele_type="id", ele="password")

    def locate_submit(self):
        return self.find_ele(ele_type="class", ele="login-btn")

    def locate_search_box(self, wait_time=10):
        return self.find_ele(ele_type="xpath", ele='//*[@id="account-search-box"]/input', timeout=wait_time)

    def locate_company(self):
        return self.find_ele(ele_type="class", ele="logo-img")


if __name__ == '__main__':
    url = "http://e.echatsoft.com/login-page/v2/login.html?language=zh"
    page = LoginPage(url,browser="firefox")
    page.locate_username().send_keys("13778995041")
    page.locate_password().send_keys("199566")
    page.locate_submit().click()
    page.locate_search_box().send_keys("521889")
    page.driver.execute_script("arguments[0].click();", page.locate_company())



