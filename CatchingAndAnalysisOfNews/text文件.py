import requests
from bs4 import BeautifulSoup
import os


class hnnu():
    def all_url(self, url):
        start_html = requests.get(url)
        start_html.encoding = start_html.apparent_encoding
        Soup = BeautifulSoup(start_html.text, 'lxml')
        all_a = Soup.find('td', class_='content').find('table').find_all('a')
        all_class_columnStyle = Soup.find('td', class_='content').find_all('table', class_='columnStyle')
        sum = 0
        arr = [0 for _ in all_a]
        for class_columnStyle in all_class_columnStyle:
            for i in class_columnStyle.find_all(attrs={"target": "_blank"}):
                arr[sum] = str(i.get_text())  # 将新闻的标题存入数组
                sum += 1
                # print(i.get_text()) 输出每则新闻的标题
                title = i.get_text()
                print(u'开始保存：', title)  ##加点提示不然太枯燥了
                path = str(title).replace(" ", '_')  ##我注意到有个标题带有 ？  这个符号Windows系统是不能创建文件夹的所以要替换掉
                print(path)
                self.mkdir(path)  ##调用mkdir函数创建文件夹！这儿path代表的是标题title哦！！！！！不要糊涂了哦！
        '''
        for a in all_a:
            title = a.get_text()
            print(u'开始保存：', title)  ##加点提示不然太枯燥了
            path = str(title).replace("?", '_')  ##我注意到有个标题带有 ？  这个符号Windows系统是不能创建文件夹的所以要替换掉
            self.mkdir(path)  ##调用mkdir函数创建文件夹！这儿path代表的是标题title哦！！！！！不要糊涂了哦！
            href = a['href']
            self.html(href)  ##调用html函数把href参数传递过去！href是啥还记的吧？ 就是套图的地址哦！！不要迷糊了哦！
        

    def html(self, href):  ##这个函数是处理套图地址获得图片的页面地址
        html = self.request(href)
        max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
        for page in range(1, int(max_span) + 1):
            page_url = href + '/' + str(page)
            self.img(page_url)  ##调用img函数

    def img(self, page_url):  ##这个函数处理图片页面地址获得图片的实际地址
        img_html = self.request(page_url)
        img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
        self.save(img_url)

    def save(self, img_url):  ##这个函数保存图片
        name = img_url[-9:-4]
        img = self.request(img_url)
        f = open(name + '.jpg', 'ab')
        f.write(img.content)
        f.close()
'''
    def mkdir(self,path):  ##这个函数创建文件夹
        path = path.strip()
        isExists = os.path.exists(os.path.join("D:\\News", path))
        if not isExists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("D:\\News", path))
            os.chdir(os.path.join("D:\\News", path))  ##切换到目录
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False

    def request(self, url):  ##这个函数获取网页的response 然后返回
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        return requests.get(url, headers=headers)

hnnu = hnnu()  ##实例化
hnnu.all_url('http://www.hnnu.edu.cn/s/21/t/148/p/11/i/1/list.htm')##给函数all_url传入参数  你可以当作启动爬虫（就是入口）