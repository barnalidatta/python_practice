thickness = int(input())
c='*'

#top cone
for i in range(thickness): 
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

#top
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

#middle
for i in range((thickness +1 ) // 2):
    print((c  * thickness * 5).center(thickness  * 6))    

#bottom
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

#bottom cone
for i in range(thickness):
    print(((c  * (thickness  -  i - 1)).rjust(thickness) + c + (c  * (thickness  -  i - 1)).ljust(thickness)).rjust(thickness * 6))