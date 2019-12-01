# 字典定义和基本操作

# 一，字典定义

# 1。 使用{}定义
vardict = {'a':1,'b':2,'c':2}

# 2。 使用 dict(key=value,key=value) 函数进行定义
vardict = dict(name='zhangsan',sex='男',age=22)

# 3。 数据类型的转换  dict(二级容器类型) 列表或元组，并且是二级容易才可以转换
vardict = dict([['a',1],['b',2],['c',3]])  # {'a': 1, 'b': 2, 'c': 3}

# 4。zip压缩函数，dict转类型
var1 = [1,2,3,4]
var2 = ['a','b','c','d']

# 转换的原理和上面的第三种 是一个原理
vardict = dict(zip(var1,var2))  # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}



# 二，字典数据的操作 获取，添加，更新，删除

var1 = {'a': 1, 'b': 2, 'c': 3}
var2 = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# res = var1 +  var2 # XXXX  TypeError
# res = var1 * 3 # xxxx TypeError

# 获取元素
res = var1['a']

# 修改元素
res = var1['a'] = 111

# 删除元素
del var1['a']

# 添加元素
var1['aa'] = 'AA'

# 如果字典中的key重复了，会被覆盖
# var1['aa'] = 'aa'

# 三 成员检测  ,只能检测key，不能检测value
res = 'AA' in var1
res = 'AA' not in var1

# 获取当前字典的长度 只能检测当前又多少个键值对
res = len(var1)

# 获取当前字典中的所有 key 键
res = var1.keys()
# 获取字典中所有的 value 值
res = var1.values()
# 获取当前字典中所有 键值对
res = var1.items()

# 四， 对字典进行遍历
# （1）在遍历当前的字典时，只能获取当前的key
for i in var1:
    print(i) # 只能获取 key
    print(var1[i]) # 通过字典的key获取对应value

#（2）遍历字典时，使用 items() 函数，可以在遍历中获取key和value
for k,v in var1.items():
    print(k)  # 遍历时的 key
    print(v)  # 遍历时的 value

print('===='*20)
# (3) 遍历字典的所有key
for k in var1.keys():
    print(k)

print('===='*20)
# (4) 遍历字典的所有 value
for v in var1.values():
    print(v)