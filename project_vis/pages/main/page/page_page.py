# -*- coding: utf-8 -*-
# @Project : Automation 
# @Time    : 2018/10/10 16:27
# @Author  : 
# @File    : page_page.py
# @Software: PyCharm
from autobase.base_page import BasePage

class PagePage(BasePage):
    '''版块管理'''
    page_tab_xpath='//*[@id="app"]/div/div[2]/div[1]/div/ul/li[1]/a'
    add_page_button_xpath='//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/button'
    page_name_input_xpath='//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/form/div/div/div[1]/input'
    page_name_tip_xpath='//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/form/div/div/div[2]'
    page_name_sure_button_xpath='//*[@id="app"]/div/div[2]/div[2]/div/div/div[2]/div/div/div[3]/div/button[2]'
    page_list_xpath='//*[@id="app"]/div/div[2]/div[2]/div/div/div[3]/div[1]/div[3]/table/tbody/tr/td/div/span'
    page_name_xpath='td/div/span'
    def enter_page_tab(self):
        self.logger.info('进入 页面管理tab页')
        self.get_element_by_xpath(self.page_tab_xpath).click()

    def click_add_page_button(self):
        self.logger.info('点击 添加页面 按钮')
        self.get_element_by_xpath(self.add_page_button_xpath).click()

    def input_page_name(self,page_name):
        self.logger.info(f'输入页面名称：{page_name}')
        self.get_element_by_xpath(self.page_name_input_xpath).send_keys(page_name)
    def get_error_message(self):
        self.logger.info(f'获取错误提示信息')
        self.logger.info(self.get_element_by_xpath(self.page_name_tip_xpath).text)
        return self.get_element_by_xpath(self.page_name_tip_xpath).text
    def save_page_name(self):
        self.logger.info('点击 确定 按钮')
        self.get_element_by_xpath(self.page_name_sure_button_xpath).click()
    def get_newest_page_name(self):
        self.logger.info(f'获取页面管理列表第一个名称：{self.get_element_by_xpath(self.page_list_xpath).text}')
        return self.get_element_by_xpath(self.page_list_xpath).text