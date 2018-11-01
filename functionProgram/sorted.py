

#=======================排序算法=============
"""
python内置的sorted函数，sorted也是一个高阶函数，还可以接收一个key函数 来实现自定义的排序

"""

r = sorted([36,5,-12,9,-21],key=abs)

print(r)


'''
可实现字符串排序
'''
r1 = sorted(['bob','about','Zoo','Credit'],key=str.lower,reverse=True)
print(r1)

#==================练习题=========================
'''
用一组 tuple 表示学生名字和成绩
'''
L = [('Bob', 75), ('Adam', 92), ('bart', 66), ('Lisa', 88)]
def by_name(t):  #按名字排序
    return str.lower(t[0])

def by_score(t): #按分数排序
    return t[-1]

L2 = sorted(L,key=by_score)
#r3 = by_name(L)
print(L2)

