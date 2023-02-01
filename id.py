import uuid
import hashlib

def sha256hex(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode())
    res = sha256.hexdigest()
    # print(res)
    return res

def wyid():
    uid = uuid.uuid1()
    return uid.hex

def md5jm(djm):
    md5 = hashlib.md5()  # 应用MD5算法
    md5.update(djm.encode('utf-8'))
    # print(md5.hexdigest())
    return  md5.hexdigest()

# print(wyid())
# print(md5jm("74848"))