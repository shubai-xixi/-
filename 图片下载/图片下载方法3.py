import requests
asdf=1
url =f'https://images.weserv.nl/?url=https%3A%2F%2F23img.com%2Fi%2F2023%2F01%2F07%2Ficdyw5.jpg'
res = requests.get(url)
with open("%d.jpg" % asdf,'wb') as picture: #要读取二进制文件，如图片、视频等，要用'wb'模式写入文件
    picture.write(res.content)
    print('ok')