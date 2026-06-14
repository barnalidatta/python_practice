# d = {"a":[1,2,3], "b":[4,5,6]}
# print(d["a"][1])
# print(d["b"][2])

# for i in d:
#     if i == "a":
#         print(d[i][0] + d[i][1] + d[i][2])

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(type(integer_list))
    t = tuple(integer_list)
    print(t)
    print(hash(t))