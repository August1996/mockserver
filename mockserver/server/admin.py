#coding:utf-8

from django.contrib import admin
from mockserver.server.models import API,Router,Response
# Register your models here.
# admin.site.register(API)
# admin.site.register(Router)
# admin.site.register(Response)

class APIAdmin(admin.ModelAdmin):
    list_display = ('name', 'path')         #把字段信息全部显示出来
    # search_fields = ('name')              #添加search bar，在指定的字段中search


class RouterAdmin(admin.ModelAdmin):
    list_display = ('name', 'path')
    # list_filter = ('publication_date',)   #页面右边会出现相应的过滤器选项
    # date_hierarchy = 'publication_date'   #只接受日期类型的字段名
    # ordering = ('-publication_date',)     #排序

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('name','delay')

admin.site.register(API,APIAdmin)
admin.site.register(Router, RouterAdmin)
admin.site.register(Response, ResponseAdmin)