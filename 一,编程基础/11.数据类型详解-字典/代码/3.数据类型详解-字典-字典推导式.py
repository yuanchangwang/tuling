#  字典推导式


# 把字典中的键值对位置进行交换 {'a':1,'b':2,'c':3}
vardict = {'a':1,'b':2,'c':3}

# 普通方法实现 字典中的键值交换  {1: 'a', 2: 'b', 3: 'c'}
newdict = {}
for k,v in vardict.items():
    newdict[v] = k
# print(newdict)

# 使用字典推导式完成  {1: 'a', 2: 'b', 3: 'c'}
newdict = {v:k for k,v in vardict.items()}
# print(newdict)

# 注意：以下推导式，返回的结果是一个集合，集合推导式
# newdict = {v for k,v in vardict.items()}
# print(newdict,type(newdict))


# 把以下字典中的是偶数的值，保留下来，并且交换键值对的位置
vardict = {'a':1,'b':2,'c':3,'d':4}

# 普通方式完成  {2: 'b', 4: 'd'}
# newdict = {}
# for k,v in vardict.items():
#     if v % 2 == 0:
#         newdict[v] = k
# print(newdict)

# 字典推导式完成  {2: 'b', 4: 'd'}
newdict = {v:k for k,v in vardict.items() if v % 2 == 0}
# print(newdict)

