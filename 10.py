n = input()
def check(x):
    try:
        int(x)
        return True
    except ValueError:
        return False
if check(n):
    print("Число")
else:
    print("Не число")
