# Binary search on sorted list
# Find the target item and return the index
# target = value

def bsearch(nums,target):
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left +right)//2

        if nums[mid] == target:
            return mid
        
        elif nums[mid] > target:
            right = mid -1

        elif nums[mid] < target:
            left = mid +1
    return -1

print(bsearch([3,4,5,6,7,8,9,1,2],1))


print(bsearch([1,2,3,4,5],4))
# Rotated Sorted list
# No need to rotate