import pytest

def getcube(num):
    print(f"cube of {num} is {num*num*num}")
    return(num*num*num)
    # return pow(num, 3)
def armstrong(num:int):
    
    res = 0
    while num != 0:
        rem = num % 10
        res = res + getcube(rem)
        num = int(num/10)
    return res
def test_armstrong():
    res = armstrong(153)
    assert res == 153
