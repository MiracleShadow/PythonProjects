import requests
from bs4 import BeautifulSoup
from workers import app 
@app.task
def crawl(url):
    print('正在抓取链接{}'.format(url))
    resp_text = requests.get(url).text
    soup = BeautifulSoup(resp_text, 'html.parser')
    return soup.find('h1').text