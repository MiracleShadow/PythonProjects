import requests
from bs4 import BeautifulSoup

# print("{:^10}\t{:^100}\t{:^100}".format("时间", "新闻标题","新闻地址"))
for i in range(18):  # 新闻页数 range() <7191 网页限制  目前共424页
    if i == 0:  # 判断是否为第一页
        a = "http://www.ahnu.edu.cn/3194/"  # 第一页
        # print(a)
    else:
        if i % 17 == 0:  # 每增加17条新闻，翻页
            b = ''.join('%d') % i  # 给新闻url加后缀标明页数
            a = "http://www.ahnu.edu.cn/3194/" + b  # 后续页
            # print(a)
            r = requests.get(a)
            r.encoding = r.apparent_encoding
            # print (r.text)
            soup = BeautifulSoup(r.text, 'html.parser')
            for i in range(17):  # 每页有17条新闻
                time = soup.select('.conListTime')[i]  # 取得新闻时间
                # print(time.text)
                title = soup.select('.conListWord')[i]  # 取得新闻标题
                # print(news.text)
                href = soup.select('.rigthConBox-conList')[i]  # 取得新闻url
                # print(href['href'])
                print(time.text, title.text, href['href'])  # 打印时间，标题，url


                # print("{:^10}\t{:^100}\t{:^70}".format(time.text,title.text,href['href'])) #格式化输出
                def getNewsDetail(newsurl):
                    result = {}
                    r = requests.get(newsurl)
                    r.encoding = r.apparent_encoding
                    soup = BeautifulSoup(r.text, 'html.parser')
                    title = soup.select('.readTitle')[0].text  # 新闻标题
                    time = soup.select('.readInfoList-top')[0].text.strip()
                    text = ''.join(p.text for p in soup.select('p')[8:-4])
                    a = text  # 段落由一个个标签组成 取出
                    editor = result['editor'] = soup.select('.readInfoList-topAdd')[0].text.strip()  # 取得作者
                    print(title + "\n" + time + "\n" + a + "\n" + editor + "\n")


                a = href['href']
                getNewsDetail(a)
