def fact_recur(num:int):
    if num == 0:
        return 1
    else:
        return  num*fact_recur(num-1)
    
def fact(num:int):
    res =1
    for i in range(2,num+1):
        res *= i
    return res
    
print(f" Resursive {fact_recur(6)}")
print(f" Iterative {fact(6)}")
