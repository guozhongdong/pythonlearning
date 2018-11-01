#===============返回函数===========================
'''
函数作为返回值
'''

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

f = lazy_sum(1,3,4,6)
print(f())

#======================闭包======================
'''
闭包的概念
返回的函数 在其定义内部引用了局部变量args，
*** 返回函数不要引用任何循环变量，或者后续会发生变化的变量
'''
def count():
    def f(j):
        def g():
            return j*j
        return g()
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1,f2,f3 = count()
#print(f1())
#print(f2())
#print(f3())
#========================练习 利用闭包返回一个计数器函数=====================
def createCounter():
    a = 0
    def counter():
        nonlocal a
        a += 1
        return a
    return counter

counterA = createCounter()
#print(counterA(),counterA(),counterA())

#====================匿名函数=================
'''
关键字 lambda 表示匿名函数
'''
f = lambda x:x*x
print(f(5))

#练习
def is_odd(n):
    return n%2 == 1

L = list(filter(is_odd,range(1,20)))
L1 = list(filter(lambda x:x%2==1,range(1,20)))
print(L)
print(L1)

#==================装饰器 Decorator================
def log(func):
    def wrapper(*args,**kw):
        print('call %s():' % func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2018-11-01')

print(now())

int('123')

#=======================偏函数======================
'''
偏函数的作用：把一个函数的某些参数 给固定住，返回一个新的函数，
'''

import functools
int2 = functools.partial(int,base=2)
print(int2('10000000',base=10))

