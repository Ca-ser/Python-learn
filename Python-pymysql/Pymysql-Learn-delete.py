import pymysql

# 创建主函数
def main():
    # 创建 数据库连接池 （从左到右 分别是 ip ; 端口号 ; 用户名 ; 密码 ; 数据库 ; 编码：）
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='Qwer12345', db='pymyuser', charset='utf8')

    try:
        # 使用 with as 创建游标对象， 在执行完 SQL 语句 使其自动关闭
        with conn.cursor() as cursor:
            # 创建 表 Students 并指定 表结构
            result = cursor.execute('DELETE from students where name = "zwt" ')
            # 判断是否成功删除
            if result == 1:
                print('删除成功')
            # 提交操作到数据库
            conn.commit()
    # 出现异常 数据插入/修改 失败 则rollback (回滚)
    except pymysql.MySQLError as error:
        print(error)
        conn.rollback()
    # 关闭连接
    finally:
        conn.close()

    print(conn)
if __name__ == '__main__':
    main()
