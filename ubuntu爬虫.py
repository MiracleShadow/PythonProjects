import requests
import re
from bs4 import BeautifulSoup

def request(url):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
    content = requests.get(url, headers=headers)
    return content

#获取html
def get_html_text(url):
    start_html = request(url)
    start_html.encoding = start_html.apparent_encoding
    Soup = BeautifulSoup(start_html.text, 'lxml')
    return Soup

def get_pre(url):
    Soup = get_html_text(url)
    all_pre = Soup.find('td', class_='code').find_all('pre')
    for a in all_pre:
        title = a.get_text()
    length = len(str(all_pre))
    if length > 30000:
        print("太长")
        return 0
    elif length < 100:
        print("太短")
        return 0
    print(title)

url = "http://pastebin.ubuntu.com/"
for i in range(25554564,25554570):
    rurl = url + str(i) + '/'
    get_pre(rurl)