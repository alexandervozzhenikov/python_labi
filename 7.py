x = float(input())
y = float(input())

day = x
count = 1

while day <= y:
    count+=1
    day = day + (day*0.1)
print("count: = ",count)
