# 写入相关函数

# vars = 5211  # int类型无法写入
# vars = ['hello','world','1','2']
# vars = {'name':'zs','age':'22'}
# with open('./test/4.txt','w',encoding='utf-8') as fp:
#     # fp.write(vars)  # 只能写入字符串类型数据
#     fp.writelines(vars)  # 可以写入容器类型数据，注意容器中的元素也必须是字符串类
#

# 读取相关函数
# with open('./test/4.txt','r',encoding='utf-8') as fp:
    # fp.seek(3)  # 设置指针的位置
    # res = fp.read()  # 默认从当前指针开始读取到最后
    # res = fp.read(3)   # 设置读取的字节长度
    # res = fp.readline()  # 一次只读取一行内容
    # print(res)
    # res = fp.readline(3) # 可以读取当前行中的指定字节数
    # res = fp.readlines()  # 一次读取多行数据，每一行作为一个元素，返回一个列表
    # res = fp.readlines(6)  # 按照行进行读取，可以设置读取的字节数，设置的字节数不足一行按一行算
    # print(res)


# seek() 设置文件指针位置
# with open('./test/4.txt', 'r+', encoding='utf-8') as fp:
#     # a+模式，指针默认在文件的最后，所以直接读是读取不到内容的
#     # fp.seek(0)  # 把文件指针设置到文件的开头位置
#     fp.seek(10)   # 设置文件指针的位置
#     fp.seek(0,2)  # 0,2是把文件指定设置在文件的末尾
#     # fp.write('\n00000')
#     res = fp.read()

# truncate() 截断文件内容
with open('./test/4.txt','r+',encoding='utf-8') as fp:
    res = fp.truncate(5)
    # 默认从文件的首行的首个字符开始进行截断，截断的长度为size个字节数，
    # size如果为0，则从当前位置截断到最后

# print(res)



# 练习题： 使用数据写入文件的方式，完成一个注册和登录 
