# Missing number in an array
# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.
# Leetcode : 268

#import mypy
def missing_num(arr:list):
    arr.sort()
    arr_len = len(arr)
    for i in range(arr_len+1):
        if i != arr[i]:
            return i

ret = missing_num([9,6,4,2,3,5,7,0,1])
print(type(ret))
print(ret)
# def test_missing_num():
#     res = missing_num([9,6,4,2,3,5,7,0,1])
#     assert res == 8