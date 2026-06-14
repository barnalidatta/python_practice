# Binary search on rotated sorted list
# Find the target item and return the index
# target = value

def bsearch(nums,target):
    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left +right)//2

        if nums[mid] == target: 
            return mid
        
        if nums[left] <=nums[mid]: 
            if nums[left] <= target < nums[mid]:
                right = mid -1
            else:
                left = mid +1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

print(bsearch([3,4,5,6,7,8,9,1,2],1))

# Rotated Sorted list
# No need to rotate