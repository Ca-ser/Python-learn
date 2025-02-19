# Pynysql 入门文档 #

## 导入Pymysql模块 ##

```Powershell
使用pip 安装PyMysql
pip install pymysql
```

## 配置连接池 连接数据库

```python
    # 创建 数据库连接池 （从左到右 分别是 ip ; 端口号 ; 用户名 ; 密码 ; 数据库 ; 编码：）
conn = pymysql.connect(host='localhost', port=3306, user='root', password='*******', db='databaseName', charset='utf8')
```

## 创建游标 为增删改查做准备

```python
 with conn.cursor() as cursor:
```

## 查询语句