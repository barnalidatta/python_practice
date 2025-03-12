# one
s = "barnali"
print("loop over string\n")
for i in s:
    print(i)
# two
length = len(s)
print("\nloop over range\n")
for i in range(length):
    print(s[i])

# one and two are same
print(s) # same as (s[0::1]),(s[0::]),(s[0:]),(s[::]) (s[:])
# Reverse
print(s[::-1]) # s[Initial:End:IndexJump]
print(s[1:2]) # s[Intial(included):End(not included)]
print(s[-1]) # prints last char
print(s[:-1]) # print all except last char .Same print(s[0:-1])
print(s[1:])  # print except first char
print("######################")
s = "11114567"
length = len(s)
half = int(length/2)
print(half)
#print(s[0:half])
first = s[0:half]
print(f"first half is {first}")
print(first[1:])
print(first[:-1])
if first[1:] == first[:-1]:
    print("all same") 
#f all(iin s[0:half]:
print(s[half:])



