# OrderedDict` maintains the sequence in which keys are added, ensuring that the order is preserved during iteration. 
# In contrast, a standard dictionary does not guarantee any specific order when iterated, providing values in an arbitrary sequence. 
# `OrderedDict` distinguishes itself by retaining the original insertion order of items.


# >>> from collections import OrderedDict
# >>> l = [1,1,4,8,4,6,8,4,6]
# >>> od = OrderedDict.fromkeys(l) 
# >>> od
# OrderedDict([(1, None), (4, None), (8, None), (6, None)])
# >>> list(od)
# [1, 4, 8, 6]
# >>>

from collections import OrderedDict 

od = OrderedDict() 
#od = {}  # To check the difference. No difference.
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
  
print('Before Deleting')
for key, value in od.items(): 
    print(key, value) 
    
# deleting element
od.pop('a')

# Re-inserting the same
od['a'] = 1

print('\nAfter re-inserting')
for key, value in od.items(): 
    print(key, value)