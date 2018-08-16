# -*- coding: utf-8 -*-
# @Time    : 2018/8/4 14:27
# @Author  : GarryXie

import requests
import md5_tools
from yzm_tools import getYZMImage
from cookie_tools import getCookieByRequestUrl
import random
import re

userAgent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
}


def login(username, pwd, yzm, cookie, viewstate):
    cookie = 'ASP.NET_SessionId=' + str(cookie)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        'Cookie': cookie,
        'Referer': 'http://202.196.32.50/_data/home_login.aspx',
        'Origin': 'http://202.196.32.50',
    }
    data = {
        '__VIEWSTATE': viewstate,
        'pcInfo': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36undefined5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 SN:NULL',
        'typeName': 'ѧ��',
        'dsdsdsdsdxcxdfgfg': pwd,
        'fgfggfdgtyuuyyuuckjg': yzm,
        'Sel_Type': 'STU',
        'txt_asmcdefsddsd': username,
        'txt_pewerwedsdfsdff': '',
        'txt_sdertfgsadscxcadsads': '',
    }
    loginurl = 'http://202.196.32.50/_data/home_login.aspx'
    session = requests.session()
    response = session.post(url=loginurl, data=data, headers=headers)


    # getinfoheaders = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
    #     'Cookie': cookie,
    #     'Referer': 'http://jwglxt.aynu.edu.cn/xsxj/Stu_MyInfo.aspx',
    # }
    # response1 = session.get(url="http://202.196.32.50/xscj/Stu_MyScore_Drawimg.aspx?x=1&h=2&w=705&xnxq=20170&xn=2017&xq=0&rpt=1&rad=2&zfx=0&xh=201600004458", headers=getinfoheaders)
    # print response1.text

    info_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        'Cookie': cookie,
        'Referer': 'http://202.196.32.50/xsxj/Stu_MyInfo.aspx',
    }
    info_url = "http://202.196.32.50/xsxj/Stu_MyInfo_RPT.aspx"
    info_response = session.get(url=info_url,headers=info_headers)
    print(info_response.text)

if __name__ == '__main__':

    # 访问教务主网页获取cookie信息
    response = requests.get(url='http://202.196.32.50/',headers=userAgent)
    cookie = getCookieByRequestUrl(response)

    # 拼装新的请求头，访问登陆的链接，获取到额外的参数和对应的值
    loginheaders = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        'Cookie': cookie,
        'Referer': 'http://202.196.32.50/',
    }
    loginurl = 'http://202.196.32.50/_data/home_login.aspx'
    response = requests.get(url=loginurl, headers = loginheaders)

    VIEWSTATE = re.search(r'<input type="hidden" name="__VIEWSTATE" value="(.*)"', response.text).group(1)

    # 根据cookie信息，访问验证码链接，保存验证码图片到本地
    url = "http://202.196.32.50/sys/ValidateCode.aspx?t=" + str(random.randint(0, 999))
    getYZMImage(url=url, cookie=cookie)

    # 等待用户输入，将密码和验证码进行加密处理
    username = str(raw_input("请输入账号:"))
    passwd = str(raw_input("请输入密码:"))
    yzm = str(raw_input("请输入验证码:"))

    pwd_md5 =  md5_tools.md5_pwd(username,passwd)
    yzm_md5 =  md5_tools.md5_yzm(yzm)

    viewstate = VIEWSTATE
    # 模拟登陆
    login(username, pwd_md5, yzm_md5, cookie, viewstate)