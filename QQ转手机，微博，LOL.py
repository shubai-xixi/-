import time
import xlwt
import requests

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("手机号")
qwer=1580527186
xxx=0
count = 0
while True:
    url = f"https://zy.xywlapi.cc/qqcx2022?qq={qwer}"
    res = requests.get(url)
    qwer=qwer+1
    xxx=xxx+1
    print(xxx,res.text)
    for each in range(0, 1):
        time.sleep(0.1)
        sheet.write(count, 0, str(xxx))  # row, column, value
        sheet.write(count, 1, str(res.text))
        count = count + 1
    workbook.save('手机号数据.xls')