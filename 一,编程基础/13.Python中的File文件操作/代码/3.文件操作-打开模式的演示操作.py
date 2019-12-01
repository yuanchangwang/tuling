# 文件操作的步骤和方式


# 写入文件操作
# # 1。打开文件
# fp = open('./1.txt','a',encoding='utf-8')
# # 2。写入 文件
# fp.write('\n你好')
# # 3。关闭文件
# fp.close()

# 读取操作
# # 1。打开文件
# fp = open('./1.txt','r',encoding='utf-8')
# # 2。读取文件
# res = fp.read()
# # 3。关闭文件
# fp.close()
# print(res)

# 文件操作的 高级写法
'''
with open(文件路径，打开模式) as 变量：
    变量.操作()
'''


# w+ 即可读又可写  注意w模式的特点，是打开文件后直接清空了文件
# r+ 即可读又可写
# a+ 追加写，并且可读
# x+ 异或
with open('./1.txt','r+',encoding='utf-8') as fp:
    # 设置指针的位置
    fp.seek(20)  # 设置当前指针的位置
    fp.write('cc')
    fp.seek(0)  # 设置当前指针的位置 seek(0),最开始的位置
    res = fp.read()
    print(res)

