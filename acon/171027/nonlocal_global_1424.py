'''
Created on 2017. 10. 27.

@author: MacBook Pro
'''
a = 10 
b = 20
c = 30
print('before started function // a:{}, b:{}, c:{}'.format(a, b, c))

def Foo():
    a = 40
    b = 50
    print("print Foo //      a:{}, b:{}, c:{}".format(a, b, c))
    def Bar():
        b = 60
        c = 70
        print('print Bar//      a:{}, b:{}, c:{}'.format(a, b, c))
    Bar()
    a = 100
    print('print Foo2//      a:{}, b:{}, c:{}'.format(a, b, c))
Foo()
print('finish run function //   a:{}, b:{}, c{}'.format(a, b, c))