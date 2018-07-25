# coding=utf-8
import requests
import urllib2
import os

from lxml import etree

html = requests.get("https://www.douban.com/")
html.encoding = 'utf-8'
selector = etree.HTML(html.text)
content = selector.xpath('//img//@src')

for imgurl in content:
    name = imgurl.split('/')[len(imgurl.split('/')) - 1]
    os.chdir(r"D:\git\spider\img")
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
        'Cookie': 'AspxAutoDetectCookieSupport=1',
    }
    if imgurl.find('jpg') != -1 or imgurl.find('png') != -1:
        print imgurl
        request = urllib2.Request(imgurl, None, header)  # 刻意增加头部header，否则本行与下一行可以写为：response = urllib2.urlopen(imgurl)
        response = urllib2.urlopen(request)
        f = open(name, 'wb')
        f.write(response.read())
        f.close()