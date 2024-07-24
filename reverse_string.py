
def quick(s):
    s1 = ''.join(list(reversed(s)))
    print(s1)

def manual(s):
    result = ""
    for char in s:
        #print(char)
        print(result)
        result = char + result
    print(result)

def slicey(s):
    l = len(s)
    result = s[-1::-1]
    print(result)
    
quick("dat")
manual("edit")
slicey("jacks")
