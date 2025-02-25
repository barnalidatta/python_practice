def fibonacci(num:int):
    num1 = 0
    num2 = 1
    if num == 0:
        return num1
    if num == 1:
        return 1
    else:
        for i in range(2,num):
        
            print(f"here{i} num1 = {num1}, num2 = {num2}")
            tmp = num1 + num2
            num1 = num2
            num2 = tmp
            print(f"{tmp}")
        #return tmp

#print(fibonacci(2))
fibonacci(10)