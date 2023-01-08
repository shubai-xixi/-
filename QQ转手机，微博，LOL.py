import requests
import json
import xlwt
import time

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("QQ转手机号")

qwer=1580527199
xxx=0
count = 0
zxc=0
print('手机号  归属地  LOL  微博  QQ老密 ')
while True:
    url = f"https://zy.xywlapi.cc/qqcx2022?qq={qwer}"
    res = requests.get(url)
    text = res.text
    qwer=qwer+1
    xxx=xxx+1
    print(xxx,res.text)
    data = json.loads(text)
    for each in range(0, 1):
        if data['status'] == 500:
            continue
        else:
            zxc = zxc + 1
        time.sleep(0.1)
        sheet.write(count, 0, zxc)  # row, column, value
        sheet.write(count, 1, str(data['phone']))
        sheet.write(count, 2, str(data['phonediqu']))
        sheet.write(count, 3, str(data['lol']))
        sheet.write(count, 4, str(data['wb']))
        sheet.write(count, 5, str(data['qqlm']))
        count = count + 1
    workbook.save('QQ转数据.xls')