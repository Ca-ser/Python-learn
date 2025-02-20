import redis


def main():
    client = redis.Redis(host='localhost', port=6379, password='')

    # print(client)
    # ex = exceed the time limit

    client.set('username', 'hellokitty', ex=300)  # 向Redis 中存入key ： username; Value："hello Kitty"; 存活时间 300 ms
    print(client.ttl('username'))  # 查询键值对的存活时间
    print(client.get('username').decode())  # 根据键 来查询值
    client.set('nickname', '骆昊')
    print(client.get('nickname').decode())  # decode() 将字节数据转换成子字符串
                                            # 可传参数:Encoding指定编码格式
    client.set('yuting', '300')             # Error 表示当编码过程中遇到无法 解码的数据时的处理方式
                                            # "ignore"：忽略无法解码的字节。
                                            # "replace"：用 ? 替换无法解码的字节。
    client.incr('yuting')
    client.incrby('yuting', 50)
    print(int(client.get('yuting').decode()))
    client.hset('stu1', 'id', '1001')
    client.hset('stu1', 'name', '王大锤')
    print(client.hgetall('stu1'))
    print(client.hget('stu1', 'name'))
    client.rpush('list1', 10, 20, 30, 40)
    print(client.lrange('list1', 0, -1))


if __name__ == '__main__':
    main()
