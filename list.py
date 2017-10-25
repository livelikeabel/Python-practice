a = []
a = ["AB", 10, False]

x = a[1]
print(x)
print(a[1])

a[1] = True
print(x)
print(a[1]) #a[1] 객체가 새로 생성되는건가..?? 메모리 낭비 되겠는걸..?
y = a[-1]
print(y)
y = a[-3]
print(y)
print('========================')

a = [1, 3, 5, 7, 10]
x = a[1:3]
print(x)
x = a[0:3]
print(x)

print('========================')

n = [1,2,3,4,15,32,53,235,235,235,235,2,532,523,523,53,25,235,3245,3245,324,53,425,234,5,3425,32,4523,45,324, 5342, 52, 45]

x = n[:14]
print(x)
print('========================')

a = ["AB", 10, False]
a.append(21.5)
print(a)
a[1] = 11
print(a)
del a[2]
print(a)
print('========================')

a = [1, 2]
b = [3, 4, 5]
c = a + b
print(c)

d = a * 3
print(d)
print('========================')

mylist = "This is a book That is a pencil".split()
i = mylist.index('book')
n = mylist.index('is')
print(i, n, mylist)

print('========================')

list = [ n ** 2 for n in range(16) if n % 4 == 0 ]

print(list)



list2 = [n ** 3 for n in range(16,58) if n % 6 ==2 ]
print(list2)




