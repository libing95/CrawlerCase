# -*- coding: utf-8 -*-
import crawler_common
import os
import re

def writeImg(img_link,name):
    '''
    将下载的图片保存到本地文件夹汇总
    :param img_link:
    :param name:
    :return:
    '''
    image = crawler_common.getUrl_multiTry(img_link)

    filename = img_link[img_link.rfind("/") + 1:]
    fname = "./nsimage/{}".format(nsname)
    try:
        if not os.path.exists(fname):
            os.makedirs(fname)

        filename = fname+'/'+name.text.encode("gbk")+"-"+filename
        with open(filename,"wb") as f:
            f.write(image)
        print(filename+" 下载完成")
    except IOError:
        print("IOError...")



def tuji(url):
    '''
    获取需要爬取的图集的html，解析每个图片的地址，然后下载图片
    :param url:
    :return:
    '''
    # print(url)
    html = crawler_common.getUrl_multiTry(url)
    # 当前图集所有图片的链接
    img_list = crawler_common.del_xml(html,'//ul[@id="hgallery"]/img/@src')

    nextpage =crawler_common.del_xml(html,'//div[@id="pages"]/a[@class="a1"]/@href')[1]
    # 使用正则检查当前页是否是最后一页
    pattern = re.compile(ur'^/g/\d*$')
    #找到图集的名称
    names = crawler_common.del_xml(html,'//h1')
    for t in names:
        name = t
    # print(img_list)
    for img in img_list:
        # 保存图片
        writeImg(img,name)

    # 正则检验
    m = pattern.search(nextpage)
    if m is None:
        # 符合正则就继续遍历下一页
        return True
    else:
        # 否则就停止爬取当前图集
        return False

def nsSpider(url):
    '''
    向需要输入的url发送请求获取html页面并用lxml解析，找到图集的链接
    :param url:
    :return:
    '''
    # 向url发送请求
    html = crawler_common.getUrl_multiTry(url)
    # 使用Xpath解析
    link_list = crawler_common.del_xml(html,'//li[@class="igalleryli"]//div[@class="igalleryli_title"]/a/@href')

    # 遍历爬取图集
    for link in link_list:
        i = 1
        tag = True
        print(link_list)
        print(link)
        while tag:
                # 拼接图集的URL
                fullurl = "https://www.nvshens.com" + link + str(i)+".html"
                print(fullurl)
                i+=1
                tag = tuji(fullurl)


# 主函数，需要输入需要爬取的女神编号
if __name__ == "__main__":

    key = raw_input("请输入需要爬取的女神编号:")
    # 作为保存到本地的文件夹的名称
    nsname = raw_input("请输入需要爬取的女神姓名：")

    nsname = unicode(nsname,'utf-8').encode('gbk')
    # 拼接我们需要爬取的女神的全部图集的URl
    url = "https://www.nvshens.com/girl/{}/album/".format(key)

    nsSpider(url)
    print("谢谢使用")