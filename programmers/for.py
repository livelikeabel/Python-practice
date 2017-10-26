sum = 0
for i in range(11):
    sum += i
print(sum)

print('========================')

list = ["This", "is", "a", "book"]
for s in list:
    print(s)

print('========================')

i = 0
sum = 0
while True:
    i += 1
    if i == 2:
        continue
    if i > 10:
        break
    sum +=i

print(sum)

print('========================')

numbers = range(2, 21, 2)

for x in numbers:
    print(x)

print('========================')

numbers = range(6)
for n in numbers:
    print(n)

print('========================')

numbers = range(5, 15)
for n in numbers:
    print(n)

print('========================')

for n in range(1, 19, 2):
    print(n)

