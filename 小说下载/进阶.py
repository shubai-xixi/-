#!/usr/bin/python3.11
# -*- coding: utf-8 -*-
# @Author  : Deathlingling
# @Software: PyCharm
# @file: 进阶.py
# @time: 2023/3/4 19:37
import urllib.request,lxml.html

bt=[]
wz=[]

def paqu(shuzi):
    url = f'https://yueliangwz59.buzz/page/{shuzi}'
    html = urllib.request.urlopen(url).read()
    tree = lxml.html.fromstring(html)
    content = tree.cssselect('body>div>main>div>div>div>ul>li>div>div>h2>a')
    #/html/body/div/main/div/div/div/ul
    for n in content:
        link = n.get('href')
        tag = n.text
        print(tag,link)
        bt.append(tag)
        wz.append(link)
    print("主页面抓取成功")

for qw in range(2,46):
    paqu(qw)

def zhuneirong(url):
    html = urllib.request.urlopen(url).read()
    tree = lxml.html.fromstring(html)
    content = tree.cssselect('body>div>main>div>div>div>ul>li>div>div>h2>a')
    #/html/body/div/main/div/div/div/ul
    for n in content:
        link = n.get('href')
        tag = n.text
        print(tag,link)
        bt.append(tag)
        wz.append(link)
    print("主页面抓取成功")