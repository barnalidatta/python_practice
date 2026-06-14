def numbers():
    for i in range(1, 11):
        yield i

def square(nums):
    for num in nums:
        yield num ** 2

def filter_even(nums):
    for num in nums:
        if num % 2 == 0:
            yield num

# Creating a pipeline
nums = numbers()
squares = square(nums)
even_squares = filter_even(squares)

for num in even_squares:
    print(num)  # Prints even square numbers
