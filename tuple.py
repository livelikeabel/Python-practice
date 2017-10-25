tuple=(1,2,3)
print(tuple)
tuple2=1,2,3
print(tuple2)

a, b = 1, 2
print(a)
print(b)

c = (3, 4)
print(c)
print('======================')

d, e = c
print(d)
print(e)

print('======================')
f = d, e
print(f)
print('======================')
def tuple_func():
    return 1,2

q,w = tuple_func()
print(q)
print(w)

print('======================')

list = [1,2,3,4,5]
for a in enumerate(list):
    print('{}번째 값 {}'.format(*a))

print('======================')
ages = {'Tod': 35,'Jane': 23,'Paul': 62}
for key, val in ages.items():
    print('{}의 나이는:{}'.format(key, val))

print('======================')









