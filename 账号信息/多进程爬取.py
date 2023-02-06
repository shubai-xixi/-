import json
import sqlite3
from multiprocessing import Pool
import requests

def fetch(qwer):
    url = f"https://zy.xywlapi.cc/qqcx2023?qq={qwer}"
    res = requests.get(url)
    text = res.text
    data = json.loads(text)
    if data['status'] == 200:
        conn = sqlite3.connect('账号')
        c = conn.cursor()
        sql = "SELECT * FROM zhxx WHERE qq="
        sql_l = sql + str(qwer)
        c.execute(sql_l)
        if c.fetchone() == None:
            print(qwer)
            conn = sqlite3.connect('账号')
            c = conn.cursor()
            c.execute("INSERT INTO zhxx (shoujh,qq,weixin,weibo,lol,mima,guishudi) VALUES (?,?,?,?,?,?,?)",
                      (data['phone'], qwer, '', data['wb'], data['lol'], data['qqlm'], data['phonediqu']))
            conn.commit()
            conn.close()
        else:
            print('已录入')
            conn.commit()
            conn.close()

if __name__ == '__main__':
    asd = 1001640000
    zxc = 1001650000
    ii = [i for i in range(asd, zxc)]
    pool = Pool(processes=32)
    pool.map(fetch, ii)
    pool.close()
    pool.join()
    print("ok")
