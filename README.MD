# MockServer
## 前言
某公司的某个开发小组人员分配如下:

人员|工作
---|---
小A|前端
小B|Android
小C|IOS
小D|后台

出于维护性和兼容性等的考虑.`三端(前端,Android,IOS)`决定使用`resuful`的设计思想.

随着开发的进行,小A 小B 小C陆续编写接口给后台.因为后台忙不过来,所以接口不能按时提交.

这时小A,小B,小C的工作也就阻塞了,这样就造成三端过度依赖后台.接入数据和测试的工作就一天拖一天.

于是项目的整体进度开始延长...

**既然我们已经知道接口是怎么样的了,那么为什么我们不自己弄一台服务器,专门来返回对应接口的数据呢?**

`MockServer`就是为了解决这一尴尬的局面.字面意思很浅显易懂,就是模拟数据的服务器.

本项目基于`Python`的`Django`框架开发.

依赖的python包:
	* django			框架
	* django-suit	主题

数据库:sqlite

## 安装

### Linux
#### 安装Python
Linux下自带Python环境,所以就不需要再配置Python环境了
只需要安装依赖包

#### 安装PIP
> pip是python的包管理工具

* 下载[get-pip](https://bootstrap.pypa.io/get-pip.py
)
* 运行`get-pip`,脚本会自动安装

```bash
sudo python get-pip.py
```

#### 安装依赖包
主要是安装前言提到的两个包
```bash
sudo pip install django django-suit
```

##### 安装Sqlite3
Debian系的安装方法
```
sudo apt-get install sqlite3
```

#### 项目克隆
克隆本项目到本地
```bash
git clone https://github.com/August1996/mockserver
```

#### 启动项目
进入项目工作目录并且启动服务器
```bash
cd mockserver
python manage.py runserver
```

如果启动成功,会返回下面响应
```bash
Performing system checks...

System check identified no issues (0 silenced).
February 11, 2017 - 06:08:22
Django version 1.8.6, using settings 'mockserver.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## 使用
### 管理页面
#### 地址
如果服务器地址为`http://127.0.0.1:8000/`
那么请打开`http://127.0.0.1:8000/admin`

![登录界面](https://raw.githubusercontent.com/August1996/mockserver/master/screenshots/login.png)

#### 登录
默认登录信息:
```
admin
mockserver
```

![管理界面](https://raw.githubusercontent.com/August1996/mockserver/master/screenshots/admin.png)

#### 添加接口
##### API组成
一个接口由三部分组成

名称|意义
---|---
API|代表一个服务器
Router|代表一个接口
Response|代表一种返回结果

##### 例子
假如现在我们有一个test项目那么我们添加API:
```
服务器名称:	测试
服务器根路径:	test
```

![添加API](https://raw.githubusercontent.com/August1996/mockserver/master/screenshots/add_api.png)

假如test项目有个register的接口,我们添加Router:
```
路由名称:		注册
路由路径:		register
路由服务器:	测试
```

![添加Router](https://raw.githubusercontent.com/August1996/mockserver/master/screenshots/add_router.png)

假如test项目的register接口有两种返回结果,返回时延迟1秒(模拟网络慢),我们添加Response
```
响应名称:		注册失败
Json:
{
    "status_code": 300,
    "message": "注册失败",
    "objs": {
        "user_token": "XXXXX"
    }
}
响应延迟:		1
响应路由:		测试->注册
```

```
响应名称:		注册成功
Json:
{
    "status_code": 200,
    "message": "注册成功",
    "objs": {
        "user_token": "XXXXX"
    }
}
响应延迟:		1
响应路由:		测试->注册
```

![添加Response](https://raw.githubusercontent.com/August1996/mockserver/master/screenshots/add_response.png)

### 访问
**最后我们访问`http://127.0.0.1:8000/test/register`这个地址,MockServer就会随机返回上面的一种结果**

![结果返回](https://raw.githubusercontent.com/August1996/mockserver/master/screenshots/result.png)

## 参考
具体参考Python以及Django框架的用法.



