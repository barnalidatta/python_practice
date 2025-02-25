def word_rev(s):
    rev = ""
    result = ""
    s = (s.split(' '))
    for word in s:
        for char in word:
            rev = char + rev
        result = result + ' ' + rev
        rev=""
    print(result[1:])
            
        
        
word_rev("m y name is hfksdh")
