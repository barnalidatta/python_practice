# list3 = [1,2,[3,4,"hello"]]
# list3[2][2] = "goodbye"
# print(list3)

d ={'k1':[{'nest_key':['this is deep',['hello']]}]}
for k,v in d.items():
    for i in v:
        for j,k in i.items():
            data = k
print(k[1])