import math
x = int()
while x > 0 :
    print("hey there! we have a few function, and we want to show them you")
    x = int(input("0 - i`m ready, 1 - not yet \n"))
    if x == 0 :
        print("see ya later")
        break
    else :
        R = input("please, input radius")
        S = 2 * math.pi * R 
        print(f"your S is: {S}")
        