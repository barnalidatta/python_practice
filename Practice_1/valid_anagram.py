def validate(word1,word2):
    if len(word1) != len(word2):
        return False
    
    word_count = {}
    for ch in word1:
        if ch in word_count:
            word_count[ch] +=1
        else:
            word_count[ch] =1
    
    for ch in word2:
        if ch not in word_count:
            return False
        
        word_count[ch] -=1

        if word_count[ch] < 0:
            return False
    return True
print(validate("anagram","nagaram"))