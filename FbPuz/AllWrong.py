def getWrongAnswers(N: int, C: str) -> str:
    # Write your code here
    res = []
    # d = {True: C[0], False:C[1]}
    for i in range(0,N):
        print(i)
        if C[i] == 'A':
            res.append('B')
        if C[i] == 'B':
            res.append('A')
    r = ''.join(str(x) for x in res) 
    return r

r = getWrongAnswers(5,'BBBBB')
print(r)