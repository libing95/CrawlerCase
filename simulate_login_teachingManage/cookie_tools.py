# -*- coding: utf-8 -*-
# @Time    : 2018/8/4 13:57
# @Author  : GarryXie

import requests


def getCookieByRequestUrl(response):
    '''
    根据请求的响应获取cookie信息
    :param response: 请求网站的响应
    :return:
    '''
    cookiejar = response.cookies
    # 把CookieJar转为字典
    cookiedict = requests.utils.dict_from_cookiejar(cookiejar)

    return cookiedict['ASP.NET_SessionId']


def getCookieByRequestSession(url, headers):
    '''
    发送请求获取cookie信息
    :param url: 请求的网站
    :param headers: 请求头
    :return:
    '''
    session = requests.session()
    response = session.get(url=url, headers=headers)
    cookiedict = requests.utils.dict_from_cookiejar(response.cookies)
    return cookiedict['ASP.NET_SessionId']

headers ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

# print(getCookieByRequestSession('http://202.196.32.50',headers))
# print(getCookieByRequestUrl(requests.get('http://202.196.32.50')))