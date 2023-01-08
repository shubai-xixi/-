import requests
xxx=0
while True:
    qwer=17542129819  #修改手机号
    var = qwer + xxx
    url = f"https://zy.xywlapi.cc/qqphone?phone={var}"
    res = requests.get(url)
    xxx=xxx+1
    print(res.text)