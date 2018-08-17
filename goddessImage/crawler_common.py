# coding=utf-8

from lxml import etree
import urllib2
import logging

def put_request(url):
    '''
    向指定的uel发送request请求
    :param url: 目标url
    :return: 响应的内容
    '''
    headers = {
        "User-Agent": " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    return response.read()


def del_xml(html,xpath_rule):
    '''
    运用Xpath处理xml文本
    :param html:目标文本
    :param xpath_rule: Xpath处理规则
    :return: 处理结果
    '''
    content = etree.HTML(html)
    return  content.xpath(xpath_rule)


def getUrl_multiTry(url):
    '''
    当用多线程爬取某个网站的数据的时候，爬取一段时间后，总出现urlopen error [errno 10060]的错误，结果线程无端的被挂掉，
    一开始的解决思路是每次连接的时候换用不同的useragent,结果还是出现这种问题，
    在网上查了下，看到网上别人的经验，原来是 如果用多个线程爬去某个网站的数据，
    每次连接完的时候，需要sleep(1)一会，不然该网站服务端的防火墙会ban掉你的connect。
    so 按照这种解决方法，果然不再出现urlopen error [errno 10060]的异常了。
   睡眠等待机制会减少urlopen error [errno 10060]出现的概率，但访问次数多了还是会出现
  于 是看了网上说法是连接时网络不稳定造成的，于是写了个多次尝试连接的函数
    :param url:
    :return:
    '''
    user_agent = '"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36"'
    headers = {'User-Agent': user_agent}
    maxTryNum = 10
    for tries in range(maxTryNum):
        try:
            req = urllib2.Request(url, headers=headers)
            reqhtml = urllib2.urlopen(req).read()
            break
        except:
            if tries < (maxTryNum - 1):
                continue
            else:
                logging.error("Has tried %d times to access url %s, all failed!", maxTryNum, url)
                break

    return reqhtml
