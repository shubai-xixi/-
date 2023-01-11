import requests
import json
import xlwt
import time

workbook = xlwt.Workbook()
sheet = workbook.add_sheet("QQ信息")

qwer=1580527185
xxx=0
count = 0
zxc=0
print('qq   昵称    邮件 ')
while True:
    url = f"https://api.vvhan.com/api/qq?qq={qwer}"
    res = requests.get(url)
    text = res.text

    xxx=xxx+1
    print(xxx,qwer,res.text)
    qwer = qwer + 1
    data = json.loads(text)
    for each in range(0, 1):

        zxc = zxc + 1
        time.sleep(0.1)
        sheet.write(count, 0, zxc)  # row, column, value
        sheet.write(count, 1, qwer)
        sheet.write(count, 2, str(data['name']))
        sheet.write(count, 3, str(data['qemail']))
        count = count + 1
    workbook.save('QQ信息.xls')