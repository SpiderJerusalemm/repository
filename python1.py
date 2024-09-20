import math
print("hey there! we have a few function, and we want to show them you")
R = int(input("please, input radius \n"))
P = round(int(2) * math.pi * R, 2)
S = round(math.pi * R**2, 2)
print(f"your P, S is: {P}, {S}")

x, y = 10, 55
print (x,y)
x, y = y, x
print (x,y)

g = int(9.81)
L = int(input("please, input lenght \n"))
T = int(2) * math.pi * math.sqrt(L/g)
print(f"your period is : {T}")
