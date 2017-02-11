#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from mockserver.server.models import API,Router,Response
from mockserver.server import util
import random
import time

defaultResponse = '''{
    state_code: 400,
    err_msg: '请登录mockserver添加对应的响应结果'
}'''

def createJSONResponse(text):
    return HttpResponse(text,content_type = "application/json")

# Create your views here.
def server(request,api = None,router = None):
    print('request:' + request.scheme + '://' + request.get_host() + '/' + api + '/' + router)

    if util.isTextEmpty(api) or util.isTextEmpty(router):
        return createJSONResponse(defaultResponse)

    apiList = API.objects.filter(path = api)

    if len(apiList) == 0:
        return createJSONResponse(defaultResponse)

    print('Get APIs:')
    print(apiList)

    routerList = Router.objects.filter(api = apiList[0],path = router)

    if len(routerList) == 0:
        return createJSONResponse(defaultResponse)

    print('\nGet Routers:')
    print(routerList)

    responseList = Response.objects.filter(router = routerList[0])

    if len(responseList) == 0:
        return createJSONResponse(defaultResponse)
    
    print('\nGet Responses:')
    print(responseList)

    response = responseList[random.randint(0,len(responseList) - 1)]
    delay = response.delay
    result = response.json

    print('\nGet Result:')
    print(result)

    print('\nSleep:' + str(delay) + ' ms')

    time.sleep(delay)

    return createJSONResponse(result)

def index(request):
    return HttpResponse('Hello world');