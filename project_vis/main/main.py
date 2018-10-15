# coding:cp936
'''
执行用例的主程序
'''
from autobase import HTMLTestRunner
import unittest
import os
import sys
from autobase.log import logger
from project_vis.base_vis.vis_path import TESTCASES_PATH,REPORT_FILE_PATH

if __name__=="__main__":
    #用例文件目录
    logger.info(f'\nWEB UI 自动化启动:{__file__} ')
    testcase_dir=TESTCASES_PATH
    logger.info(f'获取 {testcase_dir} 下的用例')
    # testcase_dir="../testcases/a_login_cases/"
    #用例文件后缀
    partern_file='*_test.py'
    logger.info(f'获取用例文件名匹配 【{partern_file}】')
    suiteTest=unittest.defaultTestLoader.discover(testcase_dir,pattern=partern_file)
    # logger.info(f'获取到testcases：{suiteTest}')
    report_file_name = os.path.basename(__file__)[:-3]
    filePath = os.path.join(REPORT_FILE_PATH,f'{report_file_name}.html')
    logger.info(f'报告文件地址：{filePath}')
    fp = open(filePath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='{} TestReport'.format(report_file_name),
        description='This is {} Report'.format(report_file_name)
    )
    logger.info('runner run...')
    runner.run(suiteTest)