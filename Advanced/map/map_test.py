# map() filter() reduce() lambda() examples
def addition(n):
    return n + n

# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

result2 = map(lambda n:n+n, numbers)
print(list(result2))

# We can also use map() to create a list of strings from a list of integers
numbers = (1, 2, 3, 4)
result = map(lambda n:str(n), numbers)
print(list(result))

# filter elements from an iterable based on condition
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result = filter(lambda n:n%2==0, numbers)
print(list(result))

# reduce() is a function that applies a function to an iterable and returns a single result
from functools import reduce
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result = reduce(lambda a, b:a+b, numbers)
print(result)

# We can also use reduce() to multiply all the numbers in a list
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result = reduce(lambda a, b:a*b, numbers)
print(result)

# We can also use reduce() to concatenate all the elements in a list
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
result = reduce(lambda a, b:a+b, numbers)
print(result)

# We can also use reduce() to find the maximum and minimum numbers in a list
numbers = (-2, -1, 0, 1, 2)
result = reduce(lambda a, b:a if a>b else b, numbers)
print(result)

