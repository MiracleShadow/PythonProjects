import requests
from bs4 import BeautifulSoup
import pandas


def getNewsDetail(newsurl):
    r = requests.get(newsurl)
    soup = BeautifulSoup(r.text, 'html.parser')
    result = {'title': soup.select('.arti-title')[0].text.strip()}
    result['newssource'] = newsurl
    result['time'] = soup.select('.arti-update')[0].text.strip()
    result['article'] = soup.select('.read')[0].text.strip()
    result['editor'] = soup.select('.arti-publisher')[0].text.strip()
    return result


def parserListLinks(url):
    newsdetails = []
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for ent in soup.select('.columnStyle a'):
        url = ent['href']
        realurl = 'http://www.tlu.edu.cn' + url
        newsdetails.append(getNewsDetail(realurl))
    return newsdetails


url = 'http://www.tlu.edu.cn/s/1/t/371/p/11/i/{}/list.htm'
news_total = []
for i in range(2):
    newsurl = url.format(i + 1)
    newsary = parserListLinks(newsurl)
    news_total.extend(newsary)
    parserListLinks(url)
# print(news_total)
df = pandas.DataFrame(news_total)
print(df)
