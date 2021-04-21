#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'cd'
__data__ = '2021/4/11 17:10'

import os
import datetime

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 测试数据execl默认配置
FILE_NAME = "news\shoutu\收徒版本-团队模块.xls"
FILE_NAME2 = "news\shoutu\收徒版本-活动模块.xls"
FILE_NAME3 = "news\shoutu\收徒版本-文章模块.xls"

FILE_PATH = os.path.join(BASE_DIR, "data", FILE_NAME)
FILE_PATH2 = os.path.join(BASE_DIR, "data", FILE_NAME2)
FILE_PATH3 = os.path.join(BASE_DIR, "data", FILE_NAME3)

# -----------初始化为template cookies dict---------
COOKIES_DICT = {}

# ------allure报告相关---------
ALLURE_COMMAND = "allure generate {from_json_path} -o {save_to_path} --clean".format(
    from_json_path=os.path.join(BASE_DIR, "report", "json_result"),
    save_to_path=os.path.join(BASE_DIR, "report", "allure_result")
)


# -----------邮件相关

# 第三方SMTP服务
MAIL_HOST = "smtp.feishu.cn"  # 设置服务器smtp.qq.com
MAIL_USER = "1233333@qq.com"  # 用户名
MAIL_TOKEN = "hhhhhhhhm"  # 授权码
# 设置收件人和发件人
SENDER = "1973927469@qq.com"
RECEIVERS = ["1973927469@qq.com", "xiangxiang@163.com"]  # 接收邮箱可以设置你的qq或者其它邮箱
# 邮件主题
THEME = "请查阅接口测试报告{0}".format(datetime.datetime.now().strftime("%Y-%m-%d"))
# 正文内容
SEND_CONTENT = "hi_all 这是本次接口测试报告结果。（解压后使用Edge浏览index.html）"
# 附件的file name
SEND_FILE_NAME = "allure_report{0}.zip".format(datetime.datetime.now().strftime("%Y-%m-%d"))

# 日志文件命令
# 日志级别
LOG_LEVEL = "debug"
LOG_STREAM_LEVEL = "debug"  # 屏幕输出流
LOG_FILE_LEVEL = "info"  # 文件输出流

# 日志文件命名
LOG_FILE_NAME = os.path.join(BASE_DIR, "logs", datetime.datetime.now().strftime("%Y-%m-%d") + ".log")

# 数据库链接串
DB_CONF = {
    'host': '192.168.60.4',
    'port': 63306,
    'user': 'cdmysql',
    'password': '123456',
    'db': 'jbt',
    'charset': 'utf8'
}

if __name__ == '__main__':
    print(FILE_PATH)
