#  使用 生成器函数 改写 斐波那契数列

# 斐波那契数列
# def fibo(num):
#     a,b,i = 0,1,0
#     while i < num:
#         print(b,end=",")
#         a,b = b,a+b
#         i+=1
# fibo(7)

# 使用 生成器函数 改写 斐波那契数列
def fibo():
    a,b,i = 0,1,0
    while True:
        yield b
        a,b = b,a+b
        i+=1

num = int(input('请输入一个正整数:'))
res = fibo()
for i in range(num+1):
    print(next(res),end=",")



