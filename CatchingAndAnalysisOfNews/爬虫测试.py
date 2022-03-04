import requests
import re
from bs4 import BeautifulSoup 
import os

def request(url):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    return requests.get(url, headers=headers)

def save(img_url,num):
    name = str(num)
    img = request(img_url)
    with open(f'{name}.jpg', 'ab') as f:
        f.write(img.content)

tt = int(input("请输入你想查询的页数:"))

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
for inum in range(1,tt+1):
    all_url = 'http://www.hnnu.edu.cn/s/21/t/148/p/11/i/'+str(inum)+'/list.htm'
    start_html = requests.get(all_url,  headers=headers) 
    start_html.encoding=start_html.apparent_encoding
    Soup = BeautifulSoup(start_html.text, 'lxml')
    all_a = Soup.find('td',class_='content').find('table').find_all('a') 
    for a in all_a:
        title = a.get_text() 
        path = str(title).strip() ##去掉空格
        print(u'建了一个名字叫做', path, u'的文件夹！')
        os.makedirs(os.path.join("D:\\News", path)) ##创建一个存放新闻的文件夹
        os.chdir("D:\\News\\"+path) ##切换到上面创建的文件夹
        href = a['href'] 
        href='http://www.hnnu.edu.cn'+href
        #print(title, href)
        html = requests.get(href, headers=headers)
        html.encoding=html.apparent_encoding#获取
        #print(html.text)
        html_Soup = BeautifulSoup(html.text, 'lxml')#解析
        all_p = html_Soup.find('td',class_='biaoti3')
        all_span = html_Soup.find('td',class_='content').find_all('p')
        num=0
        for news_img in html_Soup.find('td',class_='content').find_all('img'):
            if(news_img):
                news_img_url='http://www.hnnu.edu.cn'+news_img['src']
                num+=1
                save(news_img_url,num)
        for p in all_p:
            #print(p)
            neirong = ""
            for spantext in all_span:
                neirong += spantext.get_text() + "\n"
            #print(neirong)
            name = p ##名字
            #xt = requests.get(html_Soup, headers=headers)
            f = open(name+'.text', 'wt',encoding='utf-8')##写入多媒体文件必须要 b 这个参数！！必须要！！
            f.write(neirong) ##多媒体文件要是用conctent哦！
            f.close()