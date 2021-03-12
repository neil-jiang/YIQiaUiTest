# -*- coding: utf-8 -*-#
# ------------------------------------------------------
# @Time :      2021/1/14 17:26
# @Author :    Neil.Jiang
# @project:    YiQiaUiTest
# @File :      pc_webpage.py
# @Email :     jiang.nell@qq.com
# @Description:
# @命名规范：文件名全小写+下划线，类名大写字母开头，方法和变量小写+下划线连接，常量大写

# -------------------------------------------------------
from base.base import Base
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from services_pages.home_page import MenuBar
import os
import time
from config import CompanyConfig


class PcWebPage(Base):

    def __init__(self, url, browser="chrome"):
        super().__init__(url=url,browser=browser)

    def locate_emoji_tab(self):
        """
        定位输入框上面的emoji元素
        :return:返回该元素
        """
        self.find_frame(frame_content='')
        return self.find_ele(ele_type="css", ele="#toolbar > ul > li.menu-item.menu-emo")

    def locate_file_tab(self):
        """
        定位输入框文件按钮
        :return:返回该元素
        """
        self.find_frame(frame_content='')
        return self.find_ele(ele_type="css", ele="#uploadInput")

    def locate_evaluation_tab(self):
        """
        定位满意度评价按钮
        :return:
        """
        self.find_frame(frame_content='')
        return self.find_ele(ele_type="css", ele="#menuSatisfy")

    def locate_evaluation_star(self):
        """
        定位满意度打分按钮
        :return:
        """
        return self.find_eles(ele_type="css", ele="#satisfyConfig > ul >li")

    def locate_evaluation_subname(self):
        """
        定位满意度子项
        :return:
        """
        return self.find_eles(ele_type="css", ele="#satisfyConfig > div.sub-tabs.clearfix > ul.sub-tab-sel > li")

    def locate_evaluation_suggest(self):
        """
        定位满意度评价文本框
        :return:
        """
        return self.find_ele(ele_type="css", ele="#sa_advise")

    def locate_evaluation_confirm_button(self,default):
        """
        定位满意度提交按钮
        :return:
        """
        if default:
            # 提交
            return self.find_ele(ele_type="css", ele="#sa_ok")
        else:
            # 取消
            return self.find_ele(ele_type="css", ele="sa_cancel")

    def locate_evaluation_submit_hint(self):
        """
        定位满意度提交提示
        :return:
        """
        return self.find_ele(ele_type="css", ele="#leave_tip_con")

    def locate_pool_emoji(self, target_emoji):
        """
        定位emoji池
        :param target_emoji: 目标emoji选项
        :return: 返回该选择的选项
        """
        self.find_frame(frame_content='')
        all_emojis = self.find_eles(ele_type="xpath", ele='//*[@id="emo_list"]/li')
        for each_emoji in all_emojis:
            if each_emoji.get_attribute("code") == target_emoji:
                return each_emoji
        else:
            raise ValueError("没有找到该元素")

    def locate_input_box(self):
        """
        定位输入文本框
        :return:
        """
        self.find_frame(frame_content="html_input")
        return self.find_ele(ele_type="css", ele="body")

    def locate_send_button(self):
        """
        定位发送按钮
        :return:
        """
        self.find_frame(frame_content='')
        return self.find_ele(ele_type="css", ele='#enter_btn')

    def locate_kill_session_button(self):
        """
        定位结束对话按钮
        :return:
        """
        self.find_frame(frame_content='')
        return self.find_ele(ele_type="css", ele="#close2_btn")

    def locate_warm_prompt_box(self, chose="True"):
        """
        定位温馨提示框
        :param chose: 如果chose等于True点击确定按钮，否则点击取消按钮，默认为True
        :return:
        """
        self.find_ele(ele_type="css", ele="#index > div.dialog")
        if chose == "True":
            return self.find_ele(ele_type="css",
                                 ele="#index > div.dialog > div.dialog-btns > a.dialog-btn.dialog-ok.bg0")
        else:
            return self.find_ele(ele_type="css",
                                 ele="#index > div.dialog > div.dialog-btns > a.dialog-btn.dialog-cancel.bg0.has-fade")

    def locate_restart_msg(self):
        """
        定位重新启动按钮
        :return:返回该元素
        """
        self.find_frame(frame_content='')
        return self.find_ele(ele_type="css", ele="#restartChat")

    # def locate_page_hint(self):
    #     """
    #     定位继续对话按钮
    #     :return: 返回该元素
    #     """
    #     self.find_frame(frame_content='')
    #     return self.find_ele(ele_type="css", ele="li[id^='msg'] > div[class='msg-info radius4'] > div.info-con")

    def locate_present_chat_content(self,identity, text_type,timeout=10):
        """
        定位所有的class 属性含有mode0消息,mode0消息，该方法定位了表情和文本
        :return:
        """
        self.find_frame(frame_content='')
        if identity:
            # 访客的mode0消息
            pre_ele = self.find_eles(ele_type="css", ele="#list_msg > li[class='clearfix mode0']")
        else:
            # 客服的mode0消息
            pre_ele = self.find_eles(ele_type="css", ele="#list_msg > li[class='clearfix  mode0']")
        # 全部的要找的文本或emoji
        all_eles = []  #对话框所有该身份的mode0消息
        if text_type == "text":
            for each_text in pre_ele:
                #  添加对话框所有的文本消息到all_eles
                all_eles.append(WebDriverWait(self.driver,
                                              timeout=timeout).until(lambda x: each_text.find_element_by_css_selector("div.msg-item")))
        elif text_type == "emoji":
            for each_text in pre_ele:
                # 找一遍访客发的全部emoji消息
                eles = each_text.find_elements_by_css_selector("div[class='msg-item'] > img.img-emo")
                if eles==[]:
                    pass
                else:
                    # 把一条访客消息的全部emoji元素,添加到all_eles
                    all_eles.append(WebDriverWait(self.driver,
                                                  timeout=timeout).until(
                        lambda x: eles))
        else:
            # 输入类型有误
            raise ValueError
        return all_eles

    def locate_present_chat_service_mode0(self):
        """
        定位当前对话客服发的文本消息
        :return:
        """
        self.find_frame(frame_content='')
        return self.find_eles(ele_type="css", ele="#list_msg > li[class='clearfix  mode0']")

    def locate_present_chat_file(self,identity,timeout):
        """
        定位当前对话的文件消息：
        :return:
        """
        self.find_frame(frame_content='')
        if identity:
            pre_ele = self.find_eles(ele_type='css', ele='li[class="clearfix modeundefined"] div[class="file-info"]')
        else:
            pre_ele = self.find_eles(ele_type='css', ele='li[class="clearfix  mode1"] div[class="file-info"]')
        all_eles = []
        for each_file in pre_ele:
            each_file_name = WebDriverWait(self.driver,
                                           timeout=timeout).until(
                lambda x: each_file.find_element_by_css_selector("div[class='file-name']"))
            each_file_download_button = WebDriverWait(self.driver,
                                                      timeout=timeout).until(
                lambda x: each_file.find_element_by_xpath("./following-sibling::a"))
            all_eles.append([each_file_name, each_file_download_button])
        return all_eles

    def locate_present_chat_pic(self,identity,timeout):
        self.find_frame(frame_content='')
        if identity:
            return self.find_eles(ele_type='css', ele='li[class="clearfix modeundefined"] div[class="msg-item"]> img')
        else:
            return self.find_eles(ele_type='css', ele='li[class="clearfix  mode2"] div[class="msg-item"]> img')

    def locate_his_chat_vis_mode0(self, text_type, timeout=10):
        """
        定位历史消息中访客发的所有的class 属性含有mode0消息,mode0消息，该方法定位了表情和文本
        :return:
        """
        self.find_frame(frame_content='')
        pre_ele = self.find_eles(ele_type="css", ele="ul[id^='list_msg_'][class='list-msg list-msg-his'] >"
                                                     " li[class='clearfix mode0']")
        # 全部的要找的文本或emoji
        all_eles =[]
        if text_type == "text":
            for each_text in pre_ele:
                #  添加对话框文本
                # print(dir(each_text))
                all_eles.append(WebDriverWait(self.driver,
                                 timeout=timeout).until(lambda x: each_text.find_element_by_css_selector("div.msg-item")))
        elif text_type == "emoji":
            for each_text in pre_ele:
                # 添加对话框的表情
                all_eles.append(WebDriverWait(self.driver,
                                 timeout=timeout).until(lambda x: each_text.find_element_by_css_selector("div.msg-item > img")))
        else:
            # 输入类型有误
            raise ValueError
        return all_eles

    def locate_his_chat_vis_mode2(self):
        """
        定位历史消息中访客发的所有class属性含有mode2的消息，图片消息
        :return:
        """
        self.find_frame(frame_content='')
        return self.find_eles(ele_type="css", ele="ul[id^='list_msg_'][class='list-msg list-msg-his'] >"
                                                  " li[class='clearfix mode2']")

    def locate_greeting(self):
        """
        定位欢迎语
        :return:
        """
        self.find_frame(frame_content='')
        return self.find_eles(ele_type="css",ele="li[class='clearfix msg-info-hasAvatar'] > div > div")

    def lcoate_his_button(self):
        """
        定位查看历史消息按钮
        :return:
        """
        return self.find_ele(ele_type="css", ele="#pre_his")

    def locate_tohumantip(self):
        """
        定位转人工提示
        :return:
        """
        return self.find_ele(ele_type='id', ele='toHumanWords')

    def locate_tohumanbutton(self):
        """
        定位转人工按钮
        :return:
        """
        return self.find_ele(ele_type='id', ele='robotToStaffWord')

    def locate_input_box_prompt(self):
        """
        定位输入框提示语
        :return:
        """
        return self.find_ele(ele_type='id', ele='textInput')

    def locate_robot_content(self,system_text=True):
        """
        定位机器人文本消息
        :param system_text:为真返回系统提示语：列如禁用词提示语，未识别答案提示语
        :return:
        """
        if system_text:
            return self.find_eles(ele_type='css', ele='div[class="msg-item-robot"]')
        else:
            return self.find_eles(ele_type='css', ele='div[class="msg-item-robot"] > p')

    def lcoate_robot_welcome(self, fqa):
        """
        定位欢迎语
        :param fqa:如果为真则返回常见问题列表和常见问题提示 ，否则只返回欢迎语
        :return:
        """
        if fqa:
            fqa_list = self.find_eles(ele_type='css', ele='li[class="common-ques-li"]')
            fqa_prompt = self.find_ele(ele_type='css', ele='div.common-ques-tip')
            welcome_prompt = self.find_ele(ele_type='css', ele='div.msg-item')
            return fqa_list, fqa_prompt, welcome_prompt
        else:
            return self.find_ele(ele_type='css', ele='div.msg-item')

    def locate_question_list(self,timeout):
        """
        定位问题列表
        :param timeout:
        :return:
        """

        question_lists = self.find_eles(ele_type='css', ele='ul.question-list')

        target_question_lists_box = []
        for each_question_list in question_lists:
            # 问题提示语：le:我猜你的问题是
            tip = WebDriverWait(self.driver,timeout=timeout).until(
                lambda x: each_question_list.find_element_by_css_selector("div.robot-tip"))
            # 问题序号
            serial = WebDriverWait(self.driver,timeout=timeout).until(
                lambda x: each_question_list.find_elements_by_css_selector("span.list-style-dot"))
            # 问题内容
            question = WebDriverWait(self.driver,timeout=timeout).until(
                lambda x: each_question_list.find_elements_by_css_selector("span.color-link"))
            target_question_lists_box.append([tip,serial,question])
        return target_question_lists_box

    def locate_confirm_question_solved_button(self,choice):
        """
        定位问题解决按钮
        :param choice:为真定位“是”为假定位“否”
        :return:
        """
        if choice:
            return self.find_eles(ele_type='css',ele="div.feedback-btn-solve")
        else:
            return self.find_eles(ele_type='css',ele="div.feedback-btn-unsolve")





if __name__ == '__main__':
    # url, browser,username, password, companyid = CompanyConfig().online_521889()
    # driver = MenuBar(url, browser,username, password, companyid)
    # time.sleep(5)
    # print(driver.locate_service_internal_photo().get_attribute("src"))
    # driver.open_new_handle("https://chats.rainbowred.com/visitor/pc/chat.html?companyId=2151")
    url = "https://www.echatsoft.com/visitor/pc/chat.html?companyId=524328&echatTag=jq"
    #driver = base.Base("https://www.echatsoft.com/visitor/pc/chat.html?companyId=521889")

    vistor_driver = PcWebPage(url)
    fqa_list, fqa_prompt, welcome_prompt = vistor_driver.lcoate_robot_welcome(fqa='True')
    print(fqa_list[0].text, fqa_prompt.text, welcome_prompt.text.count("宝宝，我来了！请详细描述你要求助的问题，让我更好的帮助你哦")==1)

    #vistor_driver.locate_input_box().click()
    #time.sleep(1)
    # vistor_driver.locate_input_box_prompt().send_keys('吗')
    # vistor_driver.locate_send_button().click()
    # alleles = vistor_driver.locate_question_list(11)
    # print(alleles)
    # for each in alleles[0][1]:
    #     print(each.text)
    # for each in alleles[0][2]:
    #     print(each.text)




    #time.sleep(22)
    # print(vistor_driver.locate_greeting()[0].text)
    # vistor_driver.locate_input_box().send_keys("21212")
    # vistor_driver.locate_send_button().click()
    # vistor_driver.locate_input_box().send_keys("dasd")
    # vistor_driver.locate_send_button().click()
    # vistor_driver.locate_input_box().send_keys("212d大萨达所多22")
    # vistor_driver.locate_send_button().click()
    # vistor_driver.locate_emoji_tab().click()
    # vistor_driver.locate_pool_emoji(target_emoji="1f604").click()
    # vistor_driver.locate_emoji_tab().click()
    # vistor_driver.locate_pool_emoji(target_emoji="1f60a").click()
    # vistor_driver.locate_send_button().click()
    # vistor_driver.locate_emoji_tab().click()
    # vistor_driver.locate_pool_emoji(target_emoji="1f604").click()
    # vistor_driver.locate_emoji_tab().click()
    # vistor_driver.locate_pool_emoji(target_emoji="1f60a").click()
    # vistor_driver.locate_send_button().click()

    # all_eles = vistor_driver.locate_present_chat_content(text_type="text")
    #
    # for each in all_eles:
    #     print(each.text)
    # all_eles1 = vistor_driver.locate_present_chat_content(identity=True,text_type="emoji")
    # for each in all_eles1:
    #     print(each)
