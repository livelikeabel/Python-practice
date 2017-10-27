'''
Created on 2017. 10. 27.

@author: MacBook Pro
'''
def func1 (a, list):#**a ??
    n = 0
    for i in list :
        if i > a :
            n = n + 1
    return n

def func2(mylist):
    list2 = []
    for i in range(len(mylist)-1, -1, -1):
        list2.append(mylist[i])
    return list2
"""
def func2 (list2):
    list2.reverse()
    return list2
"""