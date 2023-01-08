import json
import time
from pymongo.database import Database
from pymongo.collection import Collection
import pymongo
from lxml import etree
from selenium import webdriver


def get_html(url):
    browser = webdriver.Chrome()
    browser.get(url)
    if browser.current_url == url:
        js = "var q=document.documentElement.scrollTop=100000"
        browser.execute_script(js)
        time.sleep(2)
        responses = browser.page_source
        browser.close()
        return responses
    else:
        with open('cookies.txt', 'r', encoding='utf8') as f:
            listCookies = json.loads(f.read())
        for cookie in listCookies:
            cookie_dict = {
                'domain': '.jd.com',
                'name': cookie.get('name'),
                'value': cookie.get('value'),
                "expires": '1629446549',
                'path': '/',
                'httpOnly': False,
                'HostOnly': False,
                'Secure': False
            }
            browser.add_cookie(cookie_dict)
        time.sleep(1)
        browser.get(url)
        js = "var q=document.documentElement.scrollTop=100000"
        browser.execute_script(js)
        time.sleep(2)
        responses = browser.page_source
        browser.close()
        return responses


def parser(responses):
    res = etree.HTML(responses)
    li_list = res.xpath('//*[@id="J_goodsList"]/ul/li')
    info = []
    for li in li_list:
        title = li.xpath('./div/div[4]/a/em//font/text()')[0]
        all_title = li.xpath('./div/div[4]/a/em/text()')
        all_title = title + process_list(all_title)
        price = li.xpath('./div/div[3]/strong/i/text()')[0]
        shop = li.xpath('./div/div[7]/span/a/text()')
        comment_num = li.xpath('./div/div[5]/strong/a/text()')
        discount = li.xpath('./div/div[8]/i/text()')
        print(all_title, price, shop, comment_num, discount)
        a = {'title': all_title, 'price': price, 'shop': shop, 'comment_num': comment_num, 'discount': discount}
        info.append(a)
    return info


def save_info_to_mongo(info):
    client = pymongo.MongoClient('localhost', 27017)
    collection = Collection(Database(client, 'Jingdong'), 'huawei P50')
    for info in info:
        collection.insert_one(info)
    client.close()


def process_list(lists):
    a = ''
    for i in lists:
        b = i.replace('\n', '').replace('【', '').replace('】', '').replace('-', '')
        a += b
    return a


if __name__ == '__main__':
    #url编码改
    base_url = 'https://search.jd.com/Search?keyword=%E5%8D%8E%E4%B8%BAp50&qrst=1&suggest=3.def.0.base&wq=%E5%8D%8E%E4%B8%BAp50&ev=exbrand_%E5%8D%8E%E4%B8%BA%EF%BC%88HUAWEI%EF%BC%89%5E&pvid=ddb6b5344d4c452496da22357a030be8&page={}'
    url_list = [base_url.format(i) for i in range(1, 20, 2)]
    for page_url in url_list:
        save_info_to_mongo(parser(get_html(page_url)))
