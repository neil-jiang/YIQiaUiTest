# -*- coding: utf-8 -*-# 
# ------------------------------------------------------
# @Time :      2021/1/19 15:53 
# @Author :    Neil.Jiang
# @project:    YiQiaUiTest
# @File :      test.py
# @Email :     jiang.nell@qq.com
# @Description: 
# @命名规范：文件名全小写+下划线，类名大写字母开头，方法和变量小写+下划线连接，常量大写

# -------------------------------------------------------

from PIL import Image
import math
import operator
from functools import reduce
import base.config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# for each in range(1,6):
#     print(each)
# driver = webdriver.Chrome()
# driver.get("http://www.baidu.com")
# driver.maximize_window()
# pre_ele = driver.find_element_by_css_selector("span.bg.s_ipt_wr")
# driver.find_element_by_css_selector("#kw").send_keys("12")
# # ele = WebDriverWait(driver,timeout=10).until(lambda x:pre_ele.find_elements_by_css_selector("#kw"))
#
# driver.find_element_by_link_text("12")
if __name__ == '__main__':

    a = 1
    b = [1,2,3,4,5]
    assert b.count(a) == 2
    print(base.config.CompanyConfig().online_521889()+base.config.VisConfig().online_521889())