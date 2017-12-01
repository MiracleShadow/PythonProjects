# coding:utf-8
import urllib, urllib2
import re

'''
# 定义用于下载段子内容的函数
# 形参pageNum表示页码
def dowload_by_pae_code(pageNum):
    # 1>根据页码pageNum拼接出完整的url地址
    url = 'https://www.qiushibaike.com/hot/page/' + str(pageNum) + '/'
    # 2>设置User-Agent请求头字段，伪装成浏览器去访问网址
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'
    }
    # 3>创建网络亲求对象
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    res = response.read()
    # print len(res)
    # print res
    # 5>利用正则表达式，从网页代码中匹配数据。res结果是字符串类型的数据。
    # 匹配用户名和段子内容
    pattern = re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>', re.S)
    # .*?：省略<div class="author clearfix">后面的所有内容，直到遇见<he>标签。因为div和h2标签之间还有一些不需要的标签存在，所有直接省略。只匹配关键内容即可
    # (.*?):表示分组信息，用于提取小括号中的所有内容
    # 6>根据正则表达式对象，从目标字符串中提取用户名和内容
    content_list = re.findall(pattern, res)
    for x in xrange(0, len(content_list)):
        content = content_list[x]
        author = content[0]
        text = content[1]
        print '作者：', author
        print '内容：',text
    # print content_list
'''
class Tools(object):
    # 从结果中匹配\n
    replace_n = re.compile(r'\n')
    # 从结果中匹配<br>或者<br/>
    replace_br = re.compile(r'<br>|<br/>')
    # 从结果中匹配多余的标签
    replace_element = re.compile(r'<.*/>', re.S)
    def replace_string(self, result):
        # 昵称、年龄、内容、好笑数、评论数
        name = re.sub(self.replace_n, '', result[0])
        content = re.sub(self.replace_n, '', result[2])
        content = re.sub(self.replace_br, '\n', content)
        content = re.sub(self.replace_element, '', content)
        result_data = (name, result[1], content, result[3], result[4])
        # 返回经过处理的的元组
        return result_data

class QSBK(object):
    def __init__(self):
        # 初始化基础路径
        self.baseURL = 'https://www.qiushibaike.com/hot/page/'
        # 初始化User - Agent
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'
        }
        # 初始化Tools类对象
        self.tool = Tools()

    def get_page_code(self, pageNum):
        # 根据页码拼接完整的URL
        url = self.baseURL + str(pageNum)
        # 创建请求
        request = urllib2.Request(url, headers = self.headers)
        # 发起请求
        try:
            response = urllib2.urlopen(request)
        except Exception, e:
            print '链接糗事百科失败，原因：%s'%e
            return None
        else:
            # 响应成功,返回网页源代码
            return response.read()

    # 根据上面的函数获取的源代码，解析数据。单独定义一个解析数据的函数
    def get_data_by_page_code(self, html):
        # 生成正则表达式对象
        pattent = re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?Icon">(.*?)</div>.*?class="content">.*?<span>(.*?)</span>.*?<i class="number">(.*?)</i>.*?<i class="number">(.*?)</i>', re.S)
        results = re.findall(pattent, html)
        # 通过Tools类过滤数据
        # results_list = []
        for res in results:
            result = self.tool.replace_string(res)
            print '用户名：%s    年龄：%s    好笑数：%s    评论数：%s'%(result[0], result[1], result[3], result[4])
            print '内容：',result[2]
        #     results_list.append(result)
        # return results_list



if __name__ == '__main__':
    qsbk = QSBK()
    html = qsbk.get_page_code(1)
    qsbk.get_data_by_page_code(html)