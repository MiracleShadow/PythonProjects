import requests
import re
from bs4 import BeautifulSoup
import xlwt3
file = xlwt3.Workbook()

##这个函数获取网页的response 然后返回
def request(url):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    return requests.get(url, headers=headers)

#获取html
def get_html_text(url):
    start_html = request(url)
    start_html.encoding = start_html.apparent_encoding
    return BeautifulSoup(start_html.text, 'lxml')

#获取单界面每一条新闻的url
def get_news_url(url):
    main_html = str(get_html_text(url))
    pattern_td = re.compile(r'<td>(.*)</td>')       #获取<td>标签
    res = pattern_td.findall(main_html)
    list=[]
    for i in res:
        pattern_news_url = re.compile(r'(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')')       #获取<td>标签里的href
        news_url = pattern_news_url.findall(i)
        a=""
        a=a.join(news_url)
        if (a!=""):
            list += [f'http://www.hnnu.edu.cn{a}']
    return list

#获取单界面每一条新闻的时间
def get_news_time(url):
    main_html = str(get_html_text(url))
    pattern_td = re.compile(r'<td>(.*)</td>')  # 获取<td>标签
    res = pattern_td.findall(main_html)
    list = []
    for i in res:
        pattern_news_time = re.compile(r'[0-9]{4}-[0-9]{2}-[0-9]{2}')  # 匹配xxxx-xx-xx格式日期
        news_time = pattern_news_time.findall(str(i))
        list += news_time
    return list

#解析新闻链接的html
def news_html(url):
    list = []
    news_html_list=get_news_url(url)
    for i in news_html_list:
        list += inews_title(i)
        print(inews_p(i))
    #print(list)

#对单个新闻url进行分析，获取标题
def inews_title(url):
    list = []
    news_html_list = get_news_url(url)
    for i in news_html_list:
        news_html_text = str(get_html_text(i))
        title = re.findall(r'<title>(.*?)</title>', news_html_text,re.S|re.M)     #新闻页标题
        list += title
    return list

#对单个新闻url进行分析，获取作者、来源、审核等
def inews_p(url):
    list = [];Source=[];Author=[];Review=[];Uploader=[];Photographer=[];Examiner=[]
    news_html_list = get_news_url(url)
    for i in news_html_list:
        news_html_text = str(get_html_text(i))
        text_p = re.findall(r'<td class="content".*?>(.*?)</td>', news_html_text,re.S|re.M)      #新闻页段落
        text_p_span=re.findall(r'<p.*?>(.*?)</p>', news_html_text,re.S|re.M)
        text = re.findall(r'>([a-zA-Z0-9\u4e00-\u9fa5].*?)<',str(text_p_span))
        Source += re.findall(r'来源：.*?([\u4e00-\u9fa5]+)',str(text))  or "-"      #来源
        Author += re.findall(r'作者：.*?([\u4e00-\u9fa5]+)',str(text))  or "-"       #作者
        Review += re.findall(r'审核：.*?([\u4e00-\u9fa5]+)',str(text))  or "-"         #审核
        Uploader += re.findall(r'上传：.*?([\u4e00-\u9fa5]+)',str(text))  or "-"        #上传
        Photographer += re.findall(r'摄影：.*?([\u4e00-\u9fa5]+)',str(text))  or "-"   #摄影
        Examiner += re.findall(r'审定发布：.*?([\u4e00-\u9fa5]+)',str(text))  or "-"   #审定发布
    list = [Source] + [Author] + [Review] + [Uploader] + [Photographer] + [Examiner]
    return list

#对单个新闻url进行分析，获取正文
def inews_text(url):
    url_list = get_news_url(url);list =[]
    for url in url_list:
        html_Soup = get_html_text(url)
        for spantext in html_Soup.find('td',class_='content').find_all('p'):
            list += [spantext]               #正文
            #print(spantext.get_text())
    return list

if __name__=='__main__':
    for inum in range(1,int(input("请输入你想查询的页数:"))+1):

        url = f'http://www.hnnu.edu.cn/s/21/t/148/p/11/i/{str(inum)}/list.htm'
        text_list = inews_p(url)
        title_list = inews_title(url)
        time_list = get_news_time(url)
        url_list = get_news_url(url)
        content_list = inews_text(url)
