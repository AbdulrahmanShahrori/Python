x = 0

if (x > 0):
    print("positive")

else:
    print("negative")

mark = 77

if (mark >= 90):
    print("Excellent")

elif (mark >= 80 and mark <= 89):
    print("Very Good")

elif (mark >= 70 and mark <= 79):
    print("Good")

elif (mark >= 60 and mark <= 69):
    print("Average")

elif (mark >= 50 and mark <= 59):
    print("Weak")

else:
    print("Fail")

#Nested if statement

score = 55

attendance = 70

if (score >= 50):
        if (attendance >= 75):
            print("pass")

        else:
            print("deprived")

z = -17

if (z > 0):

    if (z % 2 == 0):
        print("Positive and even")

    else:
        print("Positive and odd")

elif (z == 0):
    print("Zero and even")

else:

    if (z % 2 == 0):
        print("Negative and even")

    else:
        print("Negative and odd")

#loops

for i in range(5):
    print(i)

print("")

for i in range(2, 7):
    print(i)

print("")

for i in range(2, 11, 2):
    print(i)

print("")

total = 0

for i in range(1, 6):
    total += i

average = total / 5

print(average)