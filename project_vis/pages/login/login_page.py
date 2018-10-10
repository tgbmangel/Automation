# coding=utf-8

from autobase.base_page import BasePage
# 继承BasePage类
class LoginPage(BasePage):
    '''登录页'''
    # 定位器，通过元素属性定位元素对象
    login_input_name_xpath = '//*[@id="app"]/div/div/form/div[1]/div/div[1]/input'
    login_input_pwd_xpath = '//*[@id="app"]/div/div/form/div[2]/div/div[1]/input'
    login_button_xpath = '//*[@id="app"]/div/div/form/div[3]/div/button'

    # 输入用户名：调用send_keys对象，输入用户名
    def input_username(self, username):
        self.logger.info(f'输入用户名：{username}')
        self.get_element_by_xpath(self.login_input_name_xpath).clear()
        self.get_element_by_xpath(self.login_input_name_xpath).send_keys(username)

    # 输入密码：调用send_keys对象，输入密码
    def input_password(self, password):
        self.logger.info(f'输入密码：{password}')
        self.get_element_by_xpath(self.login_input_pwd_xpath).clear()
        self.get_element_by_xpath(self.login_input_pwd_xpath).send_keys(password)

    # 点击登录
    def click_login(self):
        self.logger.info(f'点击登录按钮')
        self.get_element_by_xpath(self.login_button_xpath).click()

