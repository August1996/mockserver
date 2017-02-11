#coding:utf-8
from django.db import models

# Create your models here.

# 对应就是一个服务器
class API(models.Model):
    name = models.CharField(max_length = 32,verbose_name = '服务器名称')    # API名称,用于显示
    path = models.CharField(max_length = 32,verbose_name = '服务器根路径')    # API路径,如果是uLink,那么地址为http://localhost/uLink
    def __unicode__(self):
        return self.name

# 对应一个服务器的路由
class Router(models.Model):
    name = models.CharField(max_length = 32,verbose_name = '路由名称')    # 路由名称,用于显示
    path = models.CharField(max_length = 128,verbose_name = '路由路径')   # 路由路径,如果对应的API.path是uLink,router.path为register,那么地址为http://localhost/uLink/register
    api = models.ForeignKey(API,verbose_name = '路由服务器')               # 隶属的API
    def __unicode__(self):
        return self.api.name + '->'+ self.name

# 对应一种响应,一个路由可以有多种不同的响应,随机返回
class Response(models.Model):
    name = models.CharField(max_length = 32,verbose_name = '响应名称')    # Response名称,用于显示
    json = models.TextField()    # 返回的json内容
    delay = models.IntegerField(verbose_name = '响应延迟')               # 服务器延迟多久返回
    router = models.ForeignKey(Router,verbose_name = '响应路由')     # 隶属的路由
    def __unicode__(self):
        r = self.router
        a = r.api
        name = a.name + '->' + r.name + '->' + self.name
        return name


