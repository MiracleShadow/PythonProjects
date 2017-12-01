#coding:utf-8

#目的将每一页的图片存入一个单独的文件夹内，保存到本地。
import urllib,urllib2
import os
#bs4的作用是解析html源代码
from bs4 import  BeautifulSoup

class Spiderlmage(object):
    # 网站的基本路径
    # start_page_num：图片下载的起始页
    # end_page_name：图片下载的结束页
    def __init__(self, baseURL,start_page_num,end_page_name):
        self.baseURL =baseURL
        self.start_page_num = start_page_num
        self.end_page_name = end_page_name

    # 定义获取源代码的函数
    def get_html_code(self):
    # 1>拼接完整路径
        try:
            url = self.baseURL+'index_%s.html'%str(self.start_page_num)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
        except Exception, e:
            print '链接失败：',e
            return None
        else:
            # 响应成功，返回网页源代码，交友下一个函数进行解析数据。
            return response.read()
    # 定义解析网页源代码的函数
    def get_all_images_by_html(self,pageCode):
        # pageCode:接收网页源代码数据的形参
        print '正在下载第%s页数据...'%self.start_page_num
        soup = BeautifulSoup(pageCode, 'lxml')
        # 采用lxml解析源代码
        # select（）函数，是soup对象提供的通过类名/id等属性获取边坡前的函数，返回的是个列表。
        for img in soup.select('.ali a img'):
            # 获取img标签的src和alt属性的值
            img_src = img.get('src')
            # print img_src
            img_alt = img.get('alt')
            # print img_alt
            # 根据图片的绝对路径下载图片
            # urlretrieve()两个参数：1>图片地址 2>设置图片的名称
            urllib.urlretrieve(img_src, '%s.jpg'%img_alt)
    # 定义开始爬虫的函数
    def start_spider(self):
        while self.start_page_num <= self.end_page_name:
            html = self.get_html_code()
            # 声明变量，记录文件夹名称，同一目录上
            directory = '%s-pages'%self.start_page_num
            # 在当前目录下创建文件夹
            os.mkdir(directory)
            # 因为默认的工作目录是当前文件所在的目录，所以创建的新目录需要进入才能将图片存放在目录中
            os.chdir(directory)
            # 进入新目录中，开始下载图片
            self.get_all_images_by_html(html)
            # 返回到上一级目录，在新建下一页图片对应的目录
            os.chdir(os.path.pardir)
            # 当前页码+1
            self.start_page_num += 1

img_obj = Spiderlmage('http://www.ivsky.com/tupian/ziranfengguang/',1,10)
img_obj.start_spider()
# html = img_obj.get_html_code()
# img_obj.get_all_images_by_html(html)
