#requests实战之豆瓣电影.py


import requests
import json

headers ={    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
}
url = "https://movie.douban.com/j/chart/top_list"
param ={
'type': '24',
'interval_id': '100:90',
'action':'',
'start': '40',
'limit': '20'
}
response = requests.get(url=url,params=param,headers=headers)
list_data = response.json()
fp =open('./douban.json','w',encoding='utf-8')
json.dump(list_data,fp=fp,ensure_ascii=False)
fp.close()
print("好了")
