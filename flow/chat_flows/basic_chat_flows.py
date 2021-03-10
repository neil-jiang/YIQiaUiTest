# -*- coding: utf-8 -*-# 
# ------------------------------------------------------
# @Time :      2021/1/25 16:12 
# @Author :    Neil.Jiang
# @project:    YiQiaUiTest
# @File :      basic_chat_flows.py
# @Email :     jiang.nell@qq.com
# @Description: 
# @命名规范：文件名全小写+下划线，类名大写字母开头，方法和变量小写+下划线连接，常量大写

# -------------------------------------------------------
from page.visitor_pages.pc_webpage import PcWebPage
from page.services_pages.chat_pages.chat_center_page import ChatCenterPage
from base.config import CompanyConfig
from base.config import VisConfig
import time


class BasChatFlows:
    def __init__(self,url, browser, username, password, company,v_url,v_browser):
        self.s_driver = ChatCenterPage(url, browser, username, password, company)
        # 这一步的目的是定位到客服界面加载完成
        self.s_driver.locate_report()
        self.v_driver = PcWebPage(url=v_url,browser=v_browser)

    def send_text_msg(self,s_msg, v_msg):
        """
        发送文本消息
        :param s_msg:客服发的文本消息
        :param v_msg: 访客发的文本消息
        :return:
        """
        if s_msg:
            self.s_driver.locate_all_display_accinfo()  # 定位接入信息
            self.s_driver.locate_input_box().send_keys(s_msg)
            self.s_driver.locate_send_button().click()
        if v_msg:
            self.v_driver.locate_input_box().click()
            self.v_driver.locate_input_box().send_keys(v_msg)
            self.v_driver.locate_send_button().click()

    def send_pic_msg(self,s_pic,v_pic):
        """
        发送图片消息
        :param s_pic:客服图片路径
        :param v_pic: 访客图片路径
        :return:
        """
        if s_pic:
            self.s_driver.locate_all_display_accinfo()
            self.s_driver.locate_image_tab().send_keys(s_pic)
        if v_pic:
            self.v_driver.locate_file_tab().send_keys(v_pic)

    def send_file(self, s_file, v_file):
        """
        发送文件消息
        :param s_file:客服发送文件路径
        :param v_file: 访客发送文件路径
        :return:
        """
        if s_file:
            self.s_driver.locate_all_display_accinfo()
            self.s_driver.lcoate_file_tab().send_keys(s_file)
        if v_file:
            self.v_driver.locate_file_tab().send_keys(v_file)

    def send_emoji(self,s_emojis, s_emoji_type,v_emojis):
        """
        发送emoji消息
        :param s_emojis:客服要发送的emoji列表
        :param s_emoji_type: emoji的类型，分为QQ表情和我们自己的表情
        :param v_emojis: 访客要发送的emoji列表
        :return:
        """
        if s_emojis:
            self.s_driver.locate_all_display_accinfo()
            self.s_driver.locate_emoji_tab().click()
            self.s_driver.locate_emoji_type(s_emoji_type).click()
            for each_s_emoji in s_emojis:
                self.s_driver.locate_emoji_pool(each_s_emoji).click()
            self.s_driver.locate_send_button().click()
        if v_emojis:
            for each_v_emoji in v_emojis:
                self.v_driver.locate_emoji_tab().click()
                self.v_driver.locate_pool_emoji(each_v_emoji).click()
            self.v_driver.locate_send_button().click()

    def send_evaluate(self, identify, star,subitem,suggest,default):
        """
        发送满意度评价
        :param star: 满意度星级
        :param identify:评价发起者身份
        :param suggest: 满意度建议
        :param default: 满意度确认提交按钮
        :return:
        """
        if identify:
            # 客服发起提交满意度评价
            self.s_driver.locate_all_display_accinfo()
            self.s_driver.locate_evaluate_tab().click()
            self.s_driver.locate_invite_evaluate_button().click()
            if star in range(1,6):
                self.v_driver.locate_evaluation_star()[star-1].click()
            else:
                raise ValueError("满意度星级不对")
            if subitem:
                for each_item in subitem:
                    self.v_driver.locate_evaluation_subname()[each_item-1].click()
            self.v_driver.locate_evaluation_suggest().send_keys(suggest)
            self.v_driver.locate_evaluation_confirm_button(default).click()
            evaluate_hit = self.v_driver.locate_evaluation_submit_hint()
            return evaluate_hit
        else:
            # 访客发起提交满意度评价
            self.s_driver.locate_all_display_accinfo()
            self.v_driver.locate_input_box().send_keys("我要主动提交满意度评价咯")
            self.v_driver.locate_send_button().click()
            self.v_driver.locate_evaluation_tab().click()
            if star in range(1, 6):
                self.v_driver.locate_evaluation_star()[star - 1].click()
            else:
                raise ValueError("满意度星级不对")
            if subitem:
                for each_item in subitem:
                    self.v_driver.locate_evaluation_subname()[each_item-1].click()
            self.v_driver.locate_evaluation_suggest().send_keys(suggest)
            self.v_driver.locate_evaluation_confirm_button(default).click()
            evaluate_hit = self.v_driver.locate_evaluation_submit_hint()
            return evaluate_hit

    # def vis_send_evaluate(self,star,suggest,default):
    #     """
    #     访客主动发送满意度评价
    #     :param star:
    #     :param suggest:
    #     :param default:
    #     :return:
    #     """
    #     self.s_driver.locate_all_display_accinfo()
    #     self.v_driver.locate_input_box().send_keys("我要主动提交满意度评价咯")
    #     self.v_driver.locate_send_button().click()
    #     self.v_driver.locate_evaluation_tab().click()
    #     if star in range(1, 6):
    #         self.v_driver.locate_evaluation_star()[star - 1].click()
    #     else:
    #         raise ValueError("满意度星级不对")
    #     self.v_driver.locate_evaluation_suggest().send_keys(suggest)
    #     self.v_driver.locate_evaluation_confirm_button(default).click()
    #     evaluate_hit = self.v_driver.locate_evaluation_submit_hint()
    #     return evaluate_hit

    def vis_close_chat(self):
        self.v_driver.locate_kill_session_button().click()
        self.v_driver.locate_warm_prompt_box().click()


    def test_get_ser_vis_basic_msg(self,s_msg,v_msg):
        self.send_text_msg(s_msg=s_msg,v_msg=v_msg)
        self.s_driver.locate_service_content()

if __name__ == '__main__':
    service = CompanyConfig.online_521889()
    vis = VisConfig.online_521889()
    chat_flow = BasChatFlows(*service, *vis)
    chat_flow.send_evaluate(identify=False,subitem=[1,2],star=4,suggest='你是最帅的',default=True)


    # all_eles = chat_flow.s_driver.locate_present_chat_content(identity=True,text_type='emoji',timeout=10)
    # print(all_eles)
    # all_eles = chat_flow.s_driver.locate_present_chat_content(identity=False, text_type='emoji', timeout=10)
    # print(all_eles)
    #all_eles = chat_flow.v_driver.locate_present_chat_content()
    #print(chat_flow.vis_send_evaluate(4,"你好漂亮",1).text)