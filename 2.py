a = float(input("Введите первое число:"))
b = float(input("Введите второе число:"))
c = float(input("Введите третье число:"))
if a>c and a>b:
max=a
elif c>a and c>b:
max=c
else:
max=b
print('Наибольшее из данных чисел =',max)
