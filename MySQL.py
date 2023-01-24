import pymysql
#测试需要

显示所有数据库='show databases;'
创建数据库='CREATE DATABASE `yhzl_sql`;'
删除数据库='DROP DATABASE `yhzl_sql`;'
选择数据库='USE `mysql`;'
查询表格='describe `yhzl_sql`;'

def show_databases(mingling):
    conn = pymysql.connect(host='',
                           user='',
                           password='')
    cursor = conn.cursor()
    cursor.execute(mingling)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    print(result)
show_databases(查询表格)