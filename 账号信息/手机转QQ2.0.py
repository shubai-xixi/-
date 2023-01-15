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
    qwer = 17542146462
    var = qwer + xxx
    url = f"https://zy.xywlapi.cc/qqphone?phone={var}" #接口1
    res = requests.get(url)
    text = res.text
    xxx = xxx + 1
    print(xxx,var,text)
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

# 中国电信 手机号码开头数字：133、153、180、181、189、177、173、149。

# 中国联通 手机号码开头数字：130、131、132、155、156、145、185、186、176、175。

# 中国移动 手机号码开头数字：1340、1348、135、136、137、138、139、150、151、152、157、158、159、182、183、184、187、188、147、178。
# 补充：
# 14号段以前为上网卡 专属号段，如中国联通的是145， 中国移动的是147等等。
# 虚拟运营商：170、1700、1701、1702电信、1703、1705、1706移动，1704、1707、1708、1709 联通，171联通。
# 卫星通信 ：1349。