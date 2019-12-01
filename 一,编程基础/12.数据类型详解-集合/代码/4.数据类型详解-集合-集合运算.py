# 集合运算

'''
集合的主要运算
    交集  &    set.intersection()   set.intersection_update()
    并集  |    union()  update()
    差集  -    difference(),difference_update()
    对称差集 ^  symmetric_difference()  symmetric_difference_update()
'''

vars1 = {'郭富城','刘德华','张学友','黎明','都敏俊',1}
vars2 = {'尼古拉斯赵四','刘能','小沈阳','宋小宝','都敏俊',1}

#  & 求两个集合相交的部分
res = vars1 & vars2


# | 求两个集合的并集，就是把集合中所有元素全部集中起来，（去除重复）
res = vars1 | vars2

# - 差集运算
res = vars1 - vars2 # vars1有，而，vars2 没有的
res = vars2 - vars1 # vars2有，而，vars1 没有的

# ^ 对称差集
res = vars1 ^ vars2



# 交集运算函数 intersection  intersection_update
# set.intersection()  # 返回交集的结果 新的集合
# res = vars1.intersection(vars2)

# set.intersection_update()  # 没有返回值
# 计算两个集合的相交部分，把计算结果重新赋值给第一个集合
# res = vars1.intersection_update(vars2)


# 并集运算函数  |    union()  update()
# res = vars1.union(vars2)  # 返回并集结果，新的集合
# 求并集运算，并且把结果赋值给第一个集合
# res = vars1.update(vars2) # 没有返回值
# print(vars1)


# 差集运算  函数 difference(),difference_update()
# res = vars1.difference(vars2) # 返回差集结果  新的集合
# 把差集的结果，重新赋值给第一个集合
# res = vars1.difference_update(vars2) # 没有返回值

# 求对称差集
# res = vars1.symmetric_difference(vars2) # 返回对称差集的结果  新的集合

# 把对称差集的运算结果，重新赋值给第一个集合
res = vars1.symmetric_difference_update(vars2)# 没有返回值


# 检测 超集  子集
vars1 = {1,2,3,4,5,6,7,8,9}
vars2 = {1,2,3}

# issuperset() 检测是否为超集
res = vars1.issuperset(vars2)  # True  vars1是vars2的超集
res = vars2.issuperset(vars1)  # False

# issubset() 检测是否为子集
res = vars1.issubset(vars2) #  False
res = vars2.issubset(vars1) #  True vars2是vars1的子集

# 检测两个集合是否相交
vars1 = {1,2,3}
vars2 = {5,6,3}
# isdisjoint 检测是否不相交， 不相交返回True，相交则返回False
res = vars1.isdisjoint(vars2)
print(res)






