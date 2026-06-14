# Input: s = "leetcode"
# Output: 0
# Explanation:The character 'l' at index 0 is the first character that does not occur at any other index.
# first non-repeating

def first_uniq(word):
    letter_count = {}

    for letter in word:
        if letter in letter_count:
            letter_count[letter] +=1
        else:
            letter_count[letter] =1

    for index, letter in enumerate(word):
        if letter_count[letter] == 1:
            return index
        
    return -1

print(first_uniq("leetcode"))
print(first_uniq("loveleetcode"))
print(first_uniq("aabb"))
