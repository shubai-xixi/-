import requests
import json

while True:
    msg = input('我：')
    sess = requests.get('https://api.ownthink.com/bot?appid=9ffcb5785ad9617bf4e64178ac64f7b1&spoken=' + msg)
    data = json.loads(sess.text)
    print('人工智障：', data['data']['info']['text'])