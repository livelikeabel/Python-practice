def ShowPlus(start, end = 5):
    print( start + end )

ShowPlus(2, 3) #5
ShowPlus(3) #8
ShowPlus(start=2, end=3)#5
ShowPlus(end=4, start=3)#7

print('===============================')

def Func1(*ar):
    print(ar)
    for i in ar :
        print('음식  :', i )

Func1('비빔밥', '김밥', '볶음밥')

print('===============================')
print('dictionary')
def Func2(w, h, **other):
    print('weight : {}, high : {}'.format(w, h))
    print(other)
    
Func2(65, 175, name='abel', age=21)
print('===============================')

mydict = {'name':'abel', 'age':21,'address':'sindangdong'}
Func2(90, 185, **mydict)

print('variable parameter and dictionary')
def Func3(a, b, *v1, **v2):
    print(a, b)
    print(v1)
    print(v2)
    
Func3(1,2,3,4,5)
Func3(1,2,3,4,5, m=6, n=7)
Func3(1,2,3,4,5,6,**mydict)