# -*- coding: utf-8 -*-
# @Project : Automation 
# @Time    : 2018/10/10 16:34
# @Author  : 
# @File    : a_add_page_test.py
# @Software: PyCharm
from project_vis.pages.main.page.page_page import PagePage
from project_vis.base_vis.vis_unittest import *
class AddPageTest(VisUnitTestCase):
    '''页面管理-添加页面'''
    def setUp(self):
        self.logger_self_class()
        self.url="http://{}/views/index.html#/main/page".format(self.host_manage_page)
        self.login_manage()
        self.page_name='自动测试页面'
        self.page_name_null_tip='请输入名称'
        self.page_page = PagePage(self.driver, self.url, '智慧城市运营管理系统')
        self.page_page.open()

    @record_func
    def test_vis_17(self):
        '''正常添加页面流程'''
        self.page_page.enter_page_tab()
        self.page_page.click_add_page_button()
        self.page_page.wait_time_second(0.5)
        self.page_page.input_page_name(self.page_name)
        self.page_page.save_page_name()
        self.page_page.wait_time_second(1)
        self.assertEqual(self.page_page.get_newest_page_name(),self.page_name)

    @record_func
    def test_vis_18(self):
        '''页面名称留空'''
        self.page_page.enter_page_tab()
        self.page_page.click_add_page_button()
        self.page_page.wait_time_second(0.5)
        self.page_page.save_page_name()
        self.page_page.wait_time_second(2)
        self.assertEqual(self.page_page.get_error_message(),self.page_name_null_tip)
        self.page_page.wait_time_second(2)



