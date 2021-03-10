# -*- coding: utf-8 -*-# 
# ------------------------------------------------------
# @Time :      2021/1/26 21:07 
# @Author :    Neil.Jiang
# @project:    YiQiaUiTest
# @File :      test_basic_chat_flows.py
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


class TestBasicChatFlows(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        url, browser, username, password, company, v_url, v_browser = CompanyConfig().online_524328() + VisConfig().online_524328()
        cls.flow = BasChatFlows(url, browser, username, password, company, v_url, v_browser, )
        cls.s_driver = cls.flow.s_driver
        cls.v_driver = cls.flow.v_driver

    @classmethod
    def tearDownClass(cls) -> None:
        # pass
        cls.s_driver.kill_driver()
        cls.v_driver.kill_driver()

    def setUp(self) -> None:
        warnings.simplefilter('ignore',ResourceWarning)

    def tearDown(self) -> None:
        self.s_driver.driver_refresh()
        self.v_driver.driver_refresh()

    # 添加测试用例
    @parameterized.expand(OpExcel(r'D:\YiQiaUiTest\data\test_case\chat_test_cases.xlsx').get_excel_data('一洽_对话测试用例',
                                                                                                         [1,2,3,4,5,6,7,8],
                                                                                                         columns=[3],
                                                                                                         json_columns=[
                                                                                                             5]))
    def test_send_file(self, case_name, s_file, v_file,  timeout):
        self.__dict__['_testMethodDoc'] = case_name
        """
        测试发送文件
        :param case_name: 用例名称
        :param s_file: 客服文件地址
        :param v_file: 访客文件地址
        :param timeout: 超时时间
        :return:
        """
        self.flow.send_file(s_file=s_file,v_file=v_file)
        time.sleep(7)

        if s_file:
            s_s_file_ele = self.s_driver.locate_present_chat_file(identity=True,timeout=timeout)
            s_s_file_name = []
            v_s_file_ele = self.v_driver.locate_present_chat_file(identity=False, timeout=timeout)
            v_s_file_name = []
            try:
                s_s_file_ele = self.s_driver.locate_present_chat_file(identity=True, timeout=timeout)
                for each_s_s_file in s_s_file_ele:
                    s_s_file_name.append(each_s_s_file[0].text)
                assert s_s_file_name.count(os.path.basename(s_file)) == 1
            except AssertionError:
                s_file_name = "../../data/error_img/chat_img/客服端客服文件數量错误_%s_%s.png" % \
                              (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
                self.s_driver.driver.save_screenshot(filename=s_file_name)
                raise AssertionError
            try:
                v_s_file_ele = self.v_driver.locate_present_chat_file(identity=False, timeout=timeout)
                for each_v_s_file in v_s_file_ele:
                    v_s_file_name.append(each_v_s_file[0].text)
                assert s_s_file_name.count(os.path.basename(s_file)) == 1
            except AssertionError:
                v_file_name = "../../data/error_img/chat_img/访客端客服文件數量错误_%s_%s.png" % \
                              (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
                self.s_driver.driver.save_screenshot(filename=v_file_name)
                raise AssertionError
        if v_file:
            s_v_file_ele = self.s_driver.locate_present_chat_file(identity=False,
                                                                    timeout=timeout)
            s_v_file_name = []
            v_v_file_ele = self.v_driver.locate_present_chat_file(identity=True,
                                                                    timeout=timeout)
            v_v_file_name = []
            try:
                s_v_file_ele = self.s_driver.locate_present_chat_file(identity=False,
                                                                      timeout=timeout)
                for each_s_v_file in s_v_file_ele:
                    s_v_file_name.append(each_s_v_file[0].text)
                assert s_v_file_name.count(os.path.basename(v_file)) == 1
            except AssertionError:
                s_file_name = "../../data/error_img/chat_img/客服端访客文件数量错误_%s_%s.png" % \
                              (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
                self.s_driver.driver.save_screenshot(filename=s_file_name)
                raise AssertionError
            try:
                v_v_file_ele = self.v_driver.locate_present_chat_file(identity=True,
                                                                      timeout=timeout)
                for each_v_v_file in v_v_file_ele:
                    v_v_file_name.append(each_v_v_file[0].text)
                assert v_v_file_name.count(os.path.basename(v_file)) == 1
            except AssertionError:
                v_file_name = "../../data/error_img/chat_img/访客端访客文件数量错误_%s_%s.png" % \
                              (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
                self.s_driver.driver.save_screenshot(filename=v_file_name)
                raise AssertionError
        self.flow.vis_close_chat()

    @parameterized.expand( OpExcel(r'D:\YiQiaUiTest\data\test_case\chat_test_cases.xlsx').get_excel_data('一洽_对话测试用例',
                                                                                                         [18],
                                                                                                         columns=[3],
                                                                                                         json_columns=[
                                                                                                             5]))
    def test_send_text(self, case_name, s_msg, v_msg,  timeout,
                        ):
        self.__dict__['_testMethodDoc'] = case_name
        """
        测试发送文本消息
        :param case_name: 用例名字
        :param s_msg: 客服文本消息
        :param v_msg: 访客文本消息
        :param timeout: 超时时间
        :return:
        """
        self.flow.send_text_msg(s_msg=s_msg,v_msg=v_msg)
        if s_msg:
            s_s_msg_ele = self.s_driver.locate_present_chat_content(identity=True, text_type='text',
                                                                       timeout=timeout)
            s_s_msg_text = []
            v_s_msg_ele = self.v_driver.locate_present_chat_content(identity=False, text_type='text',
                                                                       timeout=timeout)
            v_s_msg_text = []
            try:
                for each_s_s_msg in s_s_msg_ele:
                    s_s_msg_text.append(each_s_s_msg.text)
                assert s_s_msg_text.count(s_msg) == 1
            except AssertionError:
                s_file_name = "../../data/error_img/chat_img/客服端客服文本數量错误_%s_%s.png" % \
                              (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
                self.s_driver.driver.save_screenshot(filename=s_file_name)
                raise AssertionError
            try:
                for each_v_s_msg in v_s_msg_ele:
                    v_s_msg_text.append(each_v_s_msg.text)
                assert v_s_msg_text.count(s_msg) == 1
            except AssertionError:
                v_file_name = "../../data/error_img/chat_img/访客端客服文本數量错误_%s_%s.png" % \
                              (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
                self.s_driver.driver.save_screenshot(filename=v_file_name)
                raise AssertionError
        if v_msg:
            s_v_msg_ele = self.s_driver.locate_present_chat_content(identity=False, text_type='text',
                                                                          timeout=timeout)
            s_v_msg_text = []
            v_v_msg_ele = self.v_driver.locate_present_chat_content(identity=True, text_type='text',
                                                                          timeout=timeout)
            v_v_msg_text = []
            try:
                for each_s_v_msg in s_v_msg_ele:
                    s_v_msg_text.append(each_s_v_msg.text)
                assert s_v_msg_text.count(v_msg) == 1
            except AssertionError:
                s_file_name = "../../data/error_img/chat_img/客服端访客文本数量错误_%s_%s.png" % \
                              (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
                self.s_driver.driver.save_screenshot(filename=s_file_name)
                raise AssertionError
            try:
                for each_v_v_msg in v_v_msg_ele:
                    v_v_msg_text.append(each_v_v_msg.text)
                assert v_v_msg_text.count(v_msg) == 1
            except AssertionError:
                v_file_name = "../../data/error_img/chat_img/访客端访客文本数量错误_%s_%s.png" % \
                              (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
                self.s_driver.driver.save_screenshot(filename=v_file_name)
                raise AssertionError
        self.flow.vis_close_chat()

    @parameterized.expand(OpExcel(r'D:\YiQiaUiTest\data\test_case\chat_test_cases.xlsx').get_excel_data('一洽_对话测试用例',
                                                                                                        [19,20],columns=[3],
                                                                                                        json_columns=[5]))
    def test_send_emoji(self, case_name, s_emojis, s_emoji_type, v_emojis,  timeout):
        self.__dict__['_testMethodDoc'] = case_name
        """
        测试发送表情
        :param case_name: 用例名字
        :param s_emojis: 客服发送表情列表
        :param s_emoji_type: 客服端表情类型
        :param v_emojis: 访客发送表情列表
        :param timeout: 超时时间
        :return:
        """

        # print(s_emojis,s_emoji_type,v_emojis)
        self.flow.send_emoji(s_emojis=s_emojis,s_emoji_type=s_emoji_type,v_emojis=v_emojis)
        if s_emojis:
            s_s_emojis_ele = self.s_driver.locate_present_chat_content(identity=True,text_type='emoji',timeout=timeout)
            all_s_s_emoji_code = []
            v_s_emojis_ele = self.v_driver.locate_present_chat_content(identity=False,text_type='emoji',timeout=timeout)
            all_v_s_emoji_code = []
            try:
                for each_group_emoji in s_s_emojis_ele:
                    for each_emoji in each_group_emoji:
                        all_s_s_emoji_code.append(each_emoji.get_attribute('code'))
                assert all_s_s_emoji_code == s_emojis
            except AssertionError:
                s_file_name = "../../data/error_img/chat_img/客服端客服表情发送错误_%s_%s.png" % \
                              (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
                self.s_driver.driver.save_screenshot(filename=s_file_name)
                raise AssertionError
            try:
                for each_group_emoji in v_s_emojis_ele:
                    for each_emoji in each_group_emoji:
                        all_v_s_emoji_code.append(each_emoji.get_attribute('src').split("/")[-1].split(".")[0])
                #print(all_v_s_emoji_code,s_emojis)
                assert all_v_s_emoji_code == s_emojis
            except AssertionError:
                v_file_name = "../../data/error_img/chat_img/访客端客服表情发送错误_%s_%s.png" % \
                              (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
                self.s_driver.driver.save_screenshot(filename=v_file_name)
                raise AssertionError
        if v_emojis:
            all_s_v_emoji_ele = self.s_driver.locate_present_chat_content(identity=False,text_type='emoji',timeout=timeout)
            all_s_v_emoji_code = []
            all_v_v_emoji_ele = self.v_driver.locate_present_chat_content(identity=True,text_type='emoji',timeout=timeout)
            all_v_v_emoji_code = []
            try:
                for each_group_emoji in all_s_v_emoji_ele:
                    for each_emoji in each_group_emoji:
                        all_s_v_emoji_code.append(each_emoji.get_attribute('src').split("/")[-1].split(".")[0])
                assert all_s_v_emoji_code == v_emojis
            except AssertionError:
                s_file_name = "../../data/error_img/chat_img/客服端访客表情发送错误_%s_%s.png" % \
                              (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
                self.s_driver.driver.save_screenshot(filename=s_file_name)
                raise AssertionError
            try:
                for each_group_emoji in all_v_v_emoji_ele:
                    for each_emoji in each_group_emoji:
                        all_v_v_emoji_code.append(each_emoji.get_attribute('src').split("/")[-1].split(".")[0])

                assert all_v_v_emoji_code == v_emojis
            except AssertionError:
                v_file_name = "../../data/error_img/chat_img/访客端访客表情发送错误_%s_%s.png" % \
                              (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
                self.s_driver.driver.save_screenshot(filename=v_file_name)
                raise AssertionError
        self.flow.vis_close_chat()

    @parameterized.expand(OpExcel(r'D:\YiQiaUiTest\data\test_case\chat_test_cases.xlsx').get_excel_data('一洽_对话测试用例',
                                                                                                         [14],
                                                                                                         columns=[3],
                                                                                                         json_columns=[
                                                                                                             5]))
    def test_send_pic(self, case_name, s_pic,s_contrast_pic, v_pic,v_contrast_pic,  timeout):
        self.__dict__['_testMethodDoc'] = case_name

        """
        测试发送图片
        :param case_name: 用例名字
        :param s_pic: 客服端客服图片
        :param s_contrast_pic:客服端比较图片
        :param v_pic:访客端图片
        :param v_contrast_pic:访客端比较图片
        :param timeout:超时时长
        :return:
        """
        self.flow.send_pic_msg(s_pic=s_pic, v_pic=v_pic)
        if s_pic:
            s_s_pic_ele = self.s_driver.locate_present_chat_pic(identity=True, timeout=timeout)
            v_s_pic_ele = self.v_driver.locate_present_chat_pic(identity=False, timeout=timeout)
            try:
                for each_s_s_pic in s_s_pic_ele:
                    file_name = '../../data/screenshot_img/chat_img' + os.sep + ('客服端界面截图_%s.png' % time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
                    self.s_driver.driver.save_screenshot(filename=file_name)
                    result_file = '../../data/screenshot_img/chat_img' +os.sep + ('目标图片截图_%s.png' % time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
                    self.s_driver.cut_ele_img(ele=each_s_s_pic,origin_file=file_name,reslt_file=result_file)
                    if OpPicture().image_contrast(result_file,s_contrast_pic) <= 50:
                        pass
                    else:
                        raise AssertionError('客服端客服截图和预期图片不一致')
            except AssertionError:
                s_file_name = "../../data/error_img/chat_img/%s_%s.png" % \
                              (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
                self.s_driver.driver.save_screenshot(filename=s_file_name)
                raise AssertionError
            try:
                for each_v_s_pic in v_s_pic_ele:
                    file_name = '../../data/screenshot_img/chat_img/访客端界面截图_%s.png' % time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
                    self.v_driver.driver.save_screenshot(filename=file_name)
                    result_file = '../../data/screenshot_img/chat_img/访客端客服目标图片截图_%s.png' % time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
                    self.v_driver.cut_ele_img(ele=each_v_s_pic, origin_file=file_name, reslt_file=result_file)
                    if OpPicture().image_contrast(result_file,v_contrast_pic) <= 50:
                        pass
                    else:
                        raise AssertionError('访客端客服截图和预期图片不一致')
            except AssertionError:
                s_file_name = "../../data/error_img/chat_img/%s_%s.png" % \
                              (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
                self.v_driver.driver.save_screenshot(filename=s_file_name)
                raise AssertionError
        if v_pic:
            s_v_pic_ele = self.s_driver.locate_present_chat_pic(identity=False, timeout=timeout)
            v_v_pic_ele = self.v_driver.locate_present_chat_pic(identity=True, timeout=timeout)
            try:
                for each_s_v_pic in s_v_pic_ele:
                    file_name = '../../data/screenshot_img/chat_img/客服端界面截图_%s.png' % time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
                    self.s_driver.driver.save_screenshot(filename=file_name)
                    result_file = '../../data/screenshot_img/chat_img/客服端访客目标图片截图_%s.png' % time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
                    self.s_driver.cut_ele_img(ele=each_s_v_pic, origin_file=file_name, reslt_file=result_file)
                    if OpPicture().image_contrast(result_file,s_contrast_pic)<= 50:
                        pass
                    else:
                        raise AssertionError('客服端访客截图和预期图片不一致')
            except AssertionError:
                s_file_name = "../../data/error_img/chat_img/%s_%s.png" % \
                              (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
                self.s_driver.driver.save_screenshot(filename=s_file_name)
                raise AssertionError
            try:
                for each_v_v_pic in v_v_pic_ele:
                    file_name = '../../data/screenshot_img/chat_img/访客端界面截图_%s.png' % time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
                    self.v_driver.driver.save_screenshot(filename=file_name)
                    result_file = '../../data/screenshot_img/chat_img/访客端访客目标图片截图_%s.png' % time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
                    self.v_driver.cut_ele_img(ele=each_v_v_pic, origin_file=file_name, reslt_file=result_file)
                    if OpPicture().image_contrast(result_file,v_contrast_pic) <= 50:
                        pass
                    else:
                        raise AssertionError('访客端访客截图和预期图片不一致')
            except AssertionError:
                s_file_name = "../../data/error_img/chat_img/%s_%s.png" % \
                              (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
                self.v_driver.driver.save_screenshot(filename=s_file_name)
                raise AssertionError
        self.flow.vis_close_chat()

    @parameterized.expand(OpExcel(r'D:\YiQiaUiTest\data\test_case\chat_test_cases.xlsx').get_excel_data('一洽_对话测试用例',
                                                                                                         [25,24],
                                                                                                         columns=[3],
                                                                                                         json_columns=[
                                                                                                             5]))
    def test_submit_evaluation(self,case_name,identify, star,subitem,suggest,default,level_star_class, subject_text,
                               subitem_text):
        self.__dict__['_testMethodDoc'] = case_name
        """
        测试对话中发送满意度评价
        :param case_name: 用例名字
        :param identify: 评价发起者身份 True：客服 ，False:访客
        :param star: 评价等级
        :param subitem: 评价子项
        :param suggest: 评价建议
        :param default: 提交满意度评价 True:提交 False:不提交
        :param level_star_class: 星级的class属性
        :param subject_text: 评价主项的文本
        :param subitem_text: 评价子项的文本
        :return:
        """
        self.flow.send_evaluate(identify, star,subitem,suggest,default)
        # for each in self.s_driver.locate_present_chat_content(identity=False,text_type='text'):
        #     print(each.text)
        #time.sleep(1)
        self.s_driver.locate_all_display_accinfo()
        try:
            # level = self.s_driver.find_eles(ele_type='css',ele='ul.sa-stars')
            # print(level.get_attribute('class'))
            # self.s_driver.locate_evaluate_content()
            level,subject,subitem,suggest_text = self.s_driver.locate_evaluate_content()
            print(level,subject,subitem,suggest_text)
            # for each in (subject,subitem,suggest_text):
            #     print(each[0].text)
            assert level_star_class in level.get_attribute('class')
            assert subject.text == subject_text
            if subitem:
                assert subitem.text == ','.join(subitem_text)
            if suggest:
                assert suggest_text.text == suggest
        except AssertionError:
            s_file_name = "../../data/error_img/chat_img/%s_%s.png" % \
                          (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
            self.s_driver.driver.save_screenshot(filename=s_file_name)
            raise AssertionError
        self.flow.vis_close_chat()

    @parameterized.expand( OpExcel(r'D:\YiQiaUiTest\data\test_case\chat_test_cases.xlsx').get_excel_data('一洽_对话测试用例',
                                                                                                         [26],
                                                                                                         columns=[3],
                                                                                                         json_columns=[
                                                                                                             5]))
    def test_service_play_video(self,case_name,s_file,v_file):
        """
        测试客服端能正常播放视频
        :param case_name:用例名字
        :param s_file:
        :param v_file:
        :param identity:
        :return:
        """
        self.flow.send_file(s_file=s_file,v_file=v_file)
        try:
            self.s_driver.locate_video_msg(identity=True)[0].click()
            count = 1
            while count < 3:
                if 'loading' in self.s_driver.locate_video_play_button().get_attribute('class'):
                    time.sleep(5)
                else:
                    break
            ele = self.s_driver.locate_video_play_button()
            ele.click()
            print(ele.get_attribute('class'))
            assert 'play' in ele.get_attribute('class')
        except AssertionError:
            v_file_name = "../../data/error_img/chat_img/客服视频不能播放_%s_%s.png" % \
                          (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
            self.s_driver.driver.save_screenshot(filename=v_file_name)
            raise AssertionError
        finally:
            self.s_driver.locate_video_close_button().click()

        try:
            self.s_driver.locate_video_msg(identity=False)[0].click()
            count = 1
            while count < 3:
                if 'loading' in self.s_driver.locate_video_play_button().get_attribute('class'):
                    time.sleep(5)
                else:
                    break
            ele = self.s_driver.locate_video_play_button()
            ele.click()
            assert 'play' in ele.get_attribute('class')
        except AssertionError:
            v_file_name = "../../data/error_img/chat_img/访客视频不能播放_%s_%s.png" % \
                          (case_name, time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))
            self.s_driver.driver.save_screenshot(filename=v_file_name)
            raise AssertionError
        finally:
            self.s_driver.locate_video_close_button().click()







if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestBasicChatFlows('test_send_file_msg'))
    runner = unittest.TextTestRunner(suit())

