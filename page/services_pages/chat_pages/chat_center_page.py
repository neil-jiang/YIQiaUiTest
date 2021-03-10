# -*- coding: utf-8 -*-# 
# ------------------------------------------------------
# @Time :      2021/1/18 18:39 
# @Author :    Neil.Jiang
# @project:    YiQiaUiTest
# @File :      chat_center_page.py
# @Email :     jiang.nell@qq.com
# @Description: 
# @命名规范：文件名全小写+下划线，类名大写字母开头，方法和变量小写+下划线连接，常量大写

# -------------------------------------------------------
from page.services_pages.chat_pages.chat_left_page import  ChatLeftPage
from page.visitor_pages.pc_webpage import PcWebPage
from base.config import CompanyConfig, VisConfig
import time
from selenium.webdriver.support.wait import WebDriverWait


class ChatCenterPage(ChatLeftPage):
    def __init__(self, url, browser,username, password, company):
        super().__init__(url, browser,username, password, company)

    def locate_input_box(self):
        """
        定位输入文本框
        :return:
        """
        return self.find_ele("css", 'pre[class="chat-editor chat-editor ng-scope"]')

    def locate_send_button(self):
        """
        定位发送按钮
        :return:
        """
        return self.find_ele("css", 'div[class="editor_bottom noseled editor-chat"] > div.editor_sendbtn')

    def locate_close_button(self):
        """
        定位结束对话按钮
        :return:
        """
        return self.find_ele("class", 'div[class="editor_bottom noseled editor-chat"] > div[class="chat_close noseled"]]')

    def locate_emoji_tab(self):
        """
        定位表情按钮
        :return:
        """
        return self.find_ele("css", 'div.icon.emotion')

    def locate_emoji_type(self,default_type):
        """
        定位表情的类型
        :param default_type:默认表情
        :return:
        """
        if default_type:
            # 定位QQ表情按钮
            return self.find_ele(ele_type="css", ele="span.emotion-bar-item.emotion-icon-qq")
        else:
            # 定位我们自己的表情按钮
            return self.find_ele(ele_type="css", ele="span.emotion-bar-item.emotion-icon-emoji")

    def locate_emoji_pool(self, target_emoji):
        """
        定位emoji_pool里的元素
        :param target_emoji: 指定的emoji
        :return:
        """
        all_emojis = self.find_eles(ele_type="css", ele='div[class="emotion-list ng-scope"] > i')
        for each_emoji in all_emojis:
            if each_emoji.get_attribute("code") == target_emoji:
                return each_emoji
        else:
            raise ValueError("没有找到该元素")

    def locate_image_tab(self):
        """
        定位图片按钮
        :return:
        """
        return self.find_ele("css", 'div.icon.pic > form > input')

    def lcoate_file_tab(self):
        """
        定位文件按钮
        :return:
        """
        return self.find_ele("css", 'div.icon.file > form > input')

    def locate_evaluate_tab(self):
        """
        定位满意度按钮
        :return:
        """
        return self.find_ele("css", "div.icon.evaluate")

    def locate_evaluate_content(self):
        """
        定位满意度评价等级
        :return:
        """
        # 满意度等级
        level = self.find_ele(ele_type="css", ele="ul.sa-stars")

        # 满意度主题
        subject = self.find_ele(ele_type="css", ele="div[class='chat_history_item history-bubble ng-scope from_system'] "
                                                  "div[ng-bind='$parent.rec.evaluateName']")

        # 满意度子项
        subitem = self.find_ele(ele_type="css", ele="div[class='chat_history_item history-bubble ng-scope from_system'] "
                                                     "div[ng-bind='$parent.rec.evaluateSubName']")

        # 满意度建议

        suggest = self.find_ele(ele_type="css", ele="div[class='chat_history_item history-bubble ng-scope from_system'] "
                                                     "div[ng-bind='$parent.rec.evaluateComment']")

        return [level,subject,subitem,suggest]

    def locate_invite_evaluate_button(self,default=True):
        """
        定位满意度邀请按钮
        :param default:
        :return:
        """
        if default:
            # 返回确认按钮
            return self.find_ele(ele_type="css", ele="div.dialog-btns > button.btn.btn-primary")
        # 返回取消按钮
        return self.find_ele(ele_type="css", ele='button[class="btn btn-default"]')

    def locate_topic_evaluate(self):
        """
        定位对话主题按钮
        :return:
        """
        return self.find_ele("css", "div.icon.init-sumup")

    def locate_pushurl_tab(self):
        """
        定位推送url按钮
        :return:
        """
        return self.find_ele("css", "div.icon.pushurl")

    def lcoate_translator_tab(self):
        """
        定位翻译按钮
        :return:
        """
        return self.find_ele("css", "div.icon.translator")

    def locate_auto_help(self):
        """
        定位智能辅助按钮
        :return:
        """
        return self.find_ele("css", "span[ng-click='toggleExternal(2,5)']")

    def locate_msg_history(self):
        """
        定位消息记录按钮
        :return:
        """
        return self.find_ele("css", "i.icon.short_msg")

    def locate_all_display_accinfo(self):
        """
        定位所有显示出的接入信息
        :return:
        """

        # 定位接入信息的title
        accinfo_titles = self.find_eles(ele_type="css",
                                   ele="div[class='chat_history_item history-bubble ng-scope from_system'] > div[class='lunch-detail ng-scope'] > div[class='lunch-detail-line'] > dt")
        # 定位接入信息的内容
        accinfo_contents = self.find_eles(ele_type="css",
                                   ele="div[class='chat_history_item history-bubble ng-scope from_system'] > div[class='lunch-detail ng-scope'] > div[class='lunch-detail-line'] > dd")

        return accinfo_titles, accinfo_contents

    def locate_present_chat_pic(self,identity,timeout):
        """
        定位客服发送的图片消息
        :return:
        """
        if identity:
            return self.find_eles(ele_type="css",
                              ele="div[class='chat_history_item history-bubble ng-scope from_service'] div.img-wrap > img[class='view_img']",
                                  timeout=timeout)
        else:
            return self.find_eles(ele_type="css",
                              ele="div[class='chat_history_item history-bubble ng-scope from_visitor'] div.img-wrap > img[class='view_img']",
                                  timeout=timeout)

    def locate_present_chat_file(self,identity,timeout):
        if identity:
            # 所有的客服的文件消息
            pre_ele = self.find_eles(ele_type="css",
                                     ele="div[class='chat_history_item history-bubble ng-scope from_service'] "
                                         "div[class='file_msg_info']")
        else:
            # 所有的访客的文件消息
            pre_ele = self.find_eles(ele_type="css",
                                     ele="div[class='chat_history_item history-bubble ng-scope from_visitor'] "
                                         "div[class='file_msg_info']")

        all_eles = [] # 对话框该身份的所有文件元素

        for each_file in pre_ele:
            each_file_name = WebDriverWait(self.driver,
                                              timeout=timeout).until(
                    lambda x: each_file.find_element_by_css_selector("div[class='file_info_name']"))
            each_file_download_button = WebDriverWait(self.driver,
                                              timeout=timeout).until(
                    lambda x: each_file.find_element_by_xpath("./following-sibling::div"))
            all_eles.append([each_file_name,each_file_download_button])
        return all_eles


    def locate_present_chat_content(self, identity, text_type, timeout=10):
        """
        定位对话框所有的文本消息
        :return:
        """

        if identity:
            # 所有的客服消息
            pre_ele = self.find_eles(ele_type="css",
                                     ele="div[class='chat_history_item history-bubble ng-scope from_service']")
        else:
            # 所有的访客消息
            pre_ele = self.find_eles(ele_type="css",
                                     ele="div[class='chat_history_item history-bubble ng-scope from_visitor']")
        all_eles = []  # 对话框所有该身份的文本消息
        if text_type == "text":
            for each_text in pre_ele:
                #  添加对话框所有的文本消息到all_eles
                all_eles.append(WebDriverWait(self.driver,
                                              timeout=timeout).until(
                    lambda x: each_text.find_element_by_css_selector("div[class='chat_content_con ng-binding']")))
        elif text_type == "emoji":
            for each_text in pre_ele:
                # 找一遍访客发的全部emoji消息
                eles = each_text.find_elements_by_css_selector("div[class='chat_content_con ng-binding'] > img")
                if eles == []:
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

    def locate_video_msg(self, identity):
        """
        定位客服发的视频消息
        :return:
        """
        if identity:
            # 返回客服发的视频消息
            return self.find_eles(ele_type="css", ele="div[class='chat_history_item history-bubble ng-scope from_service'] "
                                                  "div[class='video-wrap file-video']")
        else:
            # 返回访客发的视频消息
            return self.find_eles(ele_type="css", ele="div[class='chat_history_item history-bubble ng-scope from_visitor'] "
                                                  "div[class='video-wrap file-video']")

    def locate_video_play_button(self):
        """
        定位播放按钮
        :return:
        """
        return self.find_ele(ele_type="css", ele="div.gallery-tools > span")

    def locate_video_close_button(self):
        """
        定位视频关闭按钮
        :return:
        """
        return self.find_ele(ele_type="css", ele="button.gallery-close")

    def locate_clicked_video(self):
        """
        定位点击后的视频消息
        :return:
        """
        return self.find_ele(ele_type="css", ele="video[class='gallery-video']")

    def locate_service_pushurl(self):
        """
        定位客服发送的推送链接
        :return:
        """
        # 链接名称
        url_titles = self.find_eles(ele_type="css", ele="div[class='chat_history_item history-bubble ng-scope from_service'] "
                                                        "div[ng-bind='rec.urlName']")
        # 链接
        url_content = self.find_eles(ele_type="css", ele="div[class='chat_history_item history-bubble ng-scope from_service'] "
                                                        "div[ng-bind='rec.url']")

    def locate_warm_prompt(self):
        """
        定位温馨提示
        :return:
        """
        return self.find_ele(ele_type="css", ele="div.dialog-cnt")

if __name__ == '__main__':
    print(CompanyConfig().online_521889() + VisConfig().online_521889())
    url, browser, username, password, company = CompanyConfig().online_521889()
    service_driver = ChatCenterPage(url="http://e.echatsoft.com/login-page/v2/login.html?language=zh",browser='chrome',
                                    username=username, password=password, company=company )
    service_driver.locate_report()
    vis_driver = PcWebPage(url="https://www.echatsoft.com/visitor/pc/chat.html?companyId=521889", browser='firefox')
    service_driver.locate_all_display_accinfo()


    print(vis_driver.locate_present_chat_file(identity=False,timeout=10))



    #print(service_driver.locate_present_chat_file(identity=True,timeout=11))

    # print(service_driver.locate_warm_prompt().text)
    # assert service_driver.locate_warm_prompt().text == '不支持的文件类型\n' \
    #                   '支持类型：txt, doc, docx, xls, xlsx, amr, mp3, mp4, rar, zip, pdf, wav, log, mov, ppt, pptx, 3gp, aac, webm, ts, 3g2, 3gpp, 3gpp2, avi, m4v, mkv, ogg, psd, ai, ttf, aep, cdr, otf, vsp, prproj, c4d, jpg, png, gif, jpeg, webp, bmp'
    # #     service_driver.locate_emoji_tab().click()
    # #     service_driver.locate_emoji_type(default_type='').click()
    # #     service_driver.locate_emoji_pool('1f604').click()