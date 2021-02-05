import requests
import re
import os
import time
from bs4 import BeautifulSoup
from requests import RequestException
from tqdm import tqdm
import random

# 梳理：文件结构 ./meizitu2/xiezhen/美少女写真图集/1.jpg-max_page.jpg
#               当前目录->类型文件夹->图组文件夹->图片文件
#               now->class_name->pages_name->page_name

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


# 从列表中移除含param字符串的项
# 思路是查找然后保存下标，最后再一起删除
# 如果直接删除的话，会导致列表访问越界
def remove_some(lists, param):
    move = []
    i = len(lists)
    # 查找
    for j in range(i):
        if param in lists[j]:
            move.append(lists[j])
    # 删除
    for m in move:
        lists.remove(m)
    return lists

# url去重
# 列表去重
# 思路是创建一个空列表，然后遍历旧列表加入不重复的元素
def doubleclear(li):
    new_li = []
    for i in li:
        if i not in new_li:
            new_li.append(i)
    return new_li

# 参数1 链接列表 每一个链接对应一个图组
# 参数2 图片类型
def download(first_page_list,class_name):
    # 下载每个图组的第一页
    for i in tqdm(range(len(first_page_list))):
        first_page_url = first_page_list[i]
        # 重置path
        path = './meizitu2/' + class_name
        if not os.path.exists(path):
            os.makedirs(path)
        max_page,path = downloadFirstPage(first_page_url,path)
        # 第一页下载完成 准备下载其他页
        # print(max_page+':'+path)
        for i in range(2,int(max_page)+1):
            downloadOtherPages(first_page_url,i,path)

# 获取页面信息
def get_one_page(url):
    try:
        res = requests.get(url,headers=headers)
        res.encoding = res.apparent_encoding
        if res.status_code == 200:
            return res
        return None
    except RequestException:
        print("获取失败")

# 下载图片
def saveImages(content, path,num):
    if not os.path.exists(path):
        os.mkdir(path)
    path = path+'/'+str(num)+'.jpg'
    # print('下载到'+path)
    with open(path,'wb') as f:
        f.write(content)
        f.close()

# 下载其他页
def downloadOtherPages(first_page_url, i, path):
    url ='https://www.tupianzj.com'+first_page_url.rsplit('.',1)[0]+'_'+str(i)+'.html'
    # print('第'+str(i)+'页url为：'+url)
    html = get_one_page(url).text
    # 获取图片url并下载
    img_url = re.findall('src="(.*?)" id="bigpicimg"', html)[0]
    img = get_one_page(img_url).content
    saveImages(img, path, i)

# 下载第一页
def downloadFirstPage(first_page_url,path):
    # print('原路径'+path+'\n')
    first_page_url = 'https://www.tupianzj.com'+first_page_url
    # print(first_page_url + "下载每个图组的第一页")
    html = get_one_page(first_page_url).text
    # 获取标题
    title = re.findall('<h1>(.*?)</h1>', html)[0]
    # print(title)
    # 获取最大页
    max_page = re.findall('<a.*?>共(.*?)页: </a>', html)[0]
    # print(max_page)
    # 获取图片url并下载
    img_url = re.findall('src="(.*?)" id="bigpicimg"', html)[0]
    img = get_one_page(img_url).content
    path = path+'/'+title
    # print(path+' 第一张图')
    saveImages(img,path,1)
    return max_page,path


if __name__ == '__main__':
    headers['User-Agent'] = random.choice(user_agent_list)
    isKeep = 'y'
    while isKeep == 'y':
        print('1.清纯 2.性感 3.古装\n4.艺术 5.车模 6.丝袜 ')
        choice = int(input('请输入你想要下载的图片类型(填序号)：'))
        class_list =['xiezhen/','xinggan/','guzhuang/','yishu/','chemo/','siwa/']
        class_url = 'https://www.tupianzj.com/meinv/'+str(class_list[choice-1])
        classes = class_url.split('com',1)[1]
        # print(classes)
        res = requests.get(class_url,headers=headers)
        res.encoding=res.apparent_encoding
        html = res.text
        # print(html)
        soup = BeautifulSoup(html,'html.parser')
        # print(soup)
        # 图组第一页url
        first_page_list = soup.select('div .list_con_box a')
        first_page_list = re.findall(r'<a href="(.*?)"',str(first_page_list))
        # 去掉无关的url链接，格式都是/meinv/这样的，刚好是类型
        for link in first_page_list:
            if link == classes:
                first_page_list.remove(link)

        # 去掉含'list'的无用连接
        first_page_list = remove_some(first_page_list,'list')
        # 去掉重复的url链接
        first_page_list = doubleclear(first_page_list)
        print('要爬取的链接列表：'+str(first_page_list))
        # 图片类型
        class_name = classes.split('/',-1)[-2]
        print(class_name) #xinggan 性感类型
        # 下载模块
        download(first_page_list,class_name)
        print('图片爬取完成')
        isKeep = input('是否继续下载（y/n）：')
        print('')

