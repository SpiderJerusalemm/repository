import math


a = float(input("введите первое делимое: \n"))
b = float(input("пожалуйста, введите делитель: \n"))
if (b != 0):
    print(a/c, b/c)
else:
    print("incorrect!")


a = int(input("на какую сумму вы закупились? \n"))
if (a > 20):
  b = a * (1 - 1 * (35/100))
  print(f'ваша скидка: {round(a * 35/100, 2)} \nсо скидкой к оплате: {round(b, 2)}')
else:
  print(f'увы, скидка от 20 у.е. \nК оплате: {a}')


month = int(input("пожалуйста, введите номер месяца: \n"))
if month < 1 or month > 12:
  print("invalid number!")
else:
  if month > 2 and month <= 5:
    print("spring")
    if month == 3:
      print(f'name is march')
    elif month == 4:
      print(f'name is april')
    elif month == 5:
      print(f'name is may')
  elif month > 5 and month <= 8:
    print("summer")
    if month == 6:
      print(f'name is june')
    elif month == 7:
      print(f'name is july')
    elif month == 8:
      print(f'name is august')
  elif month > 8 and month <= 11:
    print("autumn")
    if month == 9:
      print(f'name is september')
    elif month == 10:
      print(f'name is october')
    elif month == 11:
      print(f'name is november')
  elif month == 1 or month == 2 or month == 12:
    print("winter")
    if month == 1:
      print(f'name is january')
    elif month == 2:
      print(f'name is february')
    elif month == 12:
      print(f'name is december')
