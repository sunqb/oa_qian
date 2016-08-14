#!/usr/bin/env python
# -*- coding: utf-8 -*-

'mysql工具类'

__author__ = 'sunqb'

import sys
import mysql.connector
import time

# 编码
reload(sys)
sys.setdefaultencoding('utf-8')


class Util_mysql:
    def __init__(self):
        self.conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='root',
                                            database='pmysql', use_unicode=True)
        self.cursor = self.conn.cursor()

    # 保存签到记录到数据库
    def saveRecord(self, username, signtype):
        vsql = '''insert into t_oa_record(username, signtype, addtime) values(%s, %s, %s)'''
        self.cursor.execute(vsql, [username, signtype, self.getTime()])
        self.conn.commit()

    # 关闭连接
    def closeconn(self):
        self.cursor.close()
        self.conn.close()

    # 获取当前时间
    def getTime(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

    # 查询签到记录
    def queryRecord(self, username):
        vsql = '''select * from t_oa_record where username = %s order by id desc'''
        self.cursor.execute(vsql, [username])
        results = self.cursor.fetchall()
        return results
