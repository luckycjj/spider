#coding=utf-8
import sys
import json
reload(sys)
sys.setdefaultencoding('utf8')
import requests
from bs4 import BeautifulSoup


resp=requests.get('https://movie.douban.com/j/search_tags?type=movie&tag=&source=') #请求网页首页
bsobj = BeautifulSoup(resp.content,'lxml') #将网页源码构造成BeautifulSoup对象，方便操作
p = json.loads(bsobj.find('p').get_text())['tags']
text = ""
goodmovie = ""
badmoive = ""
for i in p:
    text += '\n' + u'类别：' + i + '\n\n'
    re = requests.get('https://movie.douban.com/j/search_subjects?type=movie&tag='+i+'&sort=time&page_limit=20&page_start=0')
    bs = BeautifulSoup(re.content,'lxml')
    movie = json.loads(bs.find('p').get_text())['subjects']
    for j in movie:
        text += j['title'] + u':' + str(j['rate']) + u'分' + '\n'
        if float(j['rate']) - 8 >=0:
            goodmovie += j['title']+"("+j['rate']+")" + ", "
        elif float(j['rate']) - 4 <=0:
            badmoive += j['title']+"("+j['rate']+")" + ", "


with open('movie.txt','w') as f: #在当前路径下，以写的方式打开一个名为'haoyun.txt'，如果不存在则创建
    f.write(text + u"\n高分电影：" + goodmovie + u"\n垃圾电影：" + badmoive) #将text里的数据写入到文本中
