import json
import sqlite3
import requests
# c.execute("SELECT * FROM zhxx")
# print(c.fetchall())
a=""
qwer=31890
xxx = 0
count = 0
while True:
    url = f"https://zy.xywlapi.cc/qqcx2023?qq={qwer}"
    res = requests.get(url)
    text = res.text
    qwer = qwer + 1
    print(xxx, qwer, res.text)
    xxx=xxx+1
    data = json.loads(text)
    for each in range(0, 1):
        if data['status'] == 500:
            continue
        else:
            conn = sqlite3.connect('账号')
            c = conn.cursor()
            c.execute("INSERT INTO zhxx (shoujh,qq,weixin,weibo,lol,mima,guishudi) VALUES (?,?,?,?,?,?,?)",(data['phone'],qwer-1,a,data['wb'],data['lol'],data['qqlm'],data['phonediqu']))
            conn.commit()
            # 关闭连接
            conn.close()