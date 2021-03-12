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

from flow.chat_flows.robot_chat_flows import RobotChatFlows
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
        url, browser, username, password, company, v_url, v_browser = CompanyConfig().online_524328() + VisConfig().online_524328(echatTag='jq')
        cls.flow = RobotChatFlows(url, browser, username, password, company, v_url, v_browser, )
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
                                                                                                         [51],
                                                                                                         columns=[3],
                                                                                                         json_columns=[
                                                                                                             5]))
    def test_fqa(self,case_name,fqa,fqa_list_text,fqa_prompt_text,welcome_prompt_text):
        self.__dict__['_testMethodDoc'] = case_name
        """

        :param case_name: 用例名称
        :param fqa: fqa为真返回常见问题列表和常见问题提示 ，否则只返回欢迎语
        :param fqa_list_text: 常见问题文本
        :param fqa_prompt_text: 常见问题提示语文本
        :param welcome_prompt_text: 机器人欢迎语
        :return:
        """
        try:
            fqa_list, fqa_prompt, welcome_prompt = self.v_driver.lcoate_robot_welcome(fqa=fqa)
            assert fqa_list[0].text == fqa_list_text
            assert fqa_prompt.text == fqa_prompt_text
            assert welcome_prompt.text.count(welcome_prompt_text) == 1
        except AssertionError:
            file_name = "../../data/error_img/chat_img/访客端%s失败_%s.png" % \
                          (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
            self.s_driver.driver.save_screenshot(filename=file_name)
            raise AssertionError

    def test_input_text(self,case_name,prompt):
        self.__dict__['_testMethodDoc'] = case_name
        """
        验证输入框文本是否正确
        :param case_name:用例名
        :param prompt:输入框提示语
        :return:
        """
        try:
            assert self.v_driver.locate_input_box_prompt().get_attribute('placeholder') == prompt
        except AssertionError:
            file_name = "../../data/error_img/chat_img/访客端%s失败_%s.png" % \
                          (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
            self.s_driver.driver.save_screenshot(filename=file_name)
            raise AssertionError

    @parameterized.expand( OpExcel(r'D:\YiQiaUiTest\data\test_case\chat_test_cases.xlsx').get_excel_data('一洽_对话测试用例',
                                                                                                         [69,72,70,71,73,74,75],
                                                                                                         columns=[3],
                                                                                                         json_columns=[
                                                                                                             5]))
    def test_robot_to_manual(self,case_name,tomanual_type,v_msg,sleep_time,humanbutton,humantip,greet_jq,
                                            greet_manual):
        self.__dict__['_testMethodDoc'] = case_name
        """
        验证访客能手动触发转人工
        :param case_name:用例名字
        :param tomanual_type:手动转人工类型 1：发送消息手动转人工，2:点击未解决手动转人工,3.发送包含转人工提示语手动转人工
                                        4:发消息自动转人工，5:点击未解决自动转人工，6：发送转人工关键字自动转人工
                                        7：点击转人工按钮转人工,
        :param v_msg:访客发送的消息列表
        :param sleep_time:访客发送消息后的睡眠时间
        :param humanbutton:转人工按钮
        :param humantip:转人工提示
        :param greet_jq:转人工时机器人的欢迎语
        :param greet_manual:人工的欢迎语
        :return:
        """
        if tomanual_type in (1,3,4,6,7):
            for each_msg in v_msg:
                print(each_msg)
                self.flow.send_msg_to_robot(v_msg=each_msg)
        if tomanual_type in (2,5):
            count = 1  # 记录是第几组“是”“否”按钮
            for each_vmsg in v_msg:
                print(each_vmsg)
                self.flow.confirm_question_solved(v_msg=each_vmsg, confirm=False, sleep_time=sleep_time,
                                                  number=count)
                count += 1
        if tomanual_type in (1,2,3):
            try:
                assert self.v_driver.locate_tohumanbutton().text == humanbutton
                assert self.v_driver.locate_tohumantip().text == humantip
            except AssertionError:
                file_name = "../../data/error_img/chat_img/访客端%s失败_%s.png" % \
                            (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
                self.s_driver.driver.save_screenshot(filename=file_name)
                raise AssertionError
        if tomanual_type in (4,5,6):
            try:
                assert self.v_driver.locate_greeting()[0].text == greet_jq
                assert self.v_driver.locate_greeting()[1].text == greet_manual
            except AssertionError:
                file_name = "../../data/error_img/chat_img/访客端%s失败_%s.png" % \
                            (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
                self.s_driver.driver.save_screenshot(filename=file_name)
                raise AssertionError
        if tomanual_type == 7:
            try:
                self.v_driver.locate_tohumanbutton().click()
                assert self.v_driver.locate_greeting()[0].text == greet_manual
            except AssertionError:
                file_name = "../../data/error_img/chat_img/访客端%s失败_%s.png" % \
                            (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
                self.s_driver.driver.save_screenshot(filename=file_name)

    @parameterized.expand( OpExcel(r'D:\YiQiaUiTest\data\test_case\chat_test_cases.xlsx').get_excel_data('一洽_对话测试用例',
                                                                                                         [76,77],
                                                                                                         columns=[3],
                                                                                                         json_columns=[
                                                                                                             5]))
    def test_stop_word(self,case_name,sleep_time,v_msg,stop_word):
        self.__dict__['_testMethodDoc'] = case_name
        """
        验证禁用词
        :param case_name:用例名称 
        :param sleep_time: 访客发消息后等待机器人回答时间
        :param v_msg: 访客消息列表
        :param stop_word: 禁用词提示语
        :return: 
        """
        for each_msg in v_msg:
            self.flow.send_msg_to_robot(v_msg=each_msg)
        try:
            time.sleep(sleep_time)
            assert len(self.v_driver.locate_robot_content()) == len(v_msg)
            for each_content in self.v_driver.locate_robot_content():
                assert each_content.text == stop_word
        except AssertionError:
            file_name = "../../data/error_img/chat_img/访客端%s失败_%s.png" % \
                        (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
            self.s_driver.driver.save_screenshot(filename=file_name)



if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestRobotFlows('test_fqa'))
    runner = unittest.TextTestRunner(suit())

