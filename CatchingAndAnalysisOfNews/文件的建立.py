import os
import requests
import re
from bs4 import BeautifulSoup

##这个函数创建文件夹
def mkdir(path):
    path = path.strip()
    isExists = os.path.exists(os.path.join("D:\\News", path))
    if not isExists:
        print(u'建了一个名字叫做', path, u'的文件夹！')
        os.makedirs(os.path.join("D:\\News", path))
        os.chdir(os.path.join("D:\\News", path))  ##切换到目录
        return True
    else:
        print(u'名字叫做', path, u'的文件夹已经存在了！')
        return False

##这个函数获取网页的response 然后返回
def request(url):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    return requests.get(url, headers=headers)

##这个函数保存图片
def save(img_url):
    name = img_url[-9:-4]
    img = request(img_url)
    with open(f'{name}.jpg', 'ab') as f:
        f.write(img.content)

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
for inum in range(1,int(input("请输入你想查询的页数:"))+1):
    url = f'http://www.hnnu.edu.cn/s/21/t/148/p/11/i/{str(inum)}/list.htm'
    start_html = requests.get(url,  headers=headers)
    start_html.encoding=start_html.apparent_encoding
    Soup = BeautifulSoup(start_html.text, 'lxml')
    all_a = Soup.find('td',class_='content').find('table').find_all('a')
    all_class_columnStyle = Soup.find('td',class_='content').find_all('table',class_='columnStyle')
    arr = [0 for _ in all_a]
    for i in Soup.find_all('td',class_='lb'):
        path=i.get_text()
        mkdir(path)
    for a in all_a:
        title = a.get_text()
        href = a['href']
        href = f'http://www.hnnu.edu.cn{href}'
        #print(title, href)
        html = requests.get(href, headers=headers)
        html.encoding=html.apparent_encoding
        #print(html.text)
        html_Soup = BeautifulSoup(html.text, 'lxml')
        '''
        for biaoti3 in html_Soup.find_all('td',class_='biaoti3'):
            print(biaoti3.get_text())  #标题
        print(arr[sum])   #时间
        '''
        for news_img in html_Soup.find('td',class_='content').find_all('img'):
            news_img_url='http://www.hnnu.edu.cn'+news_img['src']
            print(news_img_url)  #图片地址
            save(news_img_url)
        print('\n')