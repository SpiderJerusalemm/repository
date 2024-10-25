# def m_stroka(row):
#   sum = 0
#   for element in row:
#     sum += element
#   return sum


# arr = [[3, 1, 4], [1, 5 , 7], [7, 0, 0], [9,3,6]]
# s = list()

# for row in arr:
#   sum_of_row = m_stroka(row)
#   s.append(sum_of_row)

# print(s,'\n',r'max is', max(s), '\n',r'min is', min(s))


def chet_nechet(min_el):
  for element in row:
    if element % 2 == 0:
      return(0)
    else:
      return(1)

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
s = list()

for row in arr:
  min_el = min(row)
  sum_of_row = chet_nechet(min_el)
  s.append(sum_of_row)

print(arr, s)