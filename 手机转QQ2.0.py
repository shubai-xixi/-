import requests
import json
import xlwt
import time

count = 0
xxx = 0
zxc=0

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("手QQ")
while True:
    qwer = 17542130567
    var = qwer + xxx
    url = f"https://zy.xywlapi.cc/qqphone?phone={var}" #接口1
    res = requests.get(url)
    text = res.text
    xxx = xxx + 1
    print(xxx,qwer,text)
    data = json.loads(text)
    for each in range(0, 1):
        if data['status'] == 500:
            continue
        else:
            zxc=zxc+1
            time.sleep(0.1)
            sheet.write(count, 0, zxc)
            sheet.write(count, 1, str(data['qq']))
            sheet.write(count, 2, str(data['']))
            sheet.write(count, 3, str(data['phonediqu']))
            count = count + 1
    workbook.save('手机转QQ数据.xls')