# -*- coding: utf-8 -*-# 
# ------------------------------------------------------
# @Time :      2021/3/9 16:12 
# @Author :    Neil.Jiang
# @project:    YiQiaUiTest
# @File :      robot_chat_flows.py
# @Email :     jiang.nell@qq.com
# @Description: 
# @命名规范：文件名全小写+下划线，类名大写字母开头，方法和变量小写+下划线连接，常量大写

# -------------------------------------------------------
from page.visitor_pages.pc_webpage import PcWebPage
from page.services_pages.chat_pages.chat_center_page import ChatCenterPage
from base.config import CompanyConfig
from base.config import VisConfig
import time

class RobotChatFlows:
    def __init__(self,url, browser, username, password, company,v_url,v_browser):
        self.s_driver = ChatCenterPage(url, browser, username, password, company)
        # 这一步的目的是定位到客服界面加载完成
        self.s_driver.locate_report()
        self.v_driver = PcWebPage(url=v_url,browser=v_browser)

    def confirm_question_solved(self,v_msg,confirm,number):
        """
        访客点击问题是否被解决
        :param v_msg: 访客消息
        :param confirm: confirm为真点击是，为假点击否
        :param number: 第几组确定按钮
        :return:
        """
        if v_msg:
            self.v_driver.locate_input_box_prompt().click()
            self.v_driver.locate_input_box_prompt().send_keys(v_msg)
            self.v_driver.locate_send_button().click()
        time.sleep(2)
        ele = self.v_driver.locate_confirm_question_solved_button(choice=confirm)
        ele[number-1].click()

    def select_question(self,v_msg,timeout,answer_num,serial):
        if v_msg:
            self.v_driver.locate_input_box_prompt().click()
            self.v_driver.locate_input_box_prompt().send_keys(v_msg)
            self.v_driver.locate_send_button().click()
        self.v_driver.locate_question_list(timeout=timeout)[answer_num-1][1][serial-1].click()


if __name__ == '__main__':
    service = CompanyConfig.online_524328()
    vis = VisConfig.online_524328(echatTag='jq')
    chat_flow = RobotChatFlows(*service, *vis)
    chat_flow.confirm_question_solved(v_msg='你是四川人吗',confirm=True,number=1)
    chat_flow.select_question(v_msg='你是四川人吗',timeout=11,answer_num=1,serial=2)
