import re

str="作者：江亭  摄影：孙燕  审核：朱其永  上传：孙燕"
author=re.match('^(作者：)[\u4e00-\u9fa5]+',str,re.M)
if author:
    print(author.group())