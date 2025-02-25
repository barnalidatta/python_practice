def sumofdig(n):
    if n<=9:
        return n
    
    rem = n%10
    return sumofdig(n//10) + rem

s = sumofdig(12)
print(s)