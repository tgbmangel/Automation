# coding=utf-8
from time import sleep
from project_vis.pages.login.login_page import LoginPage
from project_vis.base_vis.vis_unittest import VisUnitTestCase
class Caselogin(VisUnitTestCase):
    '''登录测试'''
    def setUp(self):
        ''' 教育网页-登录页测试用例 '''
        self.url = "http://{}/views/index.html#/login".format(self.host_manage_page)
        self.username = u"admin"
        self.password = "123456"
    def test_login(self):
        '''正常登录'''
        loginpage=LoginPage(self.driver, self.url, "智慧城市运营管理系统")
        loginpage.open()
        sleep(3)
        loginpage.input_username(self.username)
        loginpage.input_password(self.password)
        #loginpage.click_submit()
        sleep(3)
        loginpage.click_login()
        sleep(3)
        self.assertEqual(loginpage.page_current_url_page()[0], f'http://{self.host_manage_page}/views/index.html#/main/page')
        self.logger.info('test_login 完成')

#unittest 加入TestSuite后，对用例进行管理执行，以下代码用作单文件调试，可不写。↓

if __name__ == "__main__":
    from common.debug_run_action import DebugRunTest
    import os
    report_file_name = os.path.basename(__file__)[:-3]
    a=DebugRunTest(report_file_name)
    a.suiteTest.addTest(Caselogin("test_login"))
    a.run()