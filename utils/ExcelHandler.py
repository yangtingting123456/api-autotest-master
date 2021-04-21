#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'cd'
__data__ = '2021/4/11 17:10'

"""
处理Excel
"""
import xlrd
from conf import settings
from utils.LogHandler import logger


class ExcelOperate:
    def __init__(self, file_path, sheet_by_index=0):
        self.file_path = file_path
        self.sheet_by_index = sheet_by_index
        book = xlrd.open_workbook(self.file_path)
        self.sheet = book.sheet_by_index(self.sheet_by_index)

    def get_excel(self):
        """
        获取excel数据，定义title，将值与title拼接成字典返回
        :return:
        """
        title = self.sheet.row_values(0)
        data_list = [dict(zip(title, self.sheet.row_values(row))) for row in range(1, self.sheet.nrows)]
        logger().info("读取Excel成功,数据已返回")
        return data_list


if __name__ == '__main__':
    excel_data_list = ExcelOperate(settings.FILE_PATH, 0).get_excel()
