print("Введите длины сторон треугольника:")
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
if a+b>c and a+c>b and b+c>a:
print("yes")
else: print("no")
