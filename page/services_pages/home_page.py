# -*- coding: utf-8 -*-# 
# ------------------------------------------------------
# @Time :      2021/1/14 15:11 
# @Author :    Neil.Jiang
# @project:    YiQiaUiTest
# @File :      home_page.py
# @Email :     jiang.nell@qq.com
# @Description: 
# @命名规范：文件名全小写+下划线，类名大写字母开头，方法和变量小写+下划线连接，常量大写

# -------------------------------------------------------
from login_flows.login_flow import LoginFlow
from config import CompanyConfig


class MenuBar(LoginFlow):
    def __init__(self, url,browser,username, password, company,):
        """
        :param url:登录的url
        :param username: 登录用户名
        :param password: 登录密码
        :param company: 登录公司id
        """
        super().__init__(url,browser)
        self.login_flow(username=username,password=password,company=company)

    def locate_chat(self):
        """
        定位对话标签
        :return:
        """
        return self.find_ele("class", "icon_chat")

    def locate_leave(self):
        """
        定位留言标签
        :return:
        """
        return self.find_ele("class", "icon_leave")

    def locate_monitor(self):
        """
        定位监控标签
        :return:
        """
        return self.find_ele("class", "icon_colle")

    def locate_record(self):
        """
        定位记录标签
        :return:
        """
        return self.find_ele("class", "icon_history")

    def locate_workorder(self):
        """
        定位工单标签
        :return:
        """
        return self.find_ele("class", "icon_workorder")

    def locate_custom(self):
        """
        定位客户标签
        :return:
        """
        return self.find_ele("class", "icon_booking")

    def locate_report(self):
        """
        定位报表标签
        :return:
        """
        return self.find_ele("class", "icon_analyze")

    def locate_share(self):
        """
        定位分享标签
        :return:
        """
        return self.find_ele("class", "icon_share")

    def locate_log(self):
        """
        定位日志标签
        :return:
        """
        return self.find_ele("class", "icon_log")

    def locate_service_internal_photo(self):
        """
        定位客服对内头像
        :return:
        """
        return self.find_ele("css", "div.header_logo > img")


if __name__ == '__main__':
    url ,browser,username, password,company = CompanyConfig().online_521889()

    home_page = MenuBar(url ,browser,username, password,company)
    print(home_page.locate_chat().click())
    print(home_page.locate_leave().click())
    print(home_page.locate_record().click())
    print(home_page.locate_report().click())
    print(home_page.locate_monitor().click())
    print(home_page.locate_share().click())
    print(home_page.locate_workorder().click())
    print(home_page.locate_log().click())
    home_page.open_new_handle("https://chats.rainbowred.com/visitor/pc/chat.html?companyId=1712&echatTag=jzh")

