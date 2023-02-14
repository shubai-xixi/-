import json
import requests


def fetch(qwer):
    url = f"https://zy.xywlapi.cc/qqcx2023?qq={qwer}"
    res = requests.get(url)
    text = res.text
    data = json.loads(text)
    if data['status'] == 200:
        print(qwer, data)
    else:
        print("不存在")
    fl()

def cxsj(qwer):
    url = f"https://zy.xywlapi.cc/qqphone?phone={qwer}"
    res = requests.get(url)
    text = res.text
    data = json.loads(text)
    if data['status'] == 200:
        print(qwer, data)
    else:
        print("不存在")
    fl()

def fl():
    shuru = int(input("输入查询: "))
    if 0 < shuru < 9999999999:
        fetch(shuru)

    elif 10000000000 < shuru < 99999999999:
        cxsj(shuru)
fl()