

'''
class Hello(object):
    def hello(self,name = 'world'):
        print('Hello,%s.' % name)
from hello import Hello
h = Hello()
h.hello()

print(type(Hello))
'''

def fn(self,name='world'):
    print('Hello ,%s ' % name)

Hello = type('Hello',(object,),dict(hello=fn))
h = Hello()
h.hello()
