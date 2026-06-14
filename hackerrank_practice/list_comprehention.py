list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

l = [l for l in list_of_lists if l[0] + l[1] + l[2] == 6]
print(l)