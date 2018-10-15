#coding:utf8
'''
将unittest封装，子类继承时不需要再去加载浏览器驱动
子类继承时，直接self.driver 进行使用驱动，且可以通过调用setup做用例初始化。
'''
import unittest
from common.browser_action import StartBrowser
from project_vis.pages.login.login_page import LoginPage
from time import sleep
import time
from autobase.log import logger
import inspect

def record_func(fn):
    def _wapper(*args):
        logger.info(f"record_func name:{fn.__name__} run...")
        logger.info(f"record_func doc:{fn.__doc__}")
        func = fn(*args)
        logger.info(f"record_func name:{fn.__name__} done...")
        return func
    return _wapper

class VisUnitTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.logger=logger
        cls.logger.info('unittest TestCase Start..............')
        cls.driver = StartBrowser().driver
        cls.host_manage_page= "10.16.4.37:8072"
        # cls.database_ip="10.16.4.57"
        # cls.database_db="wisdom_education_service_pre"
        # cls.database_user="postgres"
        # cls.database_pwd="aorise"
        # cls.ini_file="Config.ini"
        # cls.image_path=r'{}\resource_file\bd_logo1.png'.format(os.path.dirname(os.path.abspath(".")))
        # cls.pwd='12345678'
        cls.now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())

    @classmethod
    def tearDownClass(cls):
        sleep(5)
        cls.driver.quit()
        cls.logger.info('unittest TestCase finish,浏览器关闭。')
        pass

    def browser_driver(self):
        return self.driver

    def login_manage(self,user_name=u'admin',pwd='123456'):
        self.logger.info('自动登录 login_manage')
        url = "http://{}/views/index.html#/login".format(self.host_manage_page)
        loginpage = LoginPage(self.driver, url, "智慧城市运营管理系统")
        loginpage.open()
        sleep(3)
        # 目前登录框会自动加载一个用户名和密码，正常需要输入特定账号进行测试
        self.logger.info(f'登录信息：{url}，{user_name},{pwd}')
        loginpage.input_username(user_name)
        loginpage.input_password(pwd)
        loginpage.click_login()
        sleep(2)
        loginpage.fresh_page()
        self.logger.info('自动登录，完成。')
    def logger_self_class(self):
        self.logger.info(f'current testcase: {self.__class__.__name__}')
