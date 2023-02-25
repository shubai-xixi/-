#!/usr/bin/python3.11
# -*- coding: utf-8 -*-
# @Time    : 2023/2/14 14:34
# @Author  : Deathlingling
# @FileName: 百度热搜.py
# @Software: PyCharm
import re
import time
from urllib.request import urlopen, Request

url='https://top.baidu.com/board?tab=realtime'
def request_html(url):
    headers={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 Edg/109.0.1518.70',
         }
    response = Request(url, headers=headers)
    res = urlopen(response)
    data = res.read().decode('utf-8')
    ist=re.findall(r'<span class="_38vEKmzrdqNxu0Z5xPExcg">(.*?)</span>',data,re.I|re.M|re.S)
    print(ist)
    time.sleep(10)

request_html(url)