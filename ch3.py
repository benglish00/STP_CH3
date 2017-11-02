# basic for loop, i starts at 0
for i in range (10):
    print(i+1)

import math
# length of a diagonal
l = 4
w = 10
d = math.sqrt(l**2 + w**2)
print(d)

#print long line
print("""Colooooooooooooooooooooooooooooooooooooooraddo
ooooo""")

#conditional
home = "Colorado"
if home == "Colorado":
    print("Hello, Colorado!")
else:
    print("Hello, Loser! :D")

x = 2
if x ==2:
    print("The number is 2!")
if x%2 == 0:
    print("The number is even!")
if x%2 != 0:
    print("The number is odd. TT")

x = 10
y = 11
if x ==10:
    if y == 11:
        print(x+y)

#Challenge 1. printe 3 strings
print("Colorado")
print("Winter")
print("Ski")

#Challenge 2 sort a number
x = 8
if x == 10:
    print("x is 10!")
if x>10:
    print("x is greater than 10!")
if x<10:
    print("x is less than 10!")

#Challenge 4 and 5. Find the remainder and quotient
print("The remainder is",10%3)
print("The quotient is",10//3)

#6 Sort an a variable age
age = 44
if age == 44:
    print(age, "is just right!")
elif age > 44:
    print("Damn!",age, " is old!")
else:
    print(age,"! Spring Chicken!")