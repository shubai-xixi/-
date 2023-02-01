import requests
from bs4 import BeautifulSoup
# 主站
url = 'https://www.jiepaig.com/'
# 模拟浏览器访问
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
# 发送请求
response = requests.get(url, headers=headers)
# 获取BeautifulSoup对象
print(response.text)
soup = BeautifulSoup(response.text, 'html.parser')
# 解析出符合要求的a标签
img_list = soup.find_all('img', {'class':'test'})
# 遍历标签
for img in img_list:
	# 获取img标签的src值
    src = img['src']
    print(src)
