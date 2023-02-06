import requests
from fake_useragent import UserAgent
from urllib import request
# while True:
#     url =f'https://www.dianping.com/citylist'
#
#     res = requests.get(url)
    # with open("" ,'wb') as picture: #要读取二进制文件，如图片、视频等，要用'wb'模式写入文件
    #     asdf=asdf+1
    #     picture.write(res.content)
url =f'https://www.dianping.com/citylist'
data={"UserAgent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Mobile Safari/537.36 Edg/109.0.1518.70"}
res = requests.get(url,headers=data)
print(res)