import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas


def getNewsDetail(newsurl):
    r = requests.get(newsurl)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'html.parser')
    result = {'title': soup.select('title')[0].text.strip()}
    result['dt'] = datetime.strptime(soup.select('.STYLE2')[0].contents[0].strip(), '发布时间：%Y-%m-%d\r\n 浏览次数：').strftime(
        '%Y-%m-%d')  # 一行时间
    '''
    timesource = soup.select('.STYLE2')[0].contents[0].strip()        #格式修改 去除多余文字
    dt = datetime.strptime(timesource,'发布时间：%Y-%m-%d\r\n 浏览次数：')
    result['time'] = dt.strftime('%Y-%m-%d')                          #时间
    '''
    result['article'] = ' '.join(p.text.strip() for p in soup.select('.MsoNormal')[:-1])  # 一行全文
    result['newssource'] = newsurl
    '''
    text=''
    for p in soup.select('.MsoNormal')[:-1]:               #全文
        text+=p.text
    result['article']=text
    '''
    # result['editor'] = soup.select('.MsoNormal')[-1].text.strip()      #作者出自倒数第一个p标签，但有少部分出自倒数第二或第三个标签，造成返回值为空，多为出错原因，对此
    # 进行信息处理时要注意，故在文章内容中将作者信息一并提取了
    return result


def parseListLinks(url):  # 你非要定义的 取得每页中所有的新闻
    newsdetails = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for ent in soup.select('.columnStyle'):
        url = ent('a')[0]['href']
        urlreal = 'http://www.aufe.edu.cn' + url
        newsdetails.append(getNewsDetail(urlreal))
    return newsdetails


url = 'http://www.aufe.edu.cn/s/1/t/21/p/12/i/{}/list.htm'
news_total = []
for i in range(10):  # 新闻翻页（改range里面的就能翻页）
    newsurl = url.format(i + 1)
    newsary = parseListLinks(newsurl)
    news_total.extend(newsary)
    # parseListLinks(url)
    print(news_total)
    # df = pandas.DataFrame(news_total)                      #我这的numpy出了点问题 pandas库用不了，你试着运行一下
    # print(df)
    # df.to_excel('news.xlsx')                               #这是存到excel里的
