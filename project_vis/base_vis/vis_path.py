# -*- coding: utf-8 -*-
# @Project : Automation 
# @Time    : 2018/10/9 16:15
# @Author  : 
# @File    : vis_path.py
# @Software: PyCharm

import os
# print(__file__)
# print(os.path.dirname(os.path.dirname(__file__)))
VIS_PROJECT_PATH=os.path.dirname(os.path.dirname(__file__))
TESTCASES_PATH=os.path.join(VIS_PROJECT_PATH,'testcases')
REPORT_FILE_PATH=os.path.join(VIS_PROJECT_PATH,'reports')
if not os.path.exists(REPORT_FILE_PATH):
    os.makedirs(REPORT_FILE_PATH)