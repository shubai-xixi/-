import re
import requests

qwer=1  #书id
asdf=1   #命名ID
zxcv=1   #运行

while True:
    url =f'https://yueliangwz40.buzz/{qwer}.html'
    qwer=qwer+1
    res = requests.get(url)
    res.encoding = 'UTF-8'
    if res.status_code == 200:
        nr = re.findall('<p>(.+?)</p>', res.text)
        qqq = re.findall('<title.*?>(.+?)</title>', res.text)
        asdf = asdf + 1
        list = qqq[0]
        with open('%s.txt' % list, 'wb') as picture:  # 要读取二进制文件，如图片、视频等，要用'wb'模式写入文件
            picture.write(nr)
            print('ok')
            print(qwer - 1, res, '已下载', zxcv, '章')
            zxcv = zxcv + 1
    else:
        continue