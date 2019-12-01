# 其它运算符


# in  not in  检测成员是否存在
s = 'iloveyoiutosimida'
# s = ['love','io','you']
# s = ('i','love','you')
# s = {'i','love','you'}
# s = {1:'i',2:'love',3:'you'} # 如果是字典类型 只能检测 键
# print(2 in s) # 检查 love 字符串 是否存在与 s变量中
# print('loves' not in s) # 检查 love 字符串 是否 不存在 与 s变量中


# id() 变量的 id属性获取，函数用于获取对象内存地址
a = 10
b = 10

# is is not 检测两个变量是否引用了同一个对象

#is 是判断两个标识符是不是引用自一个对象
print(id(a),id(b))
print(a is b)

# is not 是判断两个标识符是不是引用自不同对象
print(a is not b)


# Python运算符优先级
a = 10 and (30 and 0) or 20 and 15 or 35

print(a)



