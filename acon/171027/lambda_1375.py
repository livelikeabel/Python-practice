'''
Created on 2017. 10. 27.

@author: MacBook Pro
'''
sum = lambda a, b : a + b
print( sum(3, 4))

list1 = [lambda a, b : a + b, lambda a, b : a* b]
print( list1 )

print( list1[0](5, 4))
print( list1[1](5, 4))