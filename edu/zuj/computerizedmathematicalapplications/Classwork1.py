#This file has nothing different from the previous files, that's why I called it 'classwork'

print("Ali")

print(17)

print("Ali", "Maha", sep="&")

print("Ali,\tMaha,\nSaif")

x = 14

y = 17

print(x + y)

print(type(14.17))

print(x - y)

print(x * y)

print(x / y)

print(x % y)

print(x // y)

print(x ** y)

width = 5

length = 7

area = width * length

perimeter = 2 * (length + width)

print("Area\tPerimeter")

print(area, perimeter, sep = "\t")

print(x == 17)

print(x < 17)

print(x != 17)

print(3 + 4 * 2 - ((1 + 7) / 2) ** 3)

x = 18

if(x >= 18):
    print("adult")

else:
    print("minors")

if(x <= 19):
    print("adult")

else:
    print("minors")

temp = 10

if(temp >= 36):
    print("very hot")

elif(temp >= 28):
    print("hot")

elif(temp < 28 and temp >= 11):
    print("nice")

elif(temp < 11):
    print("cold")

age = 17

if(age >= 18):
    print("Adult")

else:
    print("Minor")