#coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
from bs4 import BeautifulSoup


resp=requests.get('http://www.haoyunhu56.com/') #请求网页首页
bsobj = BeautifulSoup(resp.content,'lxml') #将网页源码构造成BeautifulSoup对象，方便操作
ul_list = bsobj.find_all(['ul'],attrs={'class':'scroll'})
text = ""
number = 0
for i in ul_list:
    for x in i.find_all("li"):
        li = x.get_text()
        text += li + "\n"
    for j in i.find_all("span",attrs={'class':'text'}):
         x = j.find("i").get_text()
         number += float(x)
with open('haoyun.txt','w') as f: #在当前路径下，以写的方式打开一个名为'haoyun.txt'，如果不存在则创建
    f.write(text + u'总吨数：' + str(number) + u'吨') #将text里的数据写入到文本中