#reverse each word in a sentence
# this code is adding an extra space in the begining !!!
def word_rev(s):
    word = ""
    result = ""
    for char in s:      
        word = char + word
        
        if char == " ":
            print(word)
            result = result + word
            #print(result)
            word = ""
    result = result + word
    print(result)

word_rev("my name is hfksdh")

            
            
            
                
