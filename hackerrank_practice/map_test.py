if __name__ == '__main__':
    #n = int(input())
    #arr = map(int, input().split())
    #print(list(arr))
    num = "5 2 4 5 3 1"
    print(num.split())
    arr=map(int, num.split())
    l=sorted(set(arr))
    print(l[-2])