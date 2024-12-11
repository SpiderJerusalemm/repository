stroka = input()
dlina = 0
p = 1
stroka = stroka.replace('н', '!')
for i in range(len(stroka) - 1):
  if stroka[i] == stroka[i+1]:
    p += 1
    dlina = max(dlina, p)
  else:
    p = 1
print(dlina, stroka)

stroka = input()
print(stroka[stroka.find('(') + 1 : stroka.find(')')])

stroka = input()
lst = stroka.split(" ")
for i in range(len(lst)):
  if lst[i][0] == 'а' and lst[i][-1] == 'я':
    print(lst[i])
