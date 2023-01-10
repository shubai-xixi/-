import requests

qwer=1   #图片ID
asdf=1   #命名ID
zxcv=1   #运行

while qwer<376:
    url =f'https://www.woku361.com/suiji/jiepai/{qwer}.jpg'
    qwer=qwer+1
    res = requests.get(url)
    with open("%d.jpg" % asdf,'wb') as picture: #要读取二进制文件，如图片、视频等，要用'wb'模式写入文件
        asdf=asdf+1
        picture.write(res.content)
        print(qwer - 1, res,'已下载',zxcv,'张')
        zxcv=zxcv+1