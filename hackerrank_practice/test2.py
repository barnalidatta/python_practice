if __name__ == '__main__':
    n = int(input())
    str = 0
    if n<=150 and n>=1:
        for i in range(1,n+1):
            if i<10:
                str = i + str * 10
            if i>=10 and i<100:
                str = i + str*100
            if i>=100 and i<=1000:
                str = i + str*1000
    print(str)