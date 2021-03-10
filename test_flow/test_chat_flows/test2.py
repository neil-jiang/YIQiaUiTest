# -*- coding: utf-8 -*-# 
# ------------------------------------------------------
# @Time :      2021/3/1 17:41 
# @Author :    Neil.Jiang
# @project:    YiQiaUiTest
# @File :      test2.py
# @Email :     jiang.nell@qq.com
# @Description: 
# @命名规范：文件名全小写+下划线，类名大写字母开头，方法和变量小写+下划线连接，常量大写

# -------------------------------------------------------
from base.config import CompanyConfig
from base.config import VisConfig
import os
from selenium import webdriver
import json
import openpyxl
from base.base import OpExcel
from PIL import Image
import requests
import time

driver = webdriver.Chrome()
driver.get("https://www.baidu.com/")

print(driver.get_cookies())
a =driver.execute_script("return document.cookie;")
print(a)