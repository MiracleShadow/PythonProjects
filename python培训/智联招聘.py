# coding:utf-8
import urllib2, re
import xlwt

# 定义爬虫类
class ZLZP(object):
    def __init__(self, workname, citys):
        # 记录所查的工作岗位和工作地点
        self.workname = workname
        # 记录搜索结果也的基础网址
        self.url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?'
        # 处理基础网址后面追加的参数
        args = 'kw=%s&jl='%workname
        # 工作地点，每两个工作地点之间有一个%2B进行拼接多个工作地点，但是最后一个地点没有%2B
        # %2B在URL中表示+号的意思
        for city in citys:
            if city == citys[-1]:   # 如果是最后一个城市
                args += city
            else :                  # 如果不是最后一个城市
                args += city + '%2B'
        # kw=python&jl=北京&2B上海
        self.url += args
        # 记录工作地点
        self.citys = citys
        # 设置请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'
        }
    # 定义根据页码获取html源代码的函数
    def get_page_code(self, pageNum):
        # 根据pageNum拼接完整的URL地址
        getUrl = self.url + '&p=%s'%pageNum
        # 创建request请求对象
        request = urllib2.Request(getUrl, headers=self.headers)
        try :
            response = urllib2.urlopen(request)
        except Exception, e :
            print '获取第%s页失败，原因：'%pageNum
            return None
        else :
            return response.read()
    # 定义获取网页总职位数的函数
    def get_total_number(self, html):
        # 1>创建正则表达式对象
        pattern = re.compile(r'<span class="search_yx_tj">.*?<em>(.*?)</em>', re.S)
        rs = re.search(pattern, html)
        total_number = int(rs.group(1))
        print '总职位数：%s个'%total_number
        # 根据总职位数计算总页数
        if total_number%60 == 0:
            # 刚好除尽
            self.totalPage = total_number / 60
        else :
            # 将余下的数据在单独增加一页进行展示
            self.totalPage = total_number / 60 + 1
    # 定义提取工作信息的函数
    def get_all_data(self, html):
        # 1>创建正则表达式对象
        pattern = re.compile(r'<table.*?class="newlist.*?<td class="zwmc.*?<a.*?>(.*?)</a>.*?<td class="gsmc.*?_blank">(.*?)</a>.*?<td class="zwyx">(.*?)</td>.*?<td class="gzdd">(.*?)</td>', re.S)
        results = re.findall(pattern, html)
        res_data = []
        for result in results:
            # print '职位描述：%s-公司名称：%s-职位月薪：%s-工作地点：%s' % (result[0], result[1], result[2], result[3])
            remove_element = re.compile(r'<.*?>', re.S)
            zzmc = re.sub(remove_element, '', result[0])
            res_tuple = (zzmc, result[1], result[2], result[3])
            # 将处理过后的元组添加到列表
            res_data.append(res_tuple)
        return res_data
    # 定义开始爬虫函数
    def start(self):
        # 1>获取首页源代码
        html = self.get_page_code(1)
        if html ==None:
            print '首页源代码获取失败！'
            return
        # 2>提取总职位数
        self.get_total_number(html)
        # 3>根据总页数，循环下载数据
        # 配置本地excel文件的相关信息
        workbook = xlwt.Workbook(encoding='utf-8')
        # 设置表头
        sheet = workbook.add_sheet(u'Python职位表')
        sheet.write(0, 0, '职位名称')
        sheet.write(0, 1, '公司名称')
        sheet.write(0, 2, '职位月薪')
        sheet.write(0, 3, '工作地点')
        row_count = 1   # 写入excel表的行号
        for x in xrange(1, 11):
            print '正在写入第%s页数据……'%x
            html = self.get_page_code(x)
            if html == None:
                # 如果获取本页的源代码是空，则跳过本次数据的写入，执行下一次循环
                continue
            res_data = self.get_all_data(html)
            # 将res_data列表中的数据写入到本地excel表中
            for result in res_data:
                sheet.write(row_count, 0, result[0])
                sheet.write(row_count, 1, result[1])
                sheet.write(row_count, 2, result[2])
                sheet.write(row_count, 3, result[3])
                row_count += 1  # 每写入一行，行号加一
            # 将写入的数据生成到本地
            workbook.save(u'职位信息.xls')


if __name__ == '__main__':

    workname = raw_input('请输入要查询的工作名称：')
    citys = []
    # 最多只能添加4个城市
    while len(citys) <= 4:
        city_name = raw_input('请输入意向城市，最多输入4个城市，输入Q结束城市输入：')
        if city_name == 'Q':
            break
        citys.append(city_name)
    zlzp = ZLZP(workname, citys)
    zlzp.start()








