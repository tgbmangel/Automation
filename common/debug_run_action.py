#coding:utf8
from autobase import HTMLTestRunner
import unittest
from autobase.log import logger
import os

class DebugRunTest(object):
    def __init__(self,report_file_name):
        logger.info('DebugRunTest run')
        self.suiteTest = unittest.TestSuite()
        self.report_file_name = report_file_name
        filePath = "../reports/{}.html".format(self.report_file_name)
        fp = open(filePath, 'wb')
        self.runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='{} TestReport'.format(self.report_file_name),
                                                    description='This is {} Report'.format(self.report_file_name))

    def run(self):
        self.runner.run(self.suiteTest)

'''
# copy以下内容到需要单个文件执行的下方：
#unittest 加入TestSuite后，对用例进行管理执行，以下代码用作单文件调试，可不写。↓
if __name__ == "__main__":
    from common.debug_run_action import DebugRunTest
    import os
    report_file_name = os.path.basename(__file__)[:-3]
    a=DebugRunTest(report_file_name)
    a.suiteTest.addTest(Caselogin("test_case1")) #test_case替换成类中的testcase名称，多行需要手动添加
    a.suiteTest.addTest(Caselogin("test_case2")) 
    ...
    ...
    a.suiteTest.addTest(Caselogin("test_case")) 
    a.run()
'''
