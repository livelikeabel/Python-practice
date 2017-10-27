'''
Created on 2017. 10. 26.

@author: MacBook Pro
'''
print('---print1---')
for i in range(1, 6):
    for j in range(1 ,6):
        print( j, end = '')
    print()
    
print('---print2---')
for i in range(1,6):
    for j in range(1,6):
        print(i,end = '')
    print()
    
print('---print3---')
for i in range(1, 6):
    for j in range(1, 6):
        print( j + i -1, end =' ')
    print()

print('---print4---')
for i in range(9, 4, -1):
    for j in range(0, 5):
        print(i - j, end =" ")
    print()