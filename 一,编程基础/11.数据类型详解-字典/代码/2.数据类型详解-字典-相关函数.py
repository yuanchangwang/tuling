#  字典相关函数

# len(字典) #获取字典的键值对个数
# dict.keys() # 获取当前字典的所有key 键，组成的列表
# dict.values() # 获取当前字典的所有 value 值，组成的列表
# dict.items() # 返回由字典项 ((键, 值) 对) 组成的一个新视图
# iter(d) 返回以字典的键为元素的迭代器。

vardict = {'a':1,'b':2,'c':3}

# dict.pop(key) # 通过 key 从当前字典中弹出键值对  删除
# res = vardict.pop('a')

# dict.popitem()   LIFO: Last in, First out.后进先出
# res = vardict.popitem()  # 把最后加入到字典中的键值对删除并返回一个元组

# 使用key获取字典中不存在元素，会报错
# print(vardict['aa'])
# 可以使用get获取一个元素，存在则返回，不存在默认返回None
# res = vardict.get('aa')
# res = vardict.get('aa','abc')

# dict.update(),更新字典,如果key存在，则更新，对应的key不存在则添加
# vardict.update(a=11,b=22)
# vardict.update({'c':33,'d':44})

# dict.setdefault(key[,default])
# 如果字典存在键 key ，返回它的值。
# 如果不存在，插入值为 default 的键 key ，并返回 default 。
# default 默认为 None。

res = vardict.setdefault('aa','123')

print(res)
print(vardict)


