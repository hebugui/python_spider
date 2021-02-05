import requests
import re
from bs4 import BeautifulSoup
import random
from tqdm import tqdm
from urllib import parse
import os
from requests import RequestException

from StudentManagement.utils import getCurrentTime

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

# 爬取第一页
def downloadFirstPage(contents, lists):
    lists = getLists(lists, contents)
    return lists


def downloadOtherPages(url,max_page, lists):
    for i in tqdm(range(2,int(max_page)+1)):
        other_url = url.rsplit('.html')[0] +'-'+str(i)+'.html'
        # print(other_url)
        res = get_one_page(other_url)
        soup = BeautifulSoup(res.text, 'html.parser')
        # 获取视频链接列表
        contents = soup.find('main', id='main-container').find_all('a', class_='loading')
        lists = getLists(lists, contents)
    return lists

# 获取视频链接列表 增添式的
def getLists(lists, contents):
    for content in contents:
        list = {'href': '', 'title': '', 'src':''}
        # print(type(content)) content为bs4.element.Tag类型
        href = 'https://www.611d344e121d.com'+re.findall(r'href="(.*?)"',str(content))[0]
        title = re.findall(r'title="(.*?)"',str(content))[0]
        src = re.findall(r'src="(.*?)"',str(content))[0]
        list['href']=href
        list['title']=title
        list['src']=src
        lists.append(list)
    return lists

# 根据关键字筛选列表核心操作
def check(keyword, lists):
    new_lists = []
    for list in lists:
        if keyword in list['title']:
            new_lists.append(list)
    return new_lists

# 根据关键字筛选列表
def filterByKeyword(keywords, lists):
    new_lists = lists
    for keyword in keywords:
        new_lists = check(keyword,new_lists)
    return new_lists

# url去重
# 列表去重
# 思路是创建一个空列表，然后遍历旧列表加入不重复的元素
def doubleclear(li):
    new_li = []
    for i in li:
        if i not in new_li:
            new_li.append(i)
    return new_li

# 保存至txt文件
def saveInfo(lists, path,tips):
    if not os.path.exists(path):
        os.mkdir(path)
    file_name = path + getCurrentTime() + '.txt'
    # print(path)
    with open(file_name, 'w') as f:
        # 筛选第一行
        if (tips):
            f.write(tips+'\n')
        for list in lists:
            f.write(str(list)+'\n')
        f.close()


if __name__ == '__main__':
    isKeep = 'y'
    while(isKeep == 'y'):
        # 女优专区得单独爬 结构有点不一样 三层结构
        # 而且貌似和其他两个不重复，有爬取价值
        classes = {'1': '中文字幕', '2': '亚洲无码', '3': '女优专区'}
        print('\n*****菜单*****\n')
        for key in classes:
            print(key + ': ' + classes[key])
        print('\n**************\n')
        choice = int(input('请输入想要进行筛选的类型的序号：'))
        origin_url = classes[str(choice)]
        encode_origin_url = parse.quote(origin_url)
        # print('您选择的是'+origin_url+')
        # print('url加密结果：'+ encode_origin_url)
        headers['User-Agent'] = random.choice(user_agent_list)
        keyword = input('请输入关键字查找（多个关键字用空格符隔开）：')
        # url加解密
        url='https://www.611d344e121d.com/shipin/list-'+encode_origin_url+'.html'
        res = get_one_page(url)
        soup = BeautifulSoup(res.text,'html.parser')
        # 获取最大页数
        # /shipin/list-中文字幕-100.html
        # /shipin/list-亚洲无码-98.html
        max_page = soup.find('a',title='尾页')['href'].rsplit('.html',1)[0].rsplit('-',1)[-1]
        print('最大页数为：'+max_page)
        search_max_page = input('请输入想要搜索的最大页数：')
        # 获取视频链接列表
        contents = soup.find('main',id='main-container').find_all('a',class_='loading')
        # print(contents)
        lists = []
        # 爬取当前页所有的视频信息
        lists = getLists(lists, contents)
        # 爬取第一页
        lists = downloadFirstPage(contents,lists)
        # 爬取其他页
        lists = downloadOtherPages(url,search_max_page,lists)
        # 去重操作
        lists = doubleclear(lists)
        print('预处理结果')
        # for list in lists:
        #     print(list)
        path1 = './mm_spider/预处理结果/'
        saveInfo(lists,path1,'')
        # 分割 默认分隔符为空格，次数limit不限 返回一个列表
        keywords = keyword.split()
        # 根据关键字筛选列表
        lists = filterByKeyword(keywords,lists)
        # 输出筛选后的结果
        print('筛选结果')
        # for list in lists:
        #     print(list)
        path2 = './mm_spider/筛选结果/'
        tips = ''
        for keyword in keywords:
            tips = tips +''+ keyword
        tips = '类别：'+origin_url +'(关键字：'+ tips+')'
        print (tips)
        saveInfo(lists,path2,tips)
        print('\n\n')
