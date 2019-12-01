#  冰冻集合 了解
'''
语法：定义冰冻集合，只能使用 frozenset() 函数进行冰冻集合的定义
+ 冰冻集合一旦定义不能修改
+ 冰冻集合只能做集合相关的运算：求交集，差集，。。。
+ frozenset() 本身就是一个强制转换类的函数，可以把其它任何容器类型的数据转为冰冻集合
'''

# 定义
vars = frozenset({'love',666,'a',1,'b',2,'521'})
# vars = frozenset([1,2,3])

# 遍历
# for i in vars:
#     print(i)

# 冰冻集合的推导式
res = frozenset({i<<1 for i in range(6)})

# 冰冻集合可以和普通集合一样，进行集合的运算 交集。。。

# copy()
res = res.copy()
# print(res)

