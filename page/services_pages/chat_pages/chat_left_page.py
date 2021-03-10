# -*- coding: utf-8 -*-# 
# ------------------------------------------------------
# @Time :      2021/1/18 18:40 
# @Author :    Neil.Jiang
# @project:    YiQiaUiTest
# @File :      chat_left_page.py
# @Email :     jiang.nell@qq.com
# @Description: 
# @命名规范：文件名全小写+下划线，类名大写字母开头，方法和变量小写+下划线连接，常量大写

# -------------------------------------------------------
from page.services_pages.home_page import MenuBar


class ChatLeftPage(MenuBar):
    def __init__(self, url, browser,username, password, company):
        super().__init__(url, browser,username, password, company)
        self.locate_chat().click()

    def locate_queue(self):
        """
        定位排队中按钮
        :return:
        """
        return self.find_ele("css", 'div.chat_list_box.chat_onself > div.chat_lists > div.cl_box.chat-visitor.noseled > div.cm_labels > div:nth-child(1) > span')

    def locate_all_button(self):
        """
        定位排队中的所有按钮
        :return:
        """
        return self.find_ele("css", 'div.chat_list_box.chat_onself > div.chat_lists > div.cl_box.chat-visitor.noseled > div.cm_lists > div:nth-child(1) > div.sort-wrap > div.sort-btn > span')

    def locate_vis_button(self):
        """
        定位排队中的游客按钮
        :return:
        """
        return self.find_ele("css", 'div.chat_list_box.chat_onself > div.chat_lists > div.cl_box.chat-visitor.noseled > div.cm_lists > div:nth-child(1) > div.sort-wrap > div.sort-btn > span:nth-child(2)')

    def locate_mem_button(self):
        """
        定位排队中的会员按钮
        :return:
        """
        return self.find_ele("css", 'div.chat_list_box.chat_onself > div.chat_lists > div.cl_box.chat-visitor.noseled > div.cm_lists > div:nth-child(1) > div.sort-wrap > div.sort-btn > span:nth-child(3)')

    def locate_chating(self):
        """
        定位对话中按钮
        :return:
        """
        return self.find_ele("css", 'div.chat_list_box.chat_onself > div.chat_lists > div.cl_box.chat-visitor.noseled > div.cm_labels > div:nth-child(2) > span')

    def locate_ended(self):
        """
        定位已结束按钮
        :return:
        """
        return self.find_ele("css", 'div.chat_list_box.chat_onself > div.chat_lists > div.cl_box.chat-visitor.noseled > div.cm_labels > div:nth-child(3) > span')

    def locate_present_button(self):
        """
        定位已结束的当前按钮
        :return:
        """
        return self.find_ele("css", 'div.chat_list_box.chat_onself > div.chat_lists > div.cl_box.chat-visitor.noseled.ng-scope.closing > div.cm_lists > div.cm_list.chat-list-end.noscroll > div > div.sort-btn > span:nth-child(1)')

    def locate_history_button(self):
        """
        定位已结束的历史按钮
        :return:
        """
        return self.find_ele("css", 'div.chat_list_box.chat_onself > div.chat_lists > div.cl_box.chat-visitor.noseled.ng-scope.closing > div.cm_lists > div.cm_list.chat-list-end.noscroll > div > div.sort-btn > span:nth-child(2)')

    def locate_visitors_in_view(self):
        """
        定位浏览中的访客按钮
        :return:
        """
        return self.find_ele("css", 'div.chat_list_box.chat_onself > div.cl_header > div > span')

    def locate_view_lists(self):
        """
        定位浏览中的访客列表
        :return:
        """
        return self.find_eles("css", 'tr[ng-repeat="vis in visitors track by vis.visitorId"]')

    def locate_chat_lists(self):
        """
        定位对话中的访客列表
        :return: 对话中的访客列表
        """
        eles = []
        try:
            #print(self.find_ele("css",'div[class="chat-list-wrap"][ng-show="chatList.length"]> div'))
            eles.append(self.find_ele("css",'div[class="chat-list-wrap"][ng-show="chatList.length"]> div'))
        except:
            pass
        try:
            #print(self.find_eles("css", 'div[class="chat-list-wrap"][ng-show="chatList.length"]> div ~ div'))
            eles = eles + self.find_eles("css", 'div[class="chat-list-wrap"][ng-show="chatList.length"]> div ~ div')
        except:
            pass
        return eles

    def locate_queue_lists(self):
        """
        定位排队中的访客列表
        :return: 对话中的访客列表
        """

        eles = []
        try:
           # print(self.find_ele("css", 'div[class="chat-list-wrap"][ng-show="waitList.length"]> div'))
            eles.append(self.find_ele("css", 'div[class="chat-list-wrap"][ng-show="waitList.length"]> div'))
        except:
            pass
        try:
            #print(self.find_eles("css", 'div[class="chat-list-wrap"][ng-show="waitList.length"]> div ~ div'))
            eles = eles + self.find_eles("css", 'div[class="chat-list-wrap"][ng-show="waitList.length"]> div ~ div')[:-1]
        except:
            pass
        #print(eles)
        return eles


if __name__ == '__main__':
    pass
