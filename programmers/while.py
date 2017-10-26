

patterns = ['가위','보','보']
length = len(patterns)
i = 0
while i < length:
    print(patterns[i])
    i = i + 1

print('======================')

list = [1,2,3,5,1243,4123,4,2314,234,2314,21,421,342,134,7,2,5,237,55]
for val in list:
    if val % 3 == 0:
        print(val)
        break

print('======================')


for i in range(10):
    if i%2 != 0:
        print(i)
        print(i)
print('======================')

for i in range(10):
    if i%2 == 0 :
        continue
    print(i)


