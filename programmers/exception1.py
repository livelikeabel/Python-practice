"""
index error : list index out of  range

list = []
print(list[0])
"""

"""
value error : invalid literal for int() with base 10

text = 'abc'
number = int(text)
print(number)
"""

text = '100%'
try:
    number = int(text)
except ValueError:
    print('{}는 숫자가 아니네요.'.format(text))



try:
    list = []
    print(list[0])
except IndexError :
    print('베열에 값을 넣어주세요')

print('===============================')

def safe_pop_print(list, index):
    try:
        print(list.pop(index))
        print(list)
    except IndexError:
        print('{} index의 값을 가져올 수 없습니다.'.format(index))
li = [1,2,3,4,5]
safe_pop_print(li,4)

print('===============================')

try:
    import my_module
except ImportError:
    print("모듈이 없습니다")







