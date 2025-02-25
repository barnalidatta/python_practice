import itertools
p = ["a","b", "c"]
q = ["d", "e", "f"]

d = []

for i in p:
    for j in q:
       d.append(i+j) 

print(d)



# print( ["".join(j) for j in itertools.combinations(p, 2)])

