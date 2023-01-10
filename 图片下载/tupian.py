import urllib.request
import  re

def getHtml(url):
    #urllib.request.urlopen 请求网站
    page=urllib.request.urlopen(url)
    html=page.read()#从刚请求中得到html内容
    #print(html)
    return html

def getImg(html):
    reg=r'src="(.+?\.jpeg)" height' #正则测试 or reg=r'src="(.+?\.jpg)" pic_ext
    #为了提升效率，先编译

    ireg=re.compile(reg)
    html=html.decode('utf-8') #转码
    imglist=re.findall(ireg,html)
    #保存到本地 1.jpg 2.jpg....
    x=1
    for imgurl in imglist:
        #保存图片到本目录 中
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)
        x+=1
        print(imgurl)