from collections import OrderedDict

print("Before:\n")
od = OrderedDict() 
#od = {} # No differnce
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
for key, value in od.items():
    print(key, value)

print("\nAfter replacing c:\n")
od['c'] = 5
for key, value in od.items():
    print(key, value)