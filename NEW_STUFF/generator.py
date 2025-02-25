# for x in [n**2 for n in range(5)]:
#     print( x, ':',)

def gensquares(N):
    for i in range(N):
        yield i**2

gen = gensquares(5)

# for x in gen:
#     print(x, end=' ')

# write a test program to check if the generator works as expected
# def test_gen():
#     gen = gensquares(5)
#     for i in range(5):
#         assert next(gen) == i**2
#     assert next(gen) == None

# test_gen()
# print('test passed')

# 1. Yield
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

# Using the generator
for num in count_up_to(5):
    print(num)  # Outputs: 1, 2, 3, 4, 5

# 2. Generator expression
squares = (x*x for x in range(5))
print(next(squares))  # 0
print(next(squares))  # 1
print(next(squares))  # 4

# 3. Infinite Generator
def infinite_counter():
    num = 0
    while True:
        yield num
        num += 1

counter = infinite_counter()
print(next(counter))  # 0
print(next(counter))  # 1
print(next(counter))  # 2

# 4. Generator with Multiple yield Statements:
def even_odd():
    yield "even"
    yield "odd"
    yield "even"
    yield "odd"

for item in even_odd():
    print(item)

# 5. Generator with send():
def counter():
    i = 0
    while True:
        val = yield i
        if val is not None:
            i = val
        else:
            i += 1

c = counter()
print(next(c))      # 0
print(next(c))      # 1
print(c.send(10))   # 10
print(next(c))      # 11
