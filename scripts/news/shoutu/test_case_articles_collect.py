# encoding: utf-8
'''
@file: test_case_articles_id.py
@author: chenduo
@contact: chenduo1@protonmail.com
@time: 2021/4/15 12:05
@desc:
'''
import pytest
import allure
import json
from utils.ExcelHandler import ExcelOperate
from utils.RequestsHandler import RequestsOperate
from conf import settings
from utils.LogHandler import logger

excel_data_list = ExcelOperate(settings.FILE_PATH3, 3).get_excel()# 读取xls用例，返回列表

class TestCase(object):
    @pytest.mark.parametrize("item", excel_data_list)  # 参数化的实现
    def test_case(self, item):
        logger().info("正在进行断言...")
        except_data, result = RequestsOperate(current_case=item, all_excel_data_list=excel_data_list).get_response_msg()
        allure.dynamic.title(item.get('title'))
        allure.dynamic.description(
            "<b style='color:red'>请求的url:</b>{0}<hr />"
            "<b style='color:red'>response预期值:</b>{1}<hr />"
            "<b style='color:red'>实际执行结果:</b>{2}<hr />"
            "<b style='color:red'>code预期值:</b>{3}<hr />"
            "<b style='color:red'>实际执行结果:</b>{4}<hr />".format(item["url"], item["except"], result,json.loads(item["except"]).get("code"),result.get("code"))
        )
        assert result.get("code") == json.loads(item["except"]).get("code")
        logger().info("完成断言,{0}-{1}".format(except_data, result))