# coding:utf-8
import urllib,urllib2

'''
1.get请求一般用于从服务端获取数据
2.get也支持向服务端发送少量数据，
3.从安全角度考虑，由于get方法中的数据都暴露在URL地址中，不安全
举例：
1、url中没有数据
http:\\www.baidu.com
2、url中携带少量数据
http:\\www.baidu.com？uername=123&id=3
'''

'''
1.POST请求一般用于向服务端传输数据，
原则上没有大小限制
2.从安全性考考虑，POST请求的数据被放入了请求体中，并不会在URL中暴露出来
'''
'''
客户端向服务器发起网络请求（Request）

'''
'''
服务器向用户客户端返回相应（Response）
1.状态行 状态码
200 服务器响应成功
304 采用缓存css等静态文件的内容
400 以4开头的状态码，属于客户端方面的错误，比如：URL地址错误/请求方法错误等
500 以5开头的状态码，属于
2.相应头 Content-Type/Content-Language
3.响应体 服务端向客户端返回的内容
'''


# urllib发送GET请求
# 1>先创建request请求对象
request = urllib2.Request('http://www.baidu.com/')
# 2>根据request发起请求
response = urllib2.urlopen(request)
# 3>urlopen返回了一个Response类的对象，通过read()方法，读取相应的数据
the_page = response.read()
assert isinstance(the_page, object)
print the_page
