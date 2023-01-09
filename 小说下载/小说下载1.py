import re
import requests

qwer=41080  #书id
asdf=1   #命名ID
zxcv=1   #运行

while True:
    url =f'https://yueliangwz40.buzz/{qwer}.html'
    qwer=qwer+1
    res = requests.get(url)
    res.encoding = 'ISO-8559-1'
    print(res)
    if res.status_code == 404:
        continue
    else:
        qqq=re.findall(r"<title.*?>(.+?)</title>", res.text)
        asdf=asdf+1
        with open('%s.html'% qqq, 'wb') as picture:  # 要读取二进制文件，如图片、视频等，要用'wb'模式写入文件
            picture.write(res.content)
            print('ok')
            print(qwer - 1, res,'已下载',zxcv,'章')
            zxcv=zxcv+1