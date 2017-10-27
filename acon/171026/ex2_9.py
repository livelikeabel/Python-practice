'''
Created on 2017. 10. 26.

@author: MacBook Pro
'''
t=('a','b','c','a')
#t = 'a','b','c','a'

print('t is ',t)
print('t * 2 =', t*2)
print('t size = ', len(t))
print('count : ', t.count('a'))
print('search result : ', t.index('a'))

print('==========================')

p = (1,2,3)
#p[1] = 10
q = list(p)
print('q = ',q)
q[1] = 10
p = tuple(q)
print('q = ',p)

print('=========================')

print(p)
print('튜플로 슬라이싱 가능')
print('p[1:]의 결과는', p[1:]) #슬라이싱 처리

print('==========================')





