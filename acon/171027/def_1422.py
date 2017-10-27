def DoFunc1():
    print("call DoFunc1")
    
def DoFunc2( name ):
    print('Hi', name)

def DoFunc3( arg1, arg2 ):
    res = arg1 + arg2
    return print(res)

DoFunc1()

print('================================')
# function name is address of object
print("address of function : ", DoFunc1)

OtherFunc = DoFunc1
OtherFunc()

print('================================')
print('objects in this file', globals())

print('================================')

DoFunc2( 'abel' )

print('================================')
DoFunc3(10, 20)
DoFunc3('python', ' wow!')

print('================================')

def Area_tri(a, b):
    c = a*b/2
    Area_print(c)

def Area_print( c ):
    print('wide : ', int(c))
    
Area_tri(20, 30)