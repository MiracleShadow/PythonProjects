# coding=utf-8
from django.db import models

# Create your models here.

# 设置数据模型，该数据模型与数据库中需要设置的字段相互对应。
# User模型，Question模型
class User(models.Model):
    # CharField:定义字段类型，此处为字符串类型，使用CharField字段必须指定max_length最大长度的属性
    username = models.CharField(max_length = 30)
    passname = models.CharField(max_length = 20)

class Question(models.Model):
    content = models.CharField(max_length=100)
    # DateTimeField:创建日期时间的字段
    # auto_created:在提交问题的时候，自动填写该字段的值
    # null = True:允许该字段为空
    submit_time = models.DateTimeField(auto_created=True, null=True)
    # 记录该问题是由哪一个用户提交的
    # 把user用户作为问题quesetion的外键
    user = models.ForeignKey(User)