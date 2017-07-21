import requests
import re
from bs4 import BeautifulSoup
import os

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
for inum in range(1,int(input("请输入你想查询的页数:"))+1):
    url = 'http://www.hnnu.edu.cn/s/21/t/148/p/11/i/'+str(inum)+'/list.htm'
    start_html = requests.get(url,  headers=headers)
    start_html.encoding=start_html.apparent_encoding
    Soup = BeautifulSoup(start_html.text, 'lxml')
    all_a = Soup.find('td',class_='content').find('table').find_all('a')
    all_class_columnStyle = Soup.find('td',class_='content').find_all('table',class_='columnStyle')
    sum = 0
    arr= [0 for t in all_a]    #列表的长度为<a>标签数
    for class_columnStyle in all_class_columnStyle:
        for i in class_columnStyle.find_all(attrs={"align": "center"}):
            arr[sum]=str(i.get_text())      #将新闻的时间存入数组
            sum+=1
            #print(i.get_text()) 输出每则新闻的日期
    sum=0
    for a in all_a:
        title = a.get_text()
        href = a['href']
        href='http://www.hnnu.edu.cn'+href
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
        sum+=1
        for news_img in html_Soup.find('td',class_='content').find_all('img'):
            news_img_url='http://www.hnnu.edu.cn'+news_img['src']
            print(news_img_url)  #图片地址
        print('\n')