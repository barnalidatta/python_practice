# hashmap way - a dictionary that stores item of a list as key and index of that item as value
# if the difference of target and items in the list is found in that 
# Key Lookup is Instant (\(O(1)\)) - hash table/hash function 
def twosum(num,target):
    match_pile = {}

    for curr_index, curr_item in enumerate(num):
        complement = target - curr_item
        if complement in match_pile:
            return [match_pile[complement], curr_index]
        
        match_pile[curr_item] = curr_index
        
assert twosum([2,8,6,5,7],9) == [0,4]