# Pynysql 入门文档 #
##  导入Pymysql模块 ##
```cmd
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
            # 创建 表 Students 并指定 表结构
            result = cursor.execute('SQL 增删改语句')
            # 判断是否成功创建表
            if result == 1:
                print('判定')
            # 提交操作到数据库
            conn.commit()
    # 出现异常 数据插入/修改 失败 则rollback (回滚)
    except pymysql.MySQLError as error:
        print(error)
        print("添加失败")
        conn.rollback()
    # 关闭连接
    finally:
        conn.close()
```
## 查询语句