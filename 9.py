n = float(input())
x = input().split(' ')

if n < len(x):
    print("Элементов больше чем N")
else:
    print(max(x))
