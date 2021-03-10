# -*- coding: utf-8 -*-# 
# ------------------------------------------------------
# @Time :      2021/3/8 18:11 
# @Author :    Neil.Jiang
# @project:    YiQiaUiTest
# @File :      test_robot_flows.py
# @Email :     jiang.nell@qq.com
# @Description: 
# @命名规范：文件名全小写+下划线，类名大写字母开头，方法和变量小写+下划线连接，常量大写

# -------------------------------------------------------

from flow.chat_flows.basic_chat_flows import BasChatFlows
from parameterized.parameterized import parameterized
import unittest
from base.config import CompanyConfig
from base.config import VisConfig
from base.config import CommonVariable
from unittest import TestCase
import time
import warnings
import os
from base.base import OpExcel
from base.base import OpPicture


class TestRobotFlows(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        url, browser, username, password, company, v_url, v_browser = CompanyConfig().online_524328() + VisConfig().online_524328(type='jq')
        cls.flow = BasChatFlows(url, browser, username, password, company, v_url, v_browser, )
        cls.s_driver = cls.flow.s_driver
        cls.v_driver = cls.flow.v_driver

    @classmethod
    def tearDownClass(cls) -> None:
        # pass
        cls.s_driver.kill_driver()
        cls.v_driver.kill_driver()

    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self) -> None:
        self.s_driver.driver_refresh()
        self.v_driver.driver_refresh()

    @parameterized.expand( OpExcel(r'D:\YiQiaUiTest\data\test_case\chat_test_cases.xlsx').get_excel_data('一洽_对话测试用例',
                                                                                                         [26],
                                                                                                         columns=[3],
                                                                                                         json_columns=[
                                                                                                             5]))
    def test_fqa(self,case_name,s_msg,v_msg,fqa,fqa_list_text,fqa_prompt_text,welcome_prompt_text):
        """
        :return:
        """
        try:
            fqa_list, fqa_prompt, welcome_prompt = self.v_driver.lcoate_robot_welcome(fqa=fqa)
            assert fqa_list[0].text == fqa_list_text
            assert fqa_prompt.text == fqa_prompt_text
            assert welcome_prompt.count(welcome_prompt_text)==1 == welcome_prompt_text
        except AssertionError:
            file_name = "../../data/error_img/chat_img/访客端%s失败_%s.png" % \
                          (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
            self.s_driver.driver.save_screenshot(filename=file_name)
            raise AssertionError

    def test_input_text(self,case_name,prompt):
        try:
            assert self.v_driver.locate_input_box_prompt().get_attribute('placeholder') == prompt
        except AssertionError:
            file_name = "../../data/error_img/chat_img/访客端%s失败_%s.png" % \
                          (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
            self.s_driver.driver.save_screenshot(filename=file_name)
            raise AssertionError

    def test_unidentifiedQ_Manual_to_manual(self,case_name,v_msg,humanbutton,humantip):
        """
        验证访客发送n条问题机器人为识别答案能弹出转人工按钮
        :param case_name:
        :param v_msg:
        :param humanbutton:
        :param humantip:
        :return:
        """
        for each_msg in v_msg:
            self.flow.send_text_msg(s_msg='',v_msg=each_msg)
        try:
            assert self.v_driver.locate_tohumanbutton().text == humanbutton
            assert self.v_driver.locate_tohumantip().text == humantip
        except AssertionError:
            file_name = "../../data/error_img/chat_img/访客端%s失败_%s.png" % \
                        (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
            self.s_driver.driver.save_screenshot(filename=file_name)
            raise AssertionError

    # def test_unsolvedQ__Manual_to_manual(self):







if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestRobotFlows('test_fqa'))
    runner = unittest.TextTestRunner(suit())

