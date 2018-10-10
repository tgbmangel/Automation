# -*- coding: utf-8 -*-
# @Project : POM_demo 
# @Time    : 2018/5/29 17:36
# @Author  : 
# @File    : database_action.py
# @Software: PyCharm Community Edition
import psycopg2
from autobase.log import logger
class PostgreSQL_Connect():
    def __init__(self,database,user,password,host,port='5432'):
        self.database=database
        self.user=user
        self.password=password
        self.host=host
        self.port=port
        try:
            logger.info(f'尝试连接数据库：库：{self.database},用户：{self.user},密码：{self.password},host:{host=self.host},port:{self.port}')
            self.conn = psycopg2.connect(database=self.database,
                                    user=self.user,
                                    password=self.password,
                                    host=self.host,
                                    port=self.port)
            logger.info('connect success!')
            print('connect success!')
        except psycopg2.DatabaseError as e:
            logger.error(e)
            exit(e)
        except Exception as e:
            logger.error(e)
            exit(e)

    def executesql(self,sql) ->list:
        logger.info(f'执行sql：{sql}')
        try:
            __cur=self.conn.cursor()
            __cur.execute(sql)
            __results=__cur.fetchall()
            return __results
        except Exception as e:
            logger.error(e)

    def close_connection(self):
        self.conn.close()
        print('connection closed!')
        logger.info('connection closed!')

