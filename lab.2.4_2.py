n = int(input('введите число: '))
f1 = 0
f2 = 1
print(f1, f2, end=" ")
for i in range(1, n+1):
    print (f1+f2, end=' ')
    d=f1
    f1 = f2
    f2 = d+f1
print()


