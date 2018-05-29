print('compare string')
str1 = 'abc'
str2 = 'xyz'
str3 = 'xyz'
print(str1==str2)
print(str1==str3)
print(str2==str3)

print('compare lower()')
str4 = 'Abc'
print(str4.lower()==str1)
print(str4==str1)

num1 = 55
num2 = 3
print('compare number')
print(num1==num2)
print(num1!=num2)
print(num1>num2)
print(num1<num2)
print(num1>=num2)
print(num1<=num2)

print('test and or')
if num1>num2 and str2==str3:
    print('test True')
if num1<num2 and str2==str3:
    print('test True')
if num1<num2 or str==str3:
    print('test True')

animals = ['cat','dog','fish','lion']
if 'fish' in animals:
    print('The list contain fish')
if 'tiger' in animals:
    print('The list contain tiger')

if 'fish' not in animals:
    print('The list doesnt contain fish')
if 'tiger' not in animals:
    print('The list doesnt contain tiger')