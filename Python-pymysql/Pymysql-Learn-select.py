import pymysql

# 创建主函数
def main():
    # table = input("请输入要查询的表")
    # name = input("请输入要查询的姓名")
    # 创建 数据库连接池 （从左到右 分别是 ip ; 端口号 ; 用户名 ; 密码 ; 数据库 ; 编码：;游标类型 (DictCursor 字典, cursor 元组) ）
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='Qwer12345', db='pymyuser', charset='utf8', cursorclass=pymysql.cursors.DictCursor )

    try:
        # 使用 with as 创建游标对象， 在执行完 SQL 语句 使其自动关闭
        with conn.cursor() as cursor:
            # 查询 表中 的 数据
            cursor.execute('SELECT name as na ,age as age ,grade as sex from students ')
            # 多种查询方法
            # cursor.fetchall()
            # cursor.fetchone()
            # cursor.fetchmany()

            # 使用字典型游标查询
            for row in cursor.fetchall():
                print(row['na'], end='\t')
                print(row['age'], end='\t')
                print(row['sex'])

            # 使用默认游标查询
            # for row in cursor.fetchall():
            #     print(f'姓名： {row[0]}')
            #     print(f'年龄： {row[1]}')
            #     print(f'性别： {row[2]}')
    # 关闭连接
    finally:
        conn.close()

    print(conn)
if __name__ == '__main__':
    main()


