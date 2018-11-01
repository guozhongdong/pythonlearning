#=======map/reduce================
'''
map 接收连个参数，一个函数，一个Iterable

'''

def f(x):
    return x *x
r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))


#转换字符串
print(list(map(str,range(10))))


#====================reduce 操作=============
'''
reduce：把一个函数作用在一个序列上[x1,x2,x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的
下一个元素做累计计算，
'''
#序列求和

from functools import reduce
def add(x,y):
    return x * 10 + y

r1 = reduce(add,[1,2,3,4,5,6,7,8,9])
#print(r1)
#============ str 转 int的函数
def char2num(s):
    digits = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9};
    return digits[s]

#r2 = reduce(char2num(),'13579')
r2 = reduce(add,map(char2num,'13579'))
r3 = map(char2num,'13579')
#print(list(r3))
#print(r2)
#============================整理++++++++++++++++++

DIGITS = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        return DIGITS[s]
    return reduce(add,map(char2num,s))


#print(str2int('2468'))
#==============lambad===================
def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num,s))
#=====================练习 把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
L1 = ['adam', 'LISA', 'barT']
def normalize(s):
    dd = s[0:1].upper() + s[1:].lower()
    return dd

#print(list(map(normalize,L1)))

#===================练习 请编写一个prod()函数，可以接受一个list并利用reduce()求积：================

def prod(x,y):
    return x*y
#print(reduce(prod,[3,5,7,9]))

#===================练习 请编写一个prod()函数，可以接受一个list并利用reduce()求积：================

DIGITS1 = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'.':'.'}

s1 = '123.456'


def char2num(s):
    return DIGITS[s]
def str2float(s):
    s = s.split('.')
    s1 ,s2 = s[0],s[1]
    s1_num = reduce(lambda x,y:x*10+y,map(char2num,s1))
    s2_num = reduce(lambda x,y:x/10+y,map(char2num,s2[::-1]))
    #s2_num = round(s2_num,0.1,3)
    return s1_num+s2_num

print(str2float(s1))