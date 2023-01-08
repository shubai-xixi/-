import requests
import xlwt
import time

count = 0
xxx = 0

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("QQ")
while True:
    qwer = 17542130567
    var = qwer + xxx
    url = f"https://zy.xywlapi.cc/qqphone?phone={var}"
    res = requests.get(url)
    xxx = xxx + 1
    print(res.text)
    for each in range(0, 1):
        time.sleep(0.1)
        sheet.write(count, 0, str(res.text))  # row, column, value
        count = count + 1
    workbook.save('手机QQ数据.xls')