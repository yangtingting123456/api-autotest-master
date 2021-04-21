# encoding: utf-8
'''
@file: mysql_utils.py
@author: chenduo
@contact: chenduo1@protonmail.com
@time: 2021/4/08 11:37
@desc:封装mysql函数用于业务使用
'''
__author__ = 'cd'
__data__ = '2021/4/11 17:10'
import os,pymysql
from utils.LogHandler import logger
from conf import settings
config = settings.DB_CONF
class MysqlOperate:

    def _get_index_dict(self,cursor):
        """
        获取数据库对应表中的字段名
        """
        index_dict = dict()
        index = 0
        for desc in cursor.description:
            index_dict[desc[0]] = index
            index = index + 1
        return index_dict

    def _get_dict_data_sql(self,cursor,data):
        """
        拼接结果，根据表中字段名，转化成dict格式（默认是tuple格式）
        """
        index_dict = self._get_index_dict(cursor)
        res = []
        for i in data:
            resi = dict()
            for j in index_dict:
                resi[j] = i[index_dict[j]]
            res.append(resi)
        return res

    def _public_mysql(self,sql):
        """
        增删改一致，所以封装一个私有函数
        """
        db = pymysql.connect(**config)
        cursor = db.cursor()
        try:
            # 执行sql
            cursor.execute(sql)
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()
        finally:
            cursor.close()

    def select_mysql(self,sql):
        """
        Sql查询
        """
        try:
            db = pymysql.connect(**config)
            cursor = db.cursor()
            logger().info("正在向{0}发送请求：{1}".format(config.get("host"),sql))
            cursor.execute(sql)
            message = self._get_dict_data_sql(cursor, cursor.fetchall())  # 入参1：sql对象，入参2：select返回结果
            db.commit()
            logger().info("{0}查询成功：{1}，结果是：{2}".format(config.get("host"), sql, message))
            return message
        except Exception as e:
            db.rollback()
            logger().warning("运行{0}-{1}方法时出现错误，错误代码：{}".format(config.get("host"), sql, e))
        finally:
            cursor.close()
            db.close()

    def insert_mysql(self,sql):
        """
        执行SQL，新增
        """
        logger().info("正在向{0}发送请求：{1}".format(config.get("host"), sql))
        self._public_mysql(sql)
        logger().info("{0}新增成功：{1}".format(config.get("host"), sql))

    def update_mysql(self,sql):
        """
        执行SQL，修改
        """
        logger().info("正在向{0}发送请求：{1}".format(config.get("host"), sql))
        self._public_mysql(sql)
        logger().info("{0}修改成功：{1}".format(config.get("host"), sql))

    def delete_mysql(self,sql):
        """
        执行SQL，删除
        """
        logger().info("正在向{0}发送请求：{1}".format(config.get("host"), sql))
        self._public_mysql(sql)
        logger().info("{0}删除成功：{1}".format(config.get("host"), sql))

    def exec_sql_file(self,sqlPath):
        """
        执行SQL文件，对数据初始化
        """
        db = pymysql.connect(**config)
        cursor = db.cursor()
        try:
            with open(u'../conf/{0}'.format(sqlPath), 'r+') as f:
                sql_list = f.read().split(';')[:-1]  # sql文件最后一行加上;
                sql_list = [x.replace('\n', ' ') if '\n' in x else x for x in sql_list]  # 将每段sql里的换行符改成空格
            ##执行sql语句，使用循环执行sql语句
            for sql_item in sql_list:
                print (sql_item)
                cursor.execute(sql_item)
        except BaseException as e:
            logger().warning("运行sql[{0}]时出现错误，错误代码：{1}".format(sql_item, e))
        finally:
            cursor.close()
            db.commit()
            db.close()

if __name__ == "__main__":
    sql = "select * from user"
    sql1 = "insert into user values('haha','11','cc','34','22')"
    sql2 = "delete from user where Sno = '哈哈'"
    sql3 = "update user set Sex = 'vv' where Sage = '22'"
    print(MysqlOperate().select_mysql(sql))
    # MysqlOperate().delete_mysql(sql2)
    # MysqlOperate().insert_mysql(sql)
    # MysqlOperate().update_mysql(sql3)
    MysqlOperate().exec_sql_file("init_Mysql_User2.sql")