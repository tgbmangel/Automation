# -*- coding: utf-8 -*-
# @Project : Automation 
# @Time    : 2018/10/10 15:17
# @Author  : 
# @File    : plate_test.py
# @Software: PyCharm

from project_vis.pages.main.plate.plate_page import PlatePage
from project_vis.base_vis.vis_unittest import *

class PlatePageTest(VisUnitTestCase):
    '''版块管理页面'''
    def setUp(self):
        self.logger_self_class()
        self.url="http://{}/views/index.html#/main/page".format(self.host_manage_page)
        self.login_manage()
        self.plate_page = PlatePage(self.driver, self.url, '智慧城市运营管理系统')

    @record_func
    def test_page_state(self):
        '''版块管理-页面url地址验证'''
        self.plate_page.enter_plate_tab()
        self.plate_page.wait_time_second(3)
        self.assertEqual(self.plate_page.page_current_url_page()[0], f'http://{self.host_manage_page}/views/index.html#/main/plate/')
        self.logger.info('test_page_state 完成')