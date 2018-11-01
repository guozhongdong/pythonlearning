"""
filter 函数用于过滤序列
与map不同，filter是依次把函数作用于序列的每个元素，然后根据返回值是 True 还是False 决定保留还是丢弃

"""

def odd(x):
    return x%2==1

print(list(filter(odd,[1,2,3,4,5,6,7,8])))

#=============用filter 求素数

def _odd_iter():
    n = 1
    while True:
        n = n+2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it =_odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n),it)


for n in primes():
    if n < 1000:
        print(n)
    else:
        break

#=====================练习  用filter打印出回数=====================
from functools import reduce

print(reduce(lambda x,y:y+x,'123'))

def is_palindrome(n):
    return str(n) == reduce(lambda x,y:y+x,str(n))

print(list(filter(is_palindrome,range(1,200))))