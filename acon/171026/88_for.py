'''
Created on 2017. 10. 26.

@author: MacBook Pro
''' 
list = [90, 25, 67, 45, 80]

number = 0

for grade in list:
    number +=1
    
    if grade >= 60:
        print('{}번째 응시자 {}점 합격'.format( number, grade))
    
    else :
        print('{}번째 응시자 {}점 불합격'.format( number, grade))
        

for num in range( len(list) ):
    if list[num] <=60 :
        continue
    else :
        print('{}번째 응시자 {}점 합격'.format(num + 1,list[num]))