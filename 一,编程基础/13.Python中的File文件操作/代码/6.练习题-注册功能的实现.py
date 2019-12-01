# 注册功能

# 专门定义数据变量，存放已经注册的用户信息
userlist = [] # 存放所有的用户名
pwdlist = [] # 存放所有的用户密码

# 读取所有的注册信息 使用a+模式打开文件，在调整指针位置，防止文件不存在时报错
with open('./user.txt','a+',encoding='utf-8') as fp:
    fp.seek(0) # 调整当前的的指针位置到文件头部
    res = fp.readlines()  # 按照每一行读取所有的用户数据
    for i in res:  # 循环读取的每一行数据
        r = i.strip()  # 处理每一个换行 admin:123\n ==> admin:123
        arr = r.split(':')  # admin:123 ==> ['admin','123']
        userlist.append(arr[0]) # 把用户名追加到 用户名列表中
        pwdlist.append(arr[1])  # 把用户对应的密码 追加到 用户密码 列表中

# 封装一个函数 完成注册功能
def register():
    # 定义一个变量。用于控制外循环
    site = True
    # 循环执行 用户名输入操作
    while site:
        # 用户输入用户名
        username = input('欢迎注册，请输入用户名：')
        # 用户名需要检测是否已经存在
        if username in userlist:
            print('当前用户名已经存在，请更换用户名')
        else:
            # 循环输入密码，如果都正确，循环结束，
            while True:
                # 输入密码
                pwd = input('请输入密码：')
                # 检测密码从长度不能低于3位
                if len(pwd) >= 3:
                    # 输入确认密码
                    repwd = input('请输入确认密码：')
                    # 检测确认密码是否和密码一致
                    if pwd == repwd:
                        # 用户名和密码都正确，就可以写入文件  用户名：密码
                        # 打开文件，写入数据
                        with open('./user.txt','a+',encoding='utf-8') as fp:
                            fp.write(f'{username}:{pwd}\n')
                        print(f'注册成功：用户名：{username}')
                        # 结束循环
                        # 结束外循环
                        site = False
                        # 结束内循环
                        break
                    else:
                        print('两次密码不一致，请重新输入')
                else:
                    print('密码格式不正确')


register()


