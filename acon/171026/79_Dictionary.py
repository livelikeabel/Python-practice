'''
Created on 2017. 10. 26.

@author: MacBook Pro
'''
mydict = {'chulsu kim':35, 'yunghui park':50, 'gildong hong':40}
print('dictionary : ', mydict)

print('keys() : show key of dictionary')
for key in mydict.keys():
    print(key)
    
print('values() : show list of dictionary')
for value in mydict.values():
    print(value)

print('=================')

print('search value using by keys()')
for key in mydict.keys():
    print('{} age is {}'.format(key, mydict[key]))
    
print('items(): show pair by key and value')
for key, value in mydict.items():
    print('{} age is {}'.format(key, value))
    


print('=================')

findkey = 'hyungrea Sim'
if findkey in mydict :
    print(findkey + ' is exit')
else:
    print(findkey + ' is not exit')

print('=================')

print('output data use pop()')
result = mydict.pop('gildong hong')
print('dictionary poped : ', mydict)
print('result of pop :', result)
print('=================')

print('clear() :clear dictionary')
mydict.clear()
print('dictionrary : ', mydict)