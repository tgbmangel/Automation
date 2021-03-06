# -*- coding: utf-8 -*-
# @Project : upupup 
# @Time    : 2018/9/18 16:43
# @Author  : 
# @File    : logs.py
# @Software: PyCharm
import logging.handlers
import datetime
import os
from autobase.base_path import LOG_PATH,PROJECT_NAME
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
# handler = logging.FileHandler("logs/news.log",encoding='utf-8')
handler =logging.handlers.TimedRotatingFileHandler(
    os.path.join(LOG_PATH,f"{PROJECT_NAME}.log"),
    encoding='utf-8',
    when='midnight',
    interval=1,
    backupCount=7,
    atTime=datetime.time(0, 0, 0, 0)
)
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s')
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
logger.addHandler(handler)
