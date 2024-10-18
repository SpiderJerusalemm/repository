def cos(x, y) :
    return x  / ((x ** 2 + y ** 2) ** 0.5)

x1, x2 = map(float,input().split())
y1, y2 = map(float,input().split())
z1, z2 = map(float,input().split())
tochka = [x1, x2]
cosx = cos(x1, x2)
cosy = cos(y1, y2)
cosz = cos(z1, z2)
if cosy > cosx :
    cosx = cosy
    tochka = [y1, y2]
if cosz > cosx :
    cosz = cosz
    tochka = [z1, z2]
print(*tochka)