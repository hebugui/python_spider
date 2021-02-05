import requests #请求库
import re #正则表达式
# 下载一个网页
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://www.mzitu.com/',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8'
}

url = 'https://qxs.la/177913/'
# 模拟浏览器发送http请求
response = requests.get(url,headers=headers)
# 目标小说主页的网页源码
html = response.text
# print(html)
# 获取每一章节的信息（章节，url）
dl = re.findall(r'<div class="chapters">(.*?)</div>',html,re.S)
chapter_one = re.findall(r'<a href="(.*?)" title="第一章 雪鹰领">第一章 雪鹰领</a>',dl[0],re.S)[0]
print(chapter_one)
# 下载章节网页
chapter_url = 'https://qxs.la%s' % chapter_one
# 发送请求
chapter_response = requests.get(chapter_url)
# 获取网页源码
chapter_html = chapter_response.text

# print(chapter_html)

f = open('text.txt','w+',encoding = 'utf-8')
f.write(chapter_html)


