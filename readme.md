### MyBlog

本仓库是学习[《Flask Web开发实战》](http://helloflask.com/book)过程中的练手项目，并在原项目基础上做了改动。

原项目链接：[Blueblog](https://github.com/greyli/bluelog)。

#### 安装

```
$ git clone https://github.com/lyh081/myblog.git
$ cd mylog
$ pipenv install --dev
$ pipenv shell
$ flask forge
$ flask run
* Running on http://127.0.0.1:5000/
```

#### 博客后台管理

```
$ flask init
```
根提示输入用户名和密码即可用此用户名和密码登录。

#### 主要改动

1. 将新建博文由在线编辑改为上传Markdown文件，并支持在Markdown文档开头用Yaml配置Title以及Category。

配置示例：
```
---
title: Python

date: 2018-12-30 14:11:15

category: 
    - CS 
---
```

2. 新建博文开头配置的Category若现数据库中没有，则新建。

#### 项目拓展计划

此项目作为练习项目，会随着本人的学习拓展，计划内的拓展方向包括
+ 加入Ajax，使用户操作更加流畅
+ 添加多语言支持
+ 编写对应的Web API

待续……