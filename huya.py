import requests
import re
import os

# 获取虎牙直播封面图片、链接、标题、主播名
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36',
    'Connection': 'keep-alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://www.huya.com/',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'en-US,en;q=0.8'
}
url = 'https://www.huya.com/g/xingxiu'
response = requests.get(url,headers=headers)
html = response.text
# 直播间图片，图片url
pics = re.findall(r'<img class="pic".*?data-original="(.*?)" src.*?>',html)
# pics = re.findall(r'<img class="pic".*?src="(.*?)"',html)
# 直播间链接
hrefs = re.findall(r'<a href="(.*?)" class="title"',html)
# 直播间标题
titles = re.findall(r'<a.*?class="title".*?title="(.*?)"',html)
# 直播间主播名字
names = re.findall(r'<i class="nick".*?>(.*?)</i>',html)
items = []
# 爬取直播间信息
for i in range(len(pics)):
    item = {'pic': '', 'href':'','name': '', 'title': ''}
    # 加match主要是去除无效链接
    if(re.match(r'https://',pics[i])):
        item['pic'] = pics[i]
        item['href'] = hrefs[i]
        item['name'] = names[i]
        item['title'] = titles[i]
        items.append(item)

# 下载图片
# url图片直接访问网址然后获取二进制格式即可，如requests.get(url=pic).content
for item in items:
    print(item)
    _dir = './huya'
    if not os.path.exists(_dir):
        os.mkdir(_dir)
    name = item['name']
    path = './huya/' + name +'.jpg'
    pic = item['pic']
    content = requests.get(pic).content
    with open(path,'wb') as f:
        f.write(content)

