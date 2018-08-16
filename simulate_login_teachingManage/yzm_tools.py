# -*- coding: utf-8 -*-
# @Time    : 2018/8/4 14:10
# @Author  : GarryXie
import requests
import time
# from cookie_tools import getCookieByRequestSession


def getYZMImage(url, cookie):
    '''
    向验证码地址，发送请求下载验证码
    :param url: 验证码链接
    :param cookie: cookie
    :return:
    '''
    cookie = 'ASP.NET_SessionId='+str(cookie)
    headers = {
        'Host': '202.196.32.50',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        'Cookie':cookie,
        'Referer': 'http://202.196.32.50/_data/home_login.aspx',
        'Connection':'keep-alive',
        'Accept-Language':'zh-CN,zh;q=0.9',
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    }
    response = requests.get(url,headers=headers)
    save_image(response.content)

def save_image(image):
    '''
    保存验证码
    :param image:
    :return:
    '''
    with open('yzm.jpg','wb') as f:
        f.write(image)
    time.sleep(1)

# headers ={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
# }
#
# cookie = getCookieByRequestSession("http://202.196.32.50",headers=headers)
#
# url = "http://202.196.32.50/sys/ValidateCode.aspx"
# getYZMImage(url=url,cookie=cookie)
