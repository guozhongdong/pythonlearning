
# _*_ coding=: utf-8 _*_
# ==========================切片==============================
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

#print(L[0:3])

L1 = list(range(99))

#print(L1[:10])

def trim(s):
    if s=='':
       return s
    while s[0] == " ":
        s = s[1:]
    while s[-1] == " ":
        s = s[:-1]
    return s


#print(trim(' ABCDEFG  '))
#============================迭代=================================
# 迭代字典
d = {'a':1,'b':2,'c':3}
"""
for v,c in d.items():
    print('key :' ,v,'value:',c)
"""


# 求一个列表的最大值和最小值
def findMinAndMax(L):
    if L ==[]:
        return(None,None)
    min = L[0]
    max = L[0]
    for n in L:
        if n <= min:
            min = n
        if n >= max:
            max = n
    return (min,max)

#print(findMinAndMax([7,1,3,4,5,6]))

#===================列表生成式======================


L = []
for x in (range(1,11)):
    L.append(x)

#print(L)


K = [x * x for x in range(1,11)]
#print(K)

K1 = [x * x for x in range(1,11) if x%2 == 0]
#print(K1)

K2 = [m + n for m in 'ABC' for n in 'XYZ']
#print(K2)

import os
K3 = [d for d in os.listdir('.')]
#print(K3)

d = {'X':'A','Y':'B','Z':'C'}
K4 = [k + '=' + v  for k,v in d.items()]

#print(K4)

d1 = ['Hello','World',18,'IBM','Apple']
K5 = [s.lower() for s in d1 if isinstance(s,str)]
#print(K5)

#===========================生成器 generator=====================
'''g = (x * x for x in range(10))
for n in g:
    print()


'''


def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b
        a,b = b,a+b
        n= n+1
    return 'done'

#print(fib(6))
'''
杨辉三角定义
把每一行看做一个list，试写一个generator，不断的输出下一行的list
'''

def triangles(number = 10):
    row = [1]
    while True:
        yield(row)
        row,rowR = row + [0],[0] + row
        for k in range(len(row)):
            row[k] += rowR[k]


print(triangles(10))
'''
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n+1
    if n == 10:
        break
'''


#print(results)


#============================== 克迭代对象 Iterable=====================
"""
迭代器：Iterator

凡事可以用 for循环的对象都是 Iterable
凡是可作用于 next()函数的对象都是Iterator
"""
from collections import Iterator
isinstance([],Iterator)





