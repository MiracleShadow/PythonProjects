# coding:utf-8
import re

# pattern = re.compile('my')

'''match()从开头匹配，只匹配一次'''
# res1 = re.match(pattern, 'mylovehaha')
# res2 = re.match(pattern, 'lovemyhaha')
# res3 = re.match(pattern, 'lovehahamy')

# print pattern
# print res1, res2, res3

# print res1.group()

'''search()从任意位置匹配，只匹配一次'''
# res1 = re.search(pattern, 'mylovehaha')
# res2 = re.search(pattern, 'lovemyhaha')
# res3 = re.search(pattern, 'lovehahamy')

# print res1.group()
# print res2.group()
# print res3.group()

'''findall()将所有符合条件的字符串都查找出来
    \d：一个数字
    + ：前一个字符的一个或多个
'''
# pattern1 = re.compile('\d+')
# res1 = re.findall(pattern1, '1abc234ddd5657ppp')
# print res1

string = '''my name is 
heihei your name
is haha
'''
'''re.S解决换行符的问题'''
pattern = re.compile(r'my(.*?)your(.*?)haha',re.S)
res = re.findall(pattern, string)
print res