# Count frequency of words  
def count_frequency(str):
    word_count = {}

    # for curr_index, curr_word in enumerate(str.split(),start=0):
    #     word_count[curr_word] = 
        
    for word in str.split():
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1 
    return word_count

print(count_frequency("amazon amazon aws cloud amazon aws"))
