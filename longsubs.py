def lsubs(s):
    sj = list(s)
    s1 = []
    j = 0
    s2 = []
    for i in range(len(sj)):
        if i + 1 < len(sj):
            j=i
            #print(len(sj))
            if sj[j] != sj[j+1]:
                print("hello", sj[i])
                print(type(s1))
                s1.insert(0,sj[i])
            else:
                s2 = s1
                s1 = 0

    print("s1",s1)
    print("s2",s2)
        

lsubs("pwwkew")
