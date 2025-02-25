from collections import defaultdict

    
# Defining the dict and passing 
# lambda as default_factory argument
d = defaultdict(int) # int/str/list/
d["a"] = 1
d["b"] = 2

print(d["a"])
print(d["b"])
print(d["c"])