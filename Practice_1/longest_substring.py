# Longest subsstring without repeating character
# Sliding Window -> both pointer(left and right) startes from index 0.
# 
# Create a hashmap or hashset(set()) cause it checks for no duplicates.
# Traverse the string, 
# If not in hash, add it and increase the right pointer (expand the window)
# if found, move the left pointer from start and remove all the item from start until duplicate is removed (shrink the window)
# Time: O(n) Space: O(n)

def long_sub(s):
    window = set()
    left = 0
    right = 0
    max_len=0
    for right in range(len(s)):
        while s[right] in window:
            window.remove(s[left])
            left +=1
        window.add(s[right])
        max_len = max(max_len, right-left+1)
    return max_len

s = "abcabcbb"
print(long_sub(s))
