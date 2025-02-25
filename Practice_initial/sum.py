# def sum(n):
#     if n<= 0:
#         return 0
#     return n + sum(n -1)

# print(sum(4))

def pairsum(n):
    sum = 0
    for i in range(n):
        sum += pais(i, i+1)
    return sum

def pais(a, b):
    return a+b

print(pairsum(4))