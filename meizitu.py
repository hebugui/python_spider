import requests
import re
import os
import time
from bs4 import BeautifulSoup
from otherPages import downloadOtherPages,download

# 下载程序
def main(links,folder_name):
    urls = links
    i = 1
    if not os.path.exists('./meizitu/' + folder_name):
        os.mkdir('./meizitu/' + folder_name)
    print('./meizitu/' + folder_name)
    for url in urls:
        try:
            url = 'https://www.tupianzj.com'+url
            print(url)
            res = requests.get(url)
            res.encoding = res.apparent_encoding
            html = res.text
            img_url = re.findall('src="(.*?)" id="bigpicimg"',html)[0]
        except Exception as e:
            print(e)
            continue
        print('正在爬取图片：' + img_url)
        # time.sleep(1)
        img_res = requests.get(img_url)
        content = img_res.content
        path = './meizitu/'+folder_name+'/'+ str(i) +'.jpg'
        # print(path)
        i = i + 1
        with open(path, 'wb') as f:
            f.write(content)
            f.close()


# 从列表中移除含param字符串的项
def remove_some(lists, param):
    move = []
    i = len(lists)
    for j in range(i):
        if param in lists[j]:
            move.append(lists[j])
    for m in move:
        lists.remove(m)
    return lists

# url去重
def doubleclear(li):
    new_li = []
    for i in li:
        if i not in new_li:
            new_li.append(i)
    return new_li

if __name__ == '__main__':
    isKeep = 'y'
    while isKeep == 'y':
        print('1.清纯 2.性感 3.古装\n4.艺术 5.车模 6.丝袜 ')
        choice = int(input('请输入你想要下载的图片类型(填序号)：'))
        list =['xiezhen/','xinggan/','guzhuang/','yishu/','chemo/','siwa/']
        url = 'https://www.tupianzj.com/meinv/'+str(list[choice-1])
        classes = url.split('com',1)[1]
        print(classes)
        res = requests.get(url)
        res.encoding='gbk'
        html = res.text
        # print(html)
        soup = BeautifulSoup(html,'html.parser')
        # print(soup)
        links = soup.select('div .list_con_box a')
        links2 = re.findall(r'<a href="(.*?)"',str(links))
        links3 = []
        for link in links2:
            if link == classes:
                links2.remove(link)

        links2_new = remove_some(links2,'list')

        links2_newnew = doubleclear(links2_new)
        print('要爬取的链接列表：'+str(links2_newnew))
        folder_name = classes.split('/',-1)[-2]
        print(folder_name) #xinggan 性感类型
        main(links2_newnew,folder_name)
        print('图片爬取完成')
        isKeep = input('是否继续下载（y/n）：')
        print('')
