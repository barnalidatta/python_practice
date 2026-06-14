# Sliding Window method
# used to find substring
# Leetcode - 696 Count Binary Substring
# conditions - Should have 0s and 1s
#            - Should have same number of 0s and 1s
#            - 0s and 1s should be grouped consecutively

def countBinSubstrs(s:str):
    length = len(s)
    start = 0
    end = 1
    temp = []
    count = 0
    # for i in range(length):
    temp.append(s[start])
    temp.append(s[end])
    while end < length :
        
        
        # print(temp)
        # temp_len = len(temp)
        # if temp_len%2:
        #     half = int(temp_len)
        #     first = s[0:half] 
        #     second = s[half:]
        #     if first != second:
        #         if((first[1:] == first[:-1]) and (second[1:] == second[:-1])):
        #             count +=1
        # else:
        
        temp.append(s[end+1])
        # if end == length -1:
        #     del temp[0]
    print(temp)
countBinSubstrs("00110011")

# def test_countBinSubstrs():
#     assert countBinSubstrs("00110011") == 6

