import pymysql

# 创建主函数
def main():
    # 创建 数据库连接池 （从左到右 分别是 ip ; 端口号 ; 用户名 ; 密码 ; 数据库 ; 编码：）
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='Qwer12345', db='pymyuser', charset='utf8')

    try:
        # 使用 with as 创建游标对象， 在执行完 SQL 语句 使其自动关闭
        with conn.cursor() as cursor:
            # 插入数据 到 students 表中
            result = cursor.execute('INSERT INTO students VALUES("KFC",12,"nan")')
            # 判断是否成功插入
            if result == 1:
                print('添加成功')
            # 提交操作到数据库
            conn.commit()
    # 出现异常 数据插入/修改/删除 失败 则rollback (回滚)
    except pymysql.MySQLError as error:
        print(error)
        print("添加失败")
        conn.rollback()
    # 关闭连接
    finally:
        conn.close()

    print(conn)
if __name__ == '__main__':
    main()


