import itertools
# d= {"2":["a","b","c"], "3":["d","e","f"]}
lst1 = ["a","b","c"]
lst2 = ["d","e","f"]
lst3 = ["g","h","i"]
d= {"2":lst1, "3":lst2, "4":lst3}

    #, "4":["g","h","i"], "5":["j","k","l"], "6":["m","n","o"], "7":["p","q","r","s"], "8":["t","u","v"], "9":["w","x","y","z"]}

inp= input("Enter a value")

print (inp)

s = list(inp)
nl = []

def comb(s):
    if len(s)< 1:
        return d[s[0]]
    else:
        nl[] = 


#nl.append(i+j+k)
# 234
# ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei', 'bfg', 'b
# 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi']
print(nl)










# print(d["2"])
# #while len(s)>0:
# for i in s:
#     if i in d.keys():

# for k,val in d:
#     print(i)
#     print(d[s[i]])

# print(d)
# print(d.keys())
# print(d.values())
# print(d.items())
# newd = []
# inp = int(input("Enter a value"))
# while (inp > 0): 
   
#     div = inp%10
#     print(inp)
#     newd.append(d[div])
#     inp = int(inp/10) 

# print(newd)

# # print(list(newd.keys()))
# #  if len(newd)>1:
# k = 1
# def combi(newd):
#    for i in newd:
#        for j in i:
            
#            print(j,l)
           
           
# combi(newd)

# # res = [["".join(j) for j in itertools.combinations(newd[i],2)] for i in newd.keys() ]
# # while len(newd.keys()) > 1:
# #     for i in newd.keys():
# #         for j in  

# # if len(newd.keys())> 1:
# #     res = [[ j for j in newd[i] ] for i in newd.keys() ]
# # print(res)