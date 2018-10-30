#!/usr/bin/env python
# _*_ coding: utf-8 _*_
#可变参数
"""
1、位置参数
    power(X) X就是位置参数
2、默认参数
   def power(x,n=2): # n就是默认参数
    默认参数 必须指向不变对象
3、可变参数
    *numbers 表示把numbers这个list当成 可变参数传进去，
    def calc(*numbers)   #*numbers 是一个 元组tuple或list
        sum = 0
        for n in numbers:
            sum = sum + n * n
        return sum
4、关键字参数
    关键字参数允许你传入0g个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict

5、命名关键字参数
    与关键字参数不同的是，命名关键字参数需要一个特殊分隔符 * ，*后面的参数被视为命名关键字参数
    如果函数定义中已经有了一个可变参数，* 后面的参数被视为 命名关键字参数
    命名关键字参数必须传入 参数名，

6、参数组合
    可以用 必选参数、默认参数、可变参数、关键字参数和命名关键字参数
    参数的定义顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
"""




def person(name,age,**kw):
    print('name:',name,'age:',age,'other',kw)


#print(person('Bob','13',city='beijing',email='111@163.com'))


def person1(name,age,*,city='beijing',job):
    print(name,age,city,job)

#print(person1('Bob','13',job='1111'))

def person2(name,age,**kw):
    print('name:', name, 'age:', age, 'other:', kw)

extra = {'city':'beijing','job':'Engineer'}
#print(person2('ming','12',**extra))


def person3(name,age,*,city,job):
    print(name, age,city,job)

#print(person3('ming','12',city='beijing',job='Teacther'))

def product(x,y):
    return x * y

def product(*args):
    sum = 1
    for n in args:
        sum = sum * n
    return sum

print(product(2))