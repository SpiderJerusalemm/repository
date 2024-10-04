import math
import numpy as np

# result = 0
# n = int(input("input n in range 100:\n"))
# if n >= 100:
#     print("n in range 100!")
# else:
#     for i in range (n + 1):
#         result += i**3
#     print (f'finish sum = {result}')


for i in range (1, 10):
    for n in range (1, 10):
        if i * n < 10:
            print ((i * n), end = '  ')
        else:
            print ((i * n), end = ' ')
    print()

# for i in range (9, 0):
#     for n in range (1, 10):
#         if i * n < 10:
#             print ((i * n), end = '  ')
#         else:
#             print ((i * n), end = ' ')
#     print()
