'''
Created on 2017. 10. 27.

@author: MacBook Pro
'''

def string_middle(str):
    if len(str) % 2 == 0 :
        index_midle_number1 = round(len(str)/2) -1
        index_midle_number2 = round(len(str)/2)
        return str[index_midle_number1] + str[index_midle_number2]
    elif len(str) == 3:
        index_midle_number = round(len(str)/2) -1
        return str[index_midle_number]
    
    else:
        index_midle_number = round(len(str)/2)
        return str[index_midle_number]


for i in range(10):
    print('input String everything : ')
    print('result : ', string_middle(input()))



