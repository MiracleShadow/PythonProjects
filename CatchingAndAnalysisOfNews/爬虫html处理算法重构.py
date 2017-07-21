import requests
import re
from bs4 import BeautifulSoup

class Get_Html_Text(object):
    def __init__(self,url):
        self.url = url

    ##这个函数获取网页的response 然后返回
    def request(self):
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        content = requests.get(self.url, headers=headers)
        return content

    # 获取html
    def get_html_text(self):
        start_html = self.request()
        start_html.encoding = start_html.apparent_encoding
        Soup = BeautifulSoup(start_html.text, 'lxml')
        return Soup

class Get_News(object):
    def __init__(self, url):
        self.main_html = str(Get_Html_Text(url).get_html_text())

    #获取一面所有新闻的URL并存放在一个list里
    def get_news_url(self):
        pattern_td = re.compile(r'<td>(.*)</td>')  # 获取<td>标签
        res = pattern_td.findall(self.main_html)
        list = []
        for i in res:
            pattern_news_url = re.compile(r'(?<=href=\").+?(?=\")|(?<=href=\').+?(?=\')')  # 获取<td>标签里的href
            news_url = pattern_news_url.findall(i)
            a = "";a = a.join(news_url)
            if (a != ""): list += ['http://www.hnnu.edu.cn' + a]
        return list

    # 获取单界面每一条新闻的时间
    def get_news_time(self):
        pattern_td = re.compile(r'<td>(.*)</td>')  # 获取<td>标签
        res = pattern_td.findall(self.main_html)
        list = []
        for i in res:
            pattern_news_time = re.compile(r'[0-9]{4}-[0-9]{2}-[0-9]{2}')  # 匹配xxxx-xx-xx格式日期
            news_time = pattern_news_time.findall(str(i))
            list += news_time
        return list

#解析单个新闻url，获得标题、作者、内容等信息
class Get_OneNews(object):
    def __init__(self,url):
        self.url_list= Get_News(url).get_news_url()
        self.title_list = []
        self.text = []

    # 对单个新闻url进行分析，获取标题
    def get_news_title(self):
        for i in self.url_list:
            news_html_text = str(Get_Html_Text(i).get_html_text())
            title = re.findall(r'<title>(.*?)</title>', news_html_text, re.S | re.M)  # 新闻页标题
            self.title_list += title
        return self.title_list

    # 对单个新闻url进行分析，获取作者、正文等
    def get_news_text(self):
        for i in self.url_list:
            news_html_text = str(Get_Html_Text(i).get_html_text())
            text_p_span = re.findall(r'<p.*?>(.*?)</p>', news_html_text, re.S | re.M)
            text = re.findall(r'>([a-zA-Z0-9\u4e00-\u9fa5].*?)<', str(text_p_span))
            self.text += [text]
        return self.text


if __name__=='__main__':
    #for inum in range(1, int(input("请输入你想查询的页数:")) + 1):
        inum = 1
        url = 'http://www.hnnu.edu.cn/s/21/t/148/p/11/i/' + str(inum) + '/list.htm'
        title = Get_OneNews(url).get_news_title()
        text = Get_OneNews(url).get_news_text()
        print(title[0],text[0])