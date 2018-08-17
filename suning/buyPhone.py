# -*- coding: utf-8 -*-
# @Time    : 2018/8/8 18:12
# @Author  : GarryXie

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime

# 初始化
WINDOW_SIZE = "1920,1048"  # 窗体大小
CHROME_PATH = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  # chrome 路径
CHROMEDRIVER_PATH = r"D:\Program Files\headless\chromedriver.exe" # driver 路径

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH
driver = webdriver.Chrome(
        executable_path=CHROMEDRIVER_PATH,
        chrome_options=chrome_options)

def login(username, pwd):
    '''
    登录苏宁账户
    :param username:
    :param pwd:
    :return:
    '''
    driver.get('http://yushou.suning.com/appoint/myAppoint.do')
    driver.find_element_by_xpath('//a[@class="tab-item"]').click()
    driver.find_element_by_xpath('//input[@id="userName"]').send_keys(username)
    driver.find_element_by_xpath('//input[@id="password"]').send_keys(pwd)
    driver.find_element_by_xpath('//a[@name="Logon_index_denglu002"]').click()
    time.sleep(3)
    print('登录成功')
    print(driver.get_screenshot_as_file('login.png'))

def buy(buytime):
    while True:
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') >= buytime:
          driver.get('https://product.suning.com/0000000000/10578094717.html')
          time.sleep(1)
          try :
              # 错误的示范
              # driver.find_element_by_xpath('//div/a[@id="buyNowAddCart"]').click()
              driver.find_element_by_xpath('//div/a[@id="addCart"]').click()
              time.sleep(1)
              print(now.strftime('%Y-%m-%d %H:%M:%S'))
              driver.get_screenshot_as_file('buy.png')
              print('购买成功')
              break
          except :
              print("try again...")
              pass
        time.sleep(0.5)
        print(now.strftime('%Y-%m-%d %H:%M:%S')+' 等待购买中...')


login('yourUserName','yourPassword') # 更改为你的账户，密码
buy('2018-08-17 10:00:00') # 更改抢购的时间