'''
Created on 2017. 10. 26.

@author: MacBook Pro
'''
list1 = [1,1,1,2,2,3,3,3,4,4,5]

print('list1 change to set')
aSet = set( list1 )
print(aSet)

print('set change to list')
newList = list( aSet )

print('result : ', newList)

print('=========================================')

set1 = set([1, 2, 3])
print( set1 )

print('\n# add() function add index of one')
set1.add( 4 ) 
print( set1 )

print('\n# update() function add lot of index')
set1.update( [5, 6, 7] )
print( set1 )

print('==========================================')

print('\n# remove() function remove index')
set1.remove( 4 ) # 여러개는 안되나?
print( set1 )

print('\n# 문자  l은 2개이지만 중복이 안되므로 1개로 보인다.')
set2 = set('hello')
print(set2)

print('========================================')

set3 = set([1, 2, 3, 4])
set4 = set([3, 4, 5, 6])

print('\n교집합')
set5 = set3.intersection(set4)
print(set5)

print('차집합')
set7 = set3.difference( set4 )
print( set7 )









