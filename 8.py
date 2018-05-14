array = [8,3,7,0,-2,1,2,-6,-3]
check = False
for i in range(len(array)):
    if (array[i]>0 and array[i+1]>=0) or (array[0] <= 0 and array[i+1] <=0):
        check = True

print(check)
