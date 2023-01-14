import uuid
import hashlib

def sha256hex(data):
    sha256 = hashlib.sha256()
    sha256.update(data.encode())
    res = sha256.hexdigest()
    print("sha256加密结果:", res)
    return res
while True:

    uid = uuid.uuid1()
    print('uuid',uid.hex)
    md5 = hashlib.md5()  # 应用MD5算法
    data=uid.hex
    md5.update(data.encode('utf-8'))
    print('md5',md5.hexdigest())
    sha256hex(md5.hexdigest())
    input("回车键继续")




