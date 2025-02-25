import pytest
# Largest element in an array
def find_largest(arr:list):
    return(max(arr))

def find_smallest(arr:list):
    return(min(arr))

def find_second_largest(arr:list):
    arr.sort()
    return arr[-2]

def test_find_largest():
    print("find largest")
    ret = find_largest([8,6,3,5,4,9,8,3,4,7,0])
    #print(ret)
    assert ret == 9

def test_find_smallest():
    print("find smallest")
    ret = find_smallest([8,6,3,5,4,9,8,3,4,7,0])
    assert ret == 0
    
def test_find_second_largest():
    print("find second larget")
    ret = find_second_largest([8,6,3,5,4,9,8,3,4,7,0])
    assert ret == 8
