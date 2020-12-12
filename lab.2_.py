a = int(input('введите число: '))
b = int(input('введите число: '))
c = int(input('введите число: '))
if a+b>c and b+c>a and c+a>b:
    print('треугольник существует')
    if a==b or a==c:
        print('равнобедренный')
    elif a==b and a==c and b==c:
        print('равносторонний')
    else:
        print('разносторонний')
else:
    print(0)
    
