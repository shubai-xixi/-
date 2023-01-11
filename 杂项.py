import requests

mubiao = ('https://api.uomg.com/api/visitor.info?skey=1',
          'https://api.uomg.com/api/rand.qinghua?format=json',
          'https://api.vvhan.com/api/song?txt={as}',
          ''
          '')

def asdf(qwer):
    res = requests.get(mubiao[qwer])
    print(res.text)


opq=int(input('ip地址          输入0\n'
                '土味情话         输入1\n'
                '文字转语音        输入2\n'
                  '                 输入: '))

asdf(opq)