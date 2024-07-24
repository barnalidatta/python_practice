def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(5))
    
    # 2, 2*fact(1), 2*1
    # 3, 3*fact(2), 3*(2*fact(1))
    # 4, 4*(fact(3)),4*(3*fact(2)),4*(3*(2*fact(1)))nums