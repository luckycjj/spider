#coding=utf-8
import sys
import json
reload(sys)
sys.setdefaultencoding('utf8')
import requests
from bs4 import BeautifulSoup


resp=requests.post('http://www.haoyunhu56.com/entrustOrder/getBigType') #请求网页首页
bsobj = BeautifulSoup(resp.content,'lxml') #将网页源码构造成BeautifulSoup对象，方便操作
p = json.loads(bsobj.find('p').get_text())['goodsHistory']
text = ""
goodmovie = ""
badmoive = ""
for i in p:
    text += '\n\n\n\n' + u'品种：' + i['typeName'] + '('+i['typeNameId']+')'
    re = requests.post('http://www.haoyunhu56.com/entrustOrder/getBigVarieties?typeNameId='+ i['typeNameId'])
    bs = BeautifulSoup(re.content,'lxml')
    movie = json.loads(bs.find('p').get_text())['goodsHistory']
    for j in movie:
        text += '\n\n' + u'大类：' + j['varieties'] + '('+j['varietiesId']+')'
        rex = requests.post('http://www.haoyunhu56.com/entrustOrder/getBigProductName?varietiesId=' + j['varietiesId'])
        bsx = BeautifulSoup(rex.content, 'lxml')
        moviex = json.loads(bsx.find('p').get_text())['goodsHistory']
        for x in moviex:
            text += '\n' + u'品名：' + x['productName'] + '(' + x['productNameId'] + ')'



with open('movie.txt','w') as f: #在当前路径下，以写的方式打开一个名为'haoyun.txt'，如果不存在则创建
    f.write(text) #将text里的数据写
