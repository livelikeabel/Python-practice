'''
Created on 2017. 10. 27.

@author: MacBook Pro
'''
b_list2 = [1, 3, 2, 5, 7, 6]

re = all(a < 10 for a in b_list2)
print('모든 숫자가 10 미만이냐?', re)


print('=======================')

x = [10, 20, 30]
y = ['a', 'b']
for i in zip(x, y): #zip ?
    print(i)

print('=======================')

print(sum([3, 5, 7]))
print(sum({3, 5, 7}))
print(sum((3, 5, 7)))
# print(sum(3, 5, 7)) ERRORE
print(bin(8)) # ???? 0b1000
print(int(1.7)) #내림...?
print(int(2.7))
print(int(0.7))
print('=======================')
print(float(3))
print(str(5) + '오')
print('=======================')
b = eval('10+5') # 문자열도 합해주는건가....?
print(b)

print('반올림 테스트  : ',round(1.5), round(2.5)) #0.5하면 0이되고, 2.5 하면 2가 된다.1.5 하면 2가 된다.
 
b_list = [True, 1, True]
print('모두 참인가요? :', all(b_list))
print('참이 1개 이상인가요? : ', any(b_list))