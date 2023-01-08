import json
import os
import re
import time
from datetime import datetime
from time import sleep
import click
import pandas as pd
import requests
from bs4 import BeautifulSoup


class TengXunDocument():

    def __init__(self, document_url, local_pad_id, cookie_value):
        # excel文档地址
        self.document_url = document_url
        # 此值每一份腾讯文档有一个,需要手动获取
        self.localPadId = local_pad_id
        self.headers = {
            'content-type': 'text/html; charset=utf-8',
            'Cookie': 'pgv_pvid=1041635916; pac_uid=0_f2d05cc871bf7; RK=wsF9kD1UHS; ptcz=9d9f3c77379dddf000f547023a5e1df0e3f088094cc39682b2e8118c1090af9a; tvfe_boss_uuid=0e9b46f7e11eb26c; pgv_info=ssid=s9519869733; vversion_name=8.2.95; video_omgid=915bf187884dbd60; traceid=bd42f2d10e; TOK=bd42f2d10ed9fcd3; hashkey=bd42f2d1; fingerprint=19313025df9842c6833697475429364c59; ES2=77988b2337f4e040; backup_cdn_domain=docs.gtimg.com; optimal_cdn_domain=docs2.gtimg.com; low_login_enable=1; CheckKey=4e7a8a2d0f758fa6ffd94a2bXMoDp1; wx_appid=wxd45c635d754dbf59; openid=oDzL40AUwoxqOh-DwB-y9zJXAo5c; access_token=64_byyh0Ny4m0Pk9RN0gVHX0iLHlkp-n-mR9BU-o0NgOGKKF2T3cD_SXWPDOknpO0MbEjieZ6QZfvH2qxaAgtlKuKfKPV7QZLrEUBm2Q-V-67I; refresh_token=64_wP8kW5agvY6nTO0-yHX5E2aJIVjbj3KnqsWW3ZgosY77uuW20AUoq8JY2-Pm9OdNTk0ZnYkdmbVJ3DgoQMBBh6hg-6MJ0AtAE0IkJBmexZ8; DOC_SID=bb892b76257f497bb35fba82b78fc355683a7c1fadd94480a7e73f23e4f0ceb0; SID=bb892b76257f497bb35fba82b78fc355683a7c1fadd94480a7e73f23e4f0ceb0; loginTime=1673017905964'
        }

    def get_now_user_index(self):
        """
        # 获取当前用户信息,供创建下载任务使用
        :return:
            nowUserIndex = '04eda8a41aaaf6e0317ad8632ec74cd7'
            # uid = '144115225804776585'
            # utype = 'wx'
        """
        response_body = requests.get(url=self.document_url, headers=self.headers, verify=False)
        parser = BeautifulSoup(response_body.content, 'html.parser')
        global_multi_user_list = re.findall(re.compile('window.global_multi_user=(.*?);'), str(parser))
        if global_multi_user_list:
            user_dict = json.loads(global_multi_user_list[0])
            print(user_dict)
            return user_dict['nowUserIndex']
        return 'cookie过期,请重新输入'

    def export_excel_task(self, export_excel_url):
        """
        导出excel文件任务,供查询文件数据准备进度
        :return:
        """
        body = {
            'docId': self.localPadId, 'version': '2'
        }

        res = requests.post(url=export_excel_url,
                                      headers=self.headers, data=body, verify=False)
        operation_id = res.json()['operationId']
        return operation_id



    def download_excel(self, check_progress_url, file_name):
        """
        下载excel文件
        :return:
        """
        # 拿到下载excel文件的url
        start_time = time.time()
        file_url = ''
        while True:
            res = requests.get(url=check_progress_url, headers=self.headers, verify=False)
            progress = res.json()['progress']
            if progress == 100:
                file_url = res.json()['file_url']
                break
            elif time.time() - start_time > 30:
                print("数据准备超时,请排查")
                break
        if file_url:
            self.headers['content-type'] = 'application/octet-stream'
            res = requests.get(url=file_url, headers=self.headers, verify=False)
            with open(file_name, 'wb') as f:
                f.write(res.content)
            print('下载成功,文件名: ' + file_name)
        else:
            print("下载文件地址获取失败, 下载excel文件不成功")


if __name__ == '__main__':
    # excel文档地址
    document_url = 'https://docs.qq.com/sheet/DSnhHWFRraGRzSXhC'
    # 此值每一份腾讯文档有一个,需要手动获取
    local_pad_id = '300000000$JxGXTkhdsIxB'
    # 打开腾讯文档后,从抓到的接口中获取cookie信息
    cookie_value = '****'
    tx = TengXunDocument(document_url, local_pad_id, cookie_value)
    now_user_index = tx.get_now_user_index()
    # 导出文件任务url
    export_excel_url = f'https://docs.qq.com/v1/export/export_office?u={now_user_index}'
    # 获取导出任务的操作id
    operation_id = tx.export_excel_task(export_excel_url)
    check_progress_url = f'https://docs.qq.com/v1/export/query_progress?u={now_user_index}&operationId={operation_id}'
    current_datetime = datetime.strftime(datetime.now(), '%Y_%m_%d_%H_%M_%S')
    file_name = f'{current_datetime}.xlsx'
    tx.download_excel(check_progress_url, file_name)


