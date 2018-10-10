#coding:utf8
import xlrd
import os
from autobase.log import logger
class ResourceHelper(object):
    '''
    处理文件相关
    '''
    def __init__(self):
        self.current_path=os.path.dirname(os.path.abspath("."))
        logger.info(f'ResourceHelper 当前路径：{self.current_path}')

    def get_reource_path(self,resource_filename) ->str:
        '''
        获取文件路径
        :param resource_filename: 输入resource_file下的文件名
        :return: 文件绝对路径
        '''
        return self.current_path + "\\resource_file\\"+resource_filename

    def read_excel(self, excel_name, sheet_name="Sheet1") ->list:
        '''
        读取excel文件
        :param excel_name: resource_file目录下的文件名
        :param sheet_name: excel文件内的sheet名称
        :return: 当前excel-sheet页中数据list=[row1 data ,row2 data,....]
        '''
        workbook=xlrd.open_workbook(self.get_reource_path(excel_name))
        sheet1=workbook.sheet_by_name(sheet_name)
        row_all=sheet1.nrows
        all_data=[]
        for x in range(1,row_all):
            row_data=sheet1.row_values(x)
            all_data.append(row_data)
        return all_data

    def get_excel_date(self,excel_cell_data):
        '''
        将从excel中取到的日期数据转化成字符串，方便输入到输入框或者其他
        :param excel_cell_data: excel中日期 读取出来的 日期格式数据源
        :return:字符串的日期格式 年-月-日，待扩展更多格式
        '''
        __temp = xlrd.xldate_as_tuple(excel_cell_data, 0)
        return "{}-{}-{}".format(__temp[0], __temp[1], __temp[2])
