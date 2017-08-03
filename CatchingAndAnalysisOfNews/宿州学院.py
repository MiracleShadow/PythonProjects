import requests
from bs4 import BeautifulSoup


def getNewsdetails(newsurl):
    result = {}
    r = requests.get(newsurl)
    r.encoding = r.apparent_encoding
    soup = BeautifulSoup(r.text, 'html.parser')
    result['title'] = soup.select('b')[0].text
    result['article'] = ' '.join(p.text.strip() for p in soup.select('.MsoNormal'))
    result['others'] = soup.select('td')[7].text.strip()
    result['newssource'] = newsurl
    return result


def parserListLinks(url):
    newsdetails = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for ent in soup.select('a')[0:20]:
        url = ent['href']
        realurl = 'http://www.ahszu.edu.cn' + url
        newsdetails.append(getNewsdetails(realurl))
    return newsdetails


url = 'http://www.ahszu.edu.cn/Article/ShowClass.asp?ClassID=1&page={}'
news_total = []
for i in range(1):
    newsurl = url.format(i + 1)
    newsary = parserListLinks(newsurl)
    news_total.extend(newsary)
    parserListLinks(url)
print(news_total)
