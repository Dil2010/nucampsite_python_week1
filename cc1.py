"""Turn this line into a comment
"""
cities = ["Seattle", "Tacoma", "Bellevue"]

a = 1
print(type(a))

b=9.8
print(type(b))

c="string"
print(type(c))

d=a+b
print(d)

x = 0
while x < 10:
    x = x+1
    if x == 1:
        print("small")
    if x > 2:
        x = x+1
        print("medium")
    if x == 5:
        x = 7
        print("big")


my_tuple = (1,2,3,4)
my_set = {1,2,3,4}

print(my_tuple == my_set)

x = 10 
if x < 11 and x > 9: 
    print("if") 
elif x > 10: 
    print("elif") 
else: 
    print("else") 


    # while True: 
    # print("True") 
    # break 
    # print("Break") 
    # break 
    # print("False")

r = 3 
print(r) 
while True: 
    r = r - 1 
    if r == 1: 
        continue 
    elif r == 0: 
        print("END") 
        break 
    else: 
        print(r) 



print(1 > 3 or 2 > 1)

k = 1 + (0 * 10) * 3 / 8 ** 1
print(k)

while True:
    print("1, Number One")
    print("2, Number two")
    print("3,Break Out Of Infinite loop")
    option=input("Pick an Option  ")
    if option=="1":
        print("You choose 1")
    elif option=="2":
        print("You Choose 2")
    elif option=="3":
        print("You chose 3")
        break
