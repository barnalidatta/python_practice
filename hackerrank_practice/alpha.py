if __name__ == '__main__':    
    s = "#$%@^&*kjnk svskjnbui h 4oi3hheuh /dfh uidshvhdsuihv suihc 0hrem89m4c02mw4xo;,wh fwhncoishmxlxfkjsahnxu83v 08 n8OHOIHIOMOICWHOFCMHEOFMCOEJMC0J09C 03J J3L;JMFC3JM3JC3'JIOO9MMJ099U N090N9 OOHOLNHNLLKNLKNKNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK3333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333333000000000000000000000000000000000000000000000000000000000000000000000000000"

    # an = a = d = l = u = 0
    # s1=''
    # s2 =''
    # s3=''
    
    # for i in s:
    #     if i.isalnum():
    #         s1 +=i
    # print(s1.isalnum())

    # for char in s:
    #     if char.isalpha():
    #         s2 +=char
    # print(s2)
    # print(s2.isalpha())
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))

    # for i in s:
    #     if (i.isalnum()):
    #         an +=1
    #     if (i.isalpha()):
    #         a+=1
    #     if (i.isdigit()) == True:
    #         d +=1
    #     if (i.islower()) == True:
    #         l +=1
    #     if (i.isupper()) == True:
    #         u +=1
    # if an>0:
    #     print(True)
    # else:
    #     print(False)
    # if a>0:
    #     print(True)
    # else:
    #     print(False)
    # if d>0:
    #     print(True)
    # else:
    #     print(False)
    # if l>0:
    #     print(True)
    # else:
    #     print(False)
    # if u>0:
    #     print(True)
    # else:
    #     print(False)
