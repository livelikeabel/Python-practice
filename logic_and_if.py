a = 10
if a<10 and 2**a >1000 and a%5 ==2 and round(a) ==a:
    print("복잡한식")

print('=======================')

def return_false():
    print("함수return_false")
    return False

def return_true():
    print("함수return_true")
    return True

print("test 1")
a = return_false()
b = return_true()
if a or b :
    print(True)
else:
    print(False)

print('=======================')

dic = {"Key2":"Value1"}

if "Key1" in dic and dic["Key1"] == "Value1":
    print("Key1도 있고, 그 값은 Value1이네")
else:
    print("아니네")