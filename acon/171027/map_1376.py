'''
Created on 2017. 10. 27.

@author: MacBook Pro
'''
def two_times1(numList):
    result = []
    for num in numList:
        result.append( num * 2 )
        
    return result

list1 = [1, 2, 3]
result = two_times1( list1 )
print( result )

# map
def two_times2( number ):
    return 2 * number

list1 = [3, 4, 5]
list2 = list(map( two_times2, list1))
print( list2 )

#lambda and map
list1 = [4, 5, 6]
list3 = list(map(lambda a : 2 * a, list1))
print( list3 )

