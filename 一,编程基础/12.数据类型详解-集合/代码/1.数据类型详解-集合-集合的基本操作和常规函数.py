#  集合的基本操作和常规函数

# 定义集合
vars = {123,'abc',False,'love',True,(1,2,3),0,3.1415,'123'}
# 1。无序。
# 2。布尔类型 True 表示为 1，False 表示为 0，布尔和数字只存在一个
# 3。元素的值不能重复
# {0, 'abc', 'love', True, 3.1415, (1, 2, 3), 123}

# 检测集合中的值
res = '123' in vars
res = '123' not in vars

# 获取集合中元素的个数 len()
# res = len(vars)

# 集合的遍历
# for i in vars:
#     print(i,type(i))

# 向集合中追加元素 add()
res = vars.add('def')

# 删除集合中的元素 随机删除一个元素并返回  abc False True 3.1415
# r1 = vars.pop()


# 指定删除集合中的元素 remove() 返回None，不存在则报错
# res = vars.remove('aaa')

# discard 指定删除集合中的元素，不存在也不会报错
# res = vars.discard('aaa')

# clear() 清空集合
# res = vars.clear()

# update(others) 更新集合，添加来自 others 中的所有元素。
res = vars.update({1,2,3,4,5})

#  当前集合中的浅拷贝并不存在 深拷贝的问题
res = vars.copy()
'''
当前集合中的浅拷贝并不存在 深拷贝的问题
    因为集合中的元素都是不可变，包括元组和冰冻集合
    不存在拷贝后，对集合中不可变的二级容器进行操作的问题
'''

# 冰冻集合(了解)
v = frozenset((1,2,3))
print(v)


