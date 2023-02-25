import requests
fgh=[]

def shuru(daili):
    proxies = {
        'https':daili
               }
    url = "http://www.baidu.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    try:
        response = requests.get(url, headers=headers, proxies=proxies, timeout=5)
        print(response)

    except Exception as e:
        print(f"请求失败，代理IP无效！{e}")
    else:
        print("请求成功，代理IP有效！")
        fgh.append(daili)

with open("IP.txt") as file:
    for item in file:
        print(item)
        shuru(item)
print(fgh)
