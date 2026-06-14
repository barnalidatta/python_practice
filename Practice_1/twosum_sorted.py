# two pointer works on only sorted array
# for unsorted use hashmap(dictionary)
def twosum(num,target):
    num.sort()
    new_list= []
    left = 0
    right = len(num)-1

    while left < right:
        sum = num[left] + num[right]
        if sum < target:
            left = left +1
        if sum > target:
            right = right -1
        if sum == target:
            new_list.extend([left,right])
            return new_list
        
assert twosum([2,7,8,9],9) == [0,1]
#print(twosum([2,7,5,6],9))
