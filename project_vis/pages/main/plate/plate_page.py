# -*- coding: utf-8 -*-
# @Project : Automation 
# @Time    : 2018/10/10 15:13
# @Author  : 
# @File    : plate_page.py
# @Software: PyCharm
from autobase.base_page import BasePage

class PlatePage(BasePage):
    '''版块管理'''
    plate_tab_xpath='//*[@id="app"]/div/div[2]/div[1]/div/ul/li[2]/a'

    def enter_plate_tab(self):
        self.logger.info('进入版块管理 tab页')
        self.get_element_by_xpath(self.plate_tab_xpath).click()