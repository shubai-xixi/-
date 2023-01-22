import requests
headers = {
    "User_Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55",
    "Authorization":"92d4ag27ofp3n8v5",
        }
res = requests.get('https://hgame.vidar.club/api/user/contest/3',headers=headers)
print(res.text)
