#coding:utf8
'''
配置浏览器驱动
'''
from selenium import webdriver
import os
import sys
from autobase.log import logger
from autobase.base_path import TOOLS_PATH
class StartBrowser(object):
    def __init__(self,driver_name="chrome"):
        '''
        初始化时默认使用chrome浏览器
        :param driver_name:浏览器类型名称：chrome，firefox，ie
        '''
        self.driver_name=driver_name
        # self.dir_path=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath("."))),"tools")
        self.dir_path=TOOLS_PATH
        logger.info('driver path：{}'.format(self.dir_path))
        print('driver path：{}'.format(self.dir_path))
        self.chrome_driver_path=os.path.join(self.dir_path,"chromedriver.exe")
        self.firefox_driver_path=os.path.join(self.dir_path,"geckodriver.exe")
        self.ie_driver_path = os.path.join(self.dir_path , "Iedriver.exe")
        sys.path.append(self.dir_path)
        self.start_browser()
    def start_browser(self):
        logger.info(f'启动浏览器：{self.driver_name}')
        if self.driver_name=="chrome":
            try:
                self.driver = webdriver.Chrome(self.chrome_driver_path)
            except Exception as e:
                logger.error(e)
                print(e)
        elif self.driver_name=='firefox':
            try:
                self.driver=webdriver.Firefox()
            except Exception as e:
                logger.error(e)
                print(e)
        elif self.driver_name=='ie':
            try:
                self.driver=webdriver.Ie(self.ie_driver_path)
            except Exception as e:
                logger.error(e)
                print(e)
        else:
            try:
                logger.info('启动默认Chrome')
                self.driver = webdriver.Chrome()
            except Exception as e:
                logger.error(e)
                print(e)
        self.driver.implicitly_wait(30)

