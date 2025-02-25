def reverse1(my_str:str)->str:
    # edge case
    return(my_str[::-1])  # New Copy of Data

def reverse2(my_str:str):
    
    my_str1 = list(reversed(my_str)) # Iterating over Data
    return (''.join(my_str1))     

def reverse3(my_str:str):
    res = ""
    for char in my_str:
        res = char + res
    return res


print(f"Reversing by slicing {reverse1('barnali')}")
print(f"Reversing by built-in func reversed {reverse2('barnali')}")
print(f"Reversing by iteration {reverse2('barnali')}")