
# Python Flask最佳实践

## 前沿

Python Flask 是一个很简单方便的Web框架，

轻轻松松就可以完成一个Web 或者纯Web API。

前阵子需要起一个简单的Web + 脚本项目，折腾flask的时候发现没找到比较顺手的脚手架教程。

摸索了好一些知识，踩了一下坑什么的，

最后站在巨人肩膀上更新个教程。


## 代码项目结构

正儿八经一个项目工程，遵循 三层架构 + MVC模型 对项目代码有严格的划分，

对这两个概念不太了解的朋友可以自行课后补习一下。

说明如下:

- src 所有的项目代码文件
- src/service 逻辑层代码
- src/model 业务实体
- src/db 数据库相关，包括model定义和dao SQL查询
- src/sdk 依赖的外部接口
- src/job 后台进程启动的Job，一般都是通过API启动的后台任务
- src/utils 工具类，config 配置类也在里面
- src/app.py flask app 启动项
- manage.py flask.cli 启动入口 api + job
- Dockerfile Docker打包流程
- debug.py 本地debug 启动入口
- requirements.txt 所有的依赖包
- .vscode/launch.json vs code debug 配置

## 开搞

废话多说两句，我比较喜欢requirements这种包组织方式，其他的就看自己了。

### requirements.txt

```txt
flask
flask-swagger
flask-swagger-ui
flask-bootstrap
SQLAlchemy
pymysql
pydantic
requests
loguru
gunicorn

```

简单说明

- flask是核心包，flask-swagger + flask-swagger-ui 是用来做Swagger UI的，flask-bootstrap 用来乱糊 HTML页面的
- SQLAlchemy + pymysql +  一个是数据库ORM框架，一个是数据库驱动
- pydantic 用来配合SQLAlchemy完成Model数据转换，解决一些奇怪的序列化反序列化问题
- requests 用来对接外部HTTP接口或者写爬虫脚本
- loguru 简易日志框架，from loguru import logger 就完事了
- gunicorn 多进程部署
