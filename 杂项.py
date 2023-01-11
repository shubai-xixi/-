import requests

mubiao = ('https://api.uomg.com/api/visitor.info?skey=1',
          'https://api.uomg.com/api/rand.qinghua?format=json',
          '',
          ''
          '')

def asdf(qwer):
    res = requests.get(mubiao[qwer])
    print(res.text)

while True:
    opq=int(input('ip地址  输入0\n'
                  '土味情话 输入1\n'
                  ''
                  '输入: '))
    asdf(opq)