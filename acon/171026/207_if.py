'''
Created on 2017. 10. 26.

@author: MacBook Pro
'''
n = input()

if n < 0:
    print('양수아님')
elif n % 5 == 0:
    print(n, '은 5로 나누어진다.')
else:
    print('5로 나누어지지 않는다.')