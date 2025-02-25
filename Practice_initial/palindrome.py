def palindrome(str):
    for i in range(0,len(str)//2):
        if str[i] != str[-i-1]:
            return False
    return True

ret = palindrome(input("enter a string : "))
if ret:
    print("palindrome")
else:
    print("Not palindrome")