from math import sqrt

flag = 0

def check_prime(num):
    if num > 1:
        for i in range(2, int(sqrt(num))+1):
            #print(i,num)
            if (num % i == 0):
                return False
            
        return True

arr = []   
for i in range(20):
    ret = check_prime(i)
    #print(ret)
    if ret == 1:
      arr.append(i)
print(arr)

