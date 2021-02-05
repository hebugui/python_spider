import random

import requests
from bs4 import BeautifulSoup
import re
import os
import time
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Connection': 'close',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'http://www.quanshuwang.com/',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.9'
}

user_agent_list = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/61.0",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
    "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
    ]
headers['User-Agent'] = random.choice(user_agent_list)
# print(headers['User-Agent'])
# print(type(random.choice(user_agent_list)))


def download(url):
    # url = 'http://www.quanshuwang.com/book/44/44683/15379610.html'
    res = requests.get(url,headers=headers)
    res.encoding ='gbk'
    if res.status_code != 200:
        print("爬取失败")

    html = res.text
    soup = BeautifulSoup(html,'html.parser')
    # 获取内容
    content = soup.find('div',id='content')
    # print(content)
    # 获取标题
    title = re.findall(r'</script>.*?(.*?)<br/>',str(content))[0].strip()
    content = str(content).replace('<br/>','')
    # print(content)
    content = content[content.find('\n')+1:]
    content = content.split('<s',1)[0]
    content = content.replace('\n','')

    path = './book/'+title+'.txt'
    if not os.path.exists('./book'):
        os.mkdir('./book')
    with open(path,'w') as f:
        f.write(content)
        f.close()

if __name__ =="__main__":
    num = int(input("请输入想要下载的章节数目："))
    i = 0  # 已下载章节数
    j = 0  # 偏移量，一般来说加1 但存在无效链接
    while i < num:
        location = 15379609 + j
        url = 'http://www.quanshuwang.com/book/44/44683/' + str(location) + '.html'
        try:
            download(url)
        except Exception as e:
            print(url+'  '+str(e))
            j = j + 1
            continue
        print(url+'  第'+str(i)+'章下载完成')
        i = i + 1
        j = j + 1
        time.sleep(6)
    print('**下载完成**')