# Return the sum of the numbers in the array except ignore sections of number starting with 6 a
# and extending to next 9 ( every 6 will be followed by atleast one 9). Return 0 for no numbers.

#summer_69([1,3,5])--> 9
#summer_69([1,2,3,6,7,9]) --> 6

def summer_69(mylist):
    
    for i in mylist:
        if i == 6:
            ind6 = mylist.index(6)
        if i == 9:
            ind9 = mylist.index(9)

    del mylist[ind6:ind9+1]
    
    print(mylist)

summer_69([1,2,3,6,7,9,11])