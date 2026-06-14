import heapq

# By default, heapq.nlargest compares elements using their first index (item[0]). If you didn't include the lambda function, Python would sort your dictionary alphabetically by the word names ("apple", "banana", etc.).

def topk(num_list, k):
    num_freq_hash = {}
    heap = []

    # Count_frequency.py
    for num in num_list:
        if num in num_freq_hash:
            num_freq_hash[num] +=1
        else:
            num_freq_hash[num] = 1
    
    # Flipping the dictionary key,value -> value, key
    list_of_tuple = [(freq,number) for number,freq in num_freq_hash.items()]
    for freq, number in list_of_tuple: 
        if len(heap) <k:                           # heap maintains 2 item, only the highest values
            heapq.heappush(heap,(freq,number))   # heap is adding tuple
        else:
            heapq.heappushpop(heap,(freq,number))
    
    # Using nlargest : Works
    # heap = heapq.nlargest(k, num_freq_hash.items(), key=lambda item: item[1])
    heap = [item[1] for item in heap]

    return heap

nums = [1,1,1,2,2,3]
k = 2
heap = topk(nums, k)

print(heap)