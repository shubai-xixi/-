#@requests实战之肯德基.py

import requests
import json
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
kw = input("请输入要查询的城市名称")
param ={
'cname':'',
'pid': '',
'keyword': kw,
'pageIndex': '1',
'pageSize': '10'
}
response = requests.get(url=url,params=param,headers=headers)
page_text = response.text
with open('./kfc.text','w',encoding='utf-8') as fp:
    fp.write(page_text)


print("好了")