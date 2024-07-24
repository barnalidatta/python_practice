
num1 = [1,2]
num2 = [3,4]
#print(sorted(num1+num2))
arr =  sorted(num1+num2)
l =  len(arr)
if l % 2 == 0:
    mI1 = int(l/2 -1)
    mI2 = mI1 +1
    print(mI1)
    print(mI2)

    print((arr[mI1]+arr[mI2])/2)
if l % 2 != 0:
    m = l/2 -1
    print(arr[m])
