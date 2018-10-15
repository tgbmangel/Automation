# coding:cp936
'''
ִ��������������
'''
from autobase import HTMLTestRunner
import unittest
import os
import sys
from autobase.log import logger
from project_vis.base_vis.vis_path import TESTCASES_PATH,REPORT_FILE_PATH

if __name__=="__main__":
    #�����ļ�Ŀ¼
    logger.info(f'\nWEB UI �Զ�������:{__file__} ')
    testcase_dir=TESTCASES_PATH
    logger.info(f'��ȡ {testcase_dir} �µ�����')
    # testcase_dir="../testcases/a_login_cases/"
    #�����ļ���׺
    partern_file='*_test.py'
    logger.info(f'��ȡ�����ļ���ƥ�� ��{partern_file}��')
    suiteTest=unittest.defaultTestLoader.discover(testcase_dir,pattern=partern_file)
    # logger.info(f'��ȡ��testcases��{suiteTest}')
    report_file_name = os.path.basename(__file__)[:-3]
    filePath = os.path.join(REPORT_FILE_PATH,f'{report_file_name}.html')
    logger.info(f'�����ļ���ַ��{filePath}')
    fp = open(filePath, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title='{} TestReport'.format(report_file_name),
        description='This is {} Report'.format(report_file_name)
    )
    logger.info('runner run...')
    runner.run(suiteTest)