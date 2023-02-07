import json
import sqlite3
import requests
import time
import _thread
import multiprocessing
from multiprocessing import Pool

def fetch(qwer):
    url = f"https://zy.xywlapi.cc/qqcx2023?qq={qwer}"
    res = requests.get(url)
    text = res.text
    data = json.loads(text)
    print(qwer,data)
    if data['status'] == 200:
        conn = sqlite3.connect('账号')
        c = conn.cursor()
        sql = "SELECT * FROM zhxx WHERE qq="
        sql_l = sql+str(qwer)
        c.execute(sql_l)
        if c.fetchone() ==None:
            conn = sqlite3.connect('账号')
            c = conn.cursor()
            c.execute("INSERT INTO zhxx (shoujh,qq,weixin,weibo,lol,mima,guishudi) VALUES (?,?,?,?,?,?,?)",
                    (data['phone'], qwer, 'null', data['wb'], data['lol'], data['qqlm'], data['phonediqu']))
            conn.commit()
            conn.close()
        else:
            print("错误")

if __name__ == '__main__':
    asd=100410000
    zxc=100410000

    ii = [i for i in range(asd,zxc)]
    pool = Pool(processes=10)
    pool.map(fetch, ii)
    pool.close()
    pool.join()
    print("ok")
