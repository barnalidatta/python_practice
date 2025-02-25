# DEFAULT VALUE FOR MISSING KEY

from collections import defaultdict  
   
# Defining the dict 
d = defaultdict(int) 
   
# L = [1, 2, 3, 4, 2, 4, 1, 2] 
L = [1, 2, 3, 4, 2, 4, 1, 2, 8, 9, 8] 
  
# Iterate through the list 
# for keeping the count 
for i in L: 
       
    # The default value is 0 
    # so there is no need to  
    # enter the key first 
    d[i] += 1
       
print(d) 

#output :  defaultdict(<class 'int'>, {1: 2, 2: 3, 3: 1, 4: 2})
# defaultdict allows you to specify a default factory function that provides default values for missing keys.
#Syntax: defaultdict(default_factory)
#Parameters:  
    # default_factory: A function returning the default value for the dictionary defined. 
    # If this argument is absent then the dictionary raises a KeyError.