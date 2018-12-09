# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 20:02
# @Author  : Torre
# @Email   : klyweiwei@163.com
# Description ：connect to database, return cursor and conn

import json
import pymysql
import random
import string
import os
import logging


class ConnectDatabase:
    # def __init__(self, cur):
    #     self.cur = cur

    # def get_conf(self, file='databases_conf.json'):
    def get_conf(self, file):
        with open(file, "r", encoding="utf-8") as f:
            conf = json.load(f)
        return conf

    def connect_db(self, host, user, password, db, port):
        conn = pymysql.connect(host, user, password, db, port, charset="utf8")  # 最好加上utf-8
        cur = conn.cursor()
        return conn, cur

    # 获取数据库 的表, 并存储到list中
    def getTabs(self, cur):
        sql = 'show tables'
        cur.execute(sql)
        res = cur.fetchall()
        saveTabs = []
        for tab in res:
            tab = tab[0]
            saveTabs.append(tab)
        # print(saveTabs)
        return saveTabs

    # 获取列
    def get_cols(self, table, cur):
        sql = 'desc ' + str(table) + ''
        cur.execute(sql)
        res = cur.fetchall()
        return res

    # 执行sql, 返回结果
    def get_res(self, cur, sql):
        cur.execute(sql)
        res = cur.fetchall()
        return res

    # 数据的提交
    def get_fetch(self, conn, cur, sql):
        cur.execute(sql)
        conn.commit()

    # 数据库关闭
    def disconnect_db(self, conn, cur):
        cur.close()
        conn.close()









        




