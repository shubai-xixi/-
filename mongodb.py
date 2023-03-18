#!/usr/bin/python3.11
# -*- coding: utf-8 -*-
# @Time    : 2023/2/17 14:54
# @Author  : Deathlingling
# @FileName: mongodb.py
# @Software: PyCharm
from pymongo import MongoClient
# 连本机mongodb（参数可不写）
# client = MongoClient(host='localhost', port=27017)
client = MongoClient()
# 获取所有数据库
dbs = client.list_database_names()
print(dbs)
