import random
import requests

proxy = {
    'http':'112.250.107.37:53281'
}

url = 'https://www.ip138.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
}
response = requests.get(url=url,headers=headers,proxies=proxy)
with open('ip.html','w',encoding='utf-8') as f:
    f.write(response.text)
