# -*- coding: utf-8 -*-# 
# ------------------------------------------------------
# @Time :      2021/1/14 15:21 
# @Author :    Neil.Jiang
# @project:    YiQiaUiTest
# @File :      config.py
# @Email :     jiang.nell@qq.com
# @Description: 
# @命名规范：文件名全小写+下划线，类名大写字母开头，方法和变量小写+下划线连接，常量大写

# -------------------------------------------------------


class CompanyConfig():
    """
    该类负责存储一些环境和角色的基本信息
    """
    @staticmethod
    def test_2151():
        browser = "chrome"
        url = "http://chat.rainbowred.com/login-page/v2/login.html?language=zh"
        username = "13778995041"
        password = "199566"
        company = "2151"
        return url, browser,username, password, company

    @staticmethod
    def online_521889():
        browser = "chrome"
        url = "http://e.echatsoft.com/login-page/v2/login.html?language=zh"
        username = "13778995041"
        password = "199566"
        company = "521889"
        return url, browser, username, password, company

    @staticmethod
    def online_524328():
        browser = "chrome"
        url = "http://e.echatsoft.com/login-page/v2/login.html?language=zh"
        username = "13778995041"
        password = "199566"
        company = "524328"
        return url, browser, username, password, company

    @staticmethod
    def online_524234():
        browser = "chrome"
        url = "http://e.echatsoft.com/login-page/v2/login.html?language=zh"
        username = "13778995041"
        password = "199566"
        company = "524234"
        return url, browser, username, password, company

    @staticmethod
    def online_521889_fire():
        browser = "firefox"
        url = "http://e.echatsoft.com/login-page/v2/login.html?language=zh"
        username = "13778995041"
        password = "199566"
        company = "521889"
        return url, browser, username, password, company

    @staticmethod
    def online_524234_fire():
        browser = "firefox"
        url = "http://e.echatsoft.com/login-page/v2/login.html?language=zh"
        username = "13778995041"
        password = "199566"
        company = "524234"
        return url, browser, username, password, company


class VisConfig:
    @staticmethod
    def online_521889():
        browser = "chrome"
        url = "https://www.echatsoft.com/visitor/pc/chat.html?companyId=521889"
        return url, browser,

    @staticmethod
    def online_524328(echatTag=''):
        browser = "chrome"
        if echatTag == '':
            url = "https://www.echatsoft.com/visitor/pc/chat.html?companyId=524328"
        else:
            url = "https://www.echatsoft.com/visitor/pc/chat.html?companyId=524328&echatTag=%s" % echatTag
        return url, browser,

    @staticmethod
    def online_521889_fire():
        browser = "firefox"
        url = "https://www.echatsoft.com/visitor/pc/chat.html?companyId=521889"
        return url, browser,


class CommonVariable:
        # 支持发送的文件类型
        SUPPORT_FILE_TYPE = ['.txt','.doc','.docx','.xls','.xlsx','.mp3','.mp4','.rar',
                     '.zip','.pdf','.log','.ppt','.avi','.jpg','.png','.gif','.jpeg','']

        warm_prompt = '不支持的文件类型\n' \
                      '支持类型：txt, doc, docx, xls, xlsx, amr, mp3, mp4, rar, zip, pdf, wav, log, mov, ppt, pptx, 3gp, aac, webm, ts, 3g2, 3gpp, 3gpp2, avi, m4v, mkv, ogg, psd, ai, ttf, aep, cdr, otf, vsp, prproj, c4d, jpg, png, gif, jpeg, webp, bmp'

