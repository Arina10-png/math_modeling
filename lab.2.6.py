a = int(input('введите число: '))
b = int(input('введите число: '))
c = int(input('введите число: '))
d = b**2 - 4*a*c
D=b**2 - 4*a*c
if D<0:
    print('корней нет')
elif D == 0:
    x = -b/(2*a)
    print( x)
else:
    x1 = (-b+D**(1/2))/(2*a)
    x2 = (-b-D**(1/2))/(2*a)
    print(x1,x2)
  
    


