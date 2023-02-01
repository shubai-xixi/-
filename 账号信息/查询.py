import sqlite3

def cx():
    shuru=int(input("输入查询: "))
    if 0 < shuru < 9999999999:
        conn = sqlite3.connect('账号')
        c = conn.cursor()
        # c.execute("SELECT * FROM zhxx")
        # print(c.fetchall())
        sql = "SELECT * FROM zhxx WHERE qq="
        sql_l = sql+str(shuru)
        c.execute(sql_l)
        print(c.fetchone())

    elif 10000000000 < shuru < 99999999999:
        conn = sqlite3.connect('账号')
        c = conn.cursor()
        sql = "SELECT * FROM zhxx WHERE shoujh="
        sql_l = sql + str(shuru)
        c.execute(sql_l)
        print(c.fetchone())

    else:
        print("错误")
    cx()
cx()
