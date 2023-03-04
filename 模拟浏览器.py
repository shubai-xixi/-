import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains

s = Service(r'E:\py\爬虫\venv\Scripts\msedgedriver.exe')  # 存储驱动所在路径
d = webdriver.Edge(service=s)  # 从路径提取驱动,设置驱动名为d
d.implicitly_wait(20)  # 设置每个步骤最大等待时间
d.get('https://search.jd.com/')  # GET方法访问
time.sleep(4)

ad = ActionChains(d)    # 行为链实例化，输入参数为驱动，
ad.perform()    # 行为开始执行的标识，必不可少！！！！！！
A = d.find_element('id', 'keyword').send_keys('AI')  # 定位元素A

time.sleep(4)
# ad = ActionChains(d)    # 实例化外部动作驱动
# ad.click(A).perform()   # 单击并执行
click = d.find_element('xpath', '/html/body/div[2]/form/input[4]')
click.click()

time.sleep(4)

js_button = 'document.documentElement.scrollTop=100000'
d.execute_script(js_button)
time.sleep(4)
jg=[]
mc=[]
nr=[]

def sdf(qwer):
    wz=f'//*[@id="J_goodsList"]/ul/li[{qwer}]/div'
    li_list=d.find_element('xpath',wz)
    print(li_list.text)
    a=li_list.find_element('xpath', './div[2]')
    jg.append(a.text)
for x in range(1,10):
    sdf(x)
print(jg)
