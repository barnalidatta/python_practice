strg = "barnali"

temp = [strg[i:j] for i in range(len(strg)) for j in range(i+1,len(strg)+1)]

print(temp)

d = dict()

for p in temp:
    d[p] = strg.count(p)

print("Extracted frequency dictionary : " + str(d))