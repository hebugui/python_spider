import requests
import re
import os

def download(url_other,path,page_num):
    print('进入jpg')
    res = requests.get(url_other)
    res.encoding = res.apparent_encoding
    html = res.text
    # 图片url
    img_url = re.findall('src="(.*?)" id="bigpicimg"', html)[0]
    content = requests.get(img_url).content
    path = path + '/' + str(page_num) + '.jpg'
    with open(path,'wb') as f:
        f.write(content)
        f.close()

def downloadOtherPages(url,max_page,title):
    print('进入图片url')
    for i in range(2,max_page+1):
        url_other = url.rsplit('.',1)[0]+'_'+str(i)+'.html'
        print(url_other)
        path = './mei/'+title
        print(path)
        if not os.path.exists(path):
            os.makedirs(path)
        download(url_other,path,i)

if __name__ == '__main__':
    url = 'https://www.tupianzj.com/meinv/20180329/158612.html'
    res = requests.get(url)
    res.encoding = res.apparent_encoding
    html = res.text
    # 图片url
    img_url = re.findall('src="(.*?)" id="bigpicimg"',html)[0]
    #下载第一页
    # downloadFirstPage(img_url,path)
    # 获取标题
    title = re.findall('<h1>(.*?)</h1>',html)[0]
    print(title)
    # 获取最大页
    max_page = re.findall('<a.*?>共(.*?)页: </a>',html)[0]
    print(max_page)
    downloadOtherPages(url,int(max_page),title)

