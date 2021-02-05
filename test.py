from __future__ import division
from urllib import parse
# str1 = '中文字幕'
# str2 = parse.quote(str1)    #将字符串进行编码
# print(str2)

import random
import os
import requests
from bs4 import BeautifulSoup
import re


# url = 'https://www.sohu.com/a/226127592_139908'
# res = requests.get(url,timeout=3).text
# print(type(res))
# soup = BeautifulSoup(res,'html.parser')
# data = soup.find_all('article',class_='article')
# # data = soup.select('article')
# print(data)
# print("\n\n\n")
#
# rep = {'\n':'',' ':'','<p>':'','</p>':'','<strong>':'','</strong>':''}
# rep = dict((re.escape(k), v) for k, v in rep.items())
# #print(rep)
# #print(rep.keys())
# pattern = re.compile("|".join(rep.keys()))
# #print(pattern)
# out = pattern.sub(lambda m: rep[re.escape(m.group(0))], repr(data))
# out1 = out.split('e">',1)
# out2 = repr(out1[1]).split('<ahref',1)[0]
# out3 = repr(out2).replace('"','').replace("'",'')
# print(out3)
# with open("./wordcloud/clice3.txt",'w') as f:
#     f.write(out3)
#     f.close()
# print("****************")
# print(type(data))
# soup2 = BeautifulSoup(repr(data),'html.parser')
# data2 = soup2.find_all('strong')
# print('------------------------')
# print(data2)
# data3 =[str(i) for i in data2]
# data4 = ' '.join(data3)
# print(data4)
# data5 = 'hello woaini'
# data6 = data5.split('o',-1)
# print(data6)
# data7 = data5.replace(" ","")
# print(data7)
# num = int(input("请输入一个数字："))
# for i in range(num):
#     print(i)
# url = 'http://www.quanshuwang.com/book/44/44683/15379655'
# res = requests.get(url,timeout=3)
# print(res.text)
#
# current_number = 0
# while current_number <= 5:
#     print(str(current_number))
#     current_number += 1

# number = random.choice([1,2,3,4,5])
# print(number)

# i = 0
# while i<5:
#     #
#     # if(i%2):
#     #     continue
#     i = i + 1
#     print(i+3000)

# url = 'https://img.tupianzj.com/uploads/allimg/202009/9999/8640f64c17.jpg'
# res = requests.get(url)
# res.encoding = res.apparent_encoding
# content = res.content
# print(content)
# path = './meizitu/' + str(111) + '.jpg'
# if not os.path.exists('./meizitu'):
#     os.mkdir('./meizitu')
# with open(path, 'wb') as f:
#     f.write(content)
#     f.close()

# url = 'https://www.tupianzj.com/meinv/xinggan/'
# classes = url.split('com',1)[1]
# print(classes)
# haha = []
# lists = ['world','hello','xixihaha']
# i = len(lists)
# for j in range(i):
#     if 'o' in lists[j]:
#         haha.append(lists[j])
# for ha in haha:
#     lists.remove(ha)
# print(lists)
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
#     'Connection': 'close',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Referer': 'http://www.quanshuwang.com/',
#     'Accept-Encoding': 'gzip, deflate, sdch',
#     'Accept-Language':'zh-CN,zh;q=0.9'
# }
#
# user_agent_list = [
#     "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
#     "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
#     "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
#     "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
#     ]
# headers['User-Agent'] = random.choice(user_agent_list)
#
# url='https://blog.csdn.net/weixin_43827376/article/details/113482197?ops_request_misc=%25257B%252522request%25255Fid%252522%25253A%252522161217394216780264098344%252522%25252C%252522scm%252522%25253A%25252220140713.130102334.pc%25255Fall.%252522%25257D&request_id=161217394216780264098344&biz_id=&utm_medium=distribute.pc_search_result.none-task-code-2~all~first_rank_v2~rank_v29-18-113482197-3.pc_search_result_before_js&utm_term=python%25E5%2586%2599%25E4%25B8%2580%25E4%25B8%25AA%25E5%25B0%258F%25E8%25AF%25B4'
# url2 = 'https://www.baidu.com'
# for i in range(100):
#     res = requests.get(url2,headers = headers)
#     print('这是第'+str(i+1)+'次访问')
#

# lists = ['hello','xixi','hahalo']
# new_list = []
# for list in lists:
#     if 'o' in list:
#         new_list.append(list)
# print(new_list)
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
#     'Connection': 'close',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#     'Referer': 'http://www.quanshuwang.com/',
#     'Accept-Encoding': 'gzip, deflate, sdch',
#     'Accept-Language':'zh-CN,zh;q=0.9'
# }
# # https://www.baidu.com/s?wd=python
# # ip地址到域名的映射
# url = 'http://www.baidu.com/s'
# url2 = 'http://112.80.248.75/s'
# data={'wd':'python'}
# res = requests.get(url2,params=data,headers=headers)
# res.encoding = res.apparent_encoding
# html = BeautifulSoup(res.text,'html.parser')
# print(html.prettify())
# print(res.headers)

# print('{}'.format)
# coding: utf-8



# def jia(x, y):
#     print(x + y)
#
# def jian(x, y):
#     print(x - y)
#
# def cheng(x, y):
#     print(x * y)
#
# def chu(x, y):
#     print(x / y)
#
# operator = {'+': jia, '-': jian, '*': cheng, '/': chu}
#
# def f(x, o, y):
#     operator.get(o)(x, y)
#
# f(3, '+', 2)


# print("\033[31;40m这是红色字体\033[0m")
#
# ans = False
# if ans:
#     print('1')
# a = '123'
# b = '123'
# c = a
# d = b

# print(a == a)
# print(id(a) == id(b))
# print(a in b)
# print(c == d)


# test = 'hah h x'
# test1 = test.split()
# print(type(test1))

# 实现list插入
list = [1,2,3]
print(list)
list2 = list
list2.append(0)
i = len(list2)-1
index = 0
while i>=0:
    if i == index:
        list2[index] = 4
        break
    list2[i] = list2[i-1]
    i = i - 1
    pass
print(list2)