# 登录和注册功能的合并


# 专门定义数据变量，存放已经注册的用户信息
userlist = [] # 存放所有的用户名
pwdlist = [] # 存放所有的用户密码
blacklist = [] # 存放所有的黑名单用户


# 读取所有数据的方法
def readallusers():
    # 读取所有的注册信息 使用a+模式打开文件，在调整指针位置，防止文件不存在时报错
    with open('./user.txt','a+',encoding='utf-8') as fp:
        fp.seek(0) # 调整当前的的指针位置到文件头部
        res = fp.readlines()  # 按照每一行读取所有的用户数据
        for i in res:  # 循环读取的每一行数据
            r = i.strip()  # 处理每一个换行 admin:123\n ==> admin:123
            arr = r.split(':')  # admin:123 ==> ['admin','123']
            userlist.append(arr[0]) # 把用户名追加到 用户名列表中
            pwdlist.append(arr[1])  # 把用户对应的密码 追加到 用户密码 列表中

    # 获取黑名单数据
    with open('./black.txt','a+',encoding='utf-8') as fp:
        fp.seek(0)
        res = fp.readlines()
        for i in res:
            blacklist.append(i.strip())


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


# 封装函数实现登录功能
def login():
    # 定义变量 控制登录的外循环
    islogin = True
    # 定义变量，用户密码的错误次数的检测
    errornum = 3

    # 循环执行用户的登录
    while islogin:
        # 获取用户登录时输入的用户名
        username = input('欢迎登录，请输入您的用户名：')
        # 检测当前用户名是否存在
        if username in userlist:
            # 检测用户是否属于锁定状态？ 判断是否在黑名单中
            if username in blacklist:
                print('当前用户属于锁定状态，不可登录，请去忏悔把。。。')
            else:
                # 定义循环，执行密码输入
                while True:
                    # 让用户输入密码
                    pwd = input('请输入您的密码：')
                    # 获取用户名在用户列表中的索引。
                    inx = userlist.index(username)
                    # 检测用户输入的密码是否正确
                    if pwd == pwdlist[inx]:
                        print('登录成功')
                        # 结束循环
                        islogin = False # 结束外循环变量
                        break  # 结束内循环
                    else:
                        # 密码错误，则修改次数变量
                        errornum -= 1
                        # 判断当前的密码错误次数 == 0
                        if errornum == 0:
                            print('曾经有那么几次机会摆在你的面前。你没有把握住，恭喜你，成功的锁定了你的账户，请联系相关人员进行忏悔把！')
                            # 如何才能锁定账户信息？ 把需要锁卡的用户拉入黑名单
                            with open('./black.txt','a+',encoding='utf-8') as fp:
                                fp.write(username+'\n')
                            # 结束循环
                            islogin = False  # 结束外循环变量
                            break  # 结束内循环
                        else:
                            print(f'密码输入错误，请重新输入密码,你还有{errornum}次机会')
        else:
            #用户名不存在
            print('用户名错误，请重新输入')


# 判断当前的脚本是否作为一个主进程脚本在执行
if __name__ == '__main__':
    # 这里的代码，只有在使用python解释器直接运行时才执行
    # 如果当前的脚本。作为了一个模块被其它的文件导入后使用，那么这个地方的代码不会执行
    # 因此这个地方的代码 适合写当前脚本中的一些测试，这样不会影响其它脚本

    # 调用初始化方法,加载数据
    readallusers()

    while True:
        vars = '''
        ***************************************
        **    登录(1)  注册(2) 退出(任意内容)    **
        ***************************************
        '''
        print(vars)

        # 让用户选择对应的操作
        num = input('请输入对应的序号，体验功能:')

        if num == '1':
            login()
        elif num == '2':
            register()
        else:
            print('欢迎下次体验。。。')
            break


# 扩展题： 可以实现 购物，定义一些商品和对应的价格，每个用户有100原，完成购物即扣款






