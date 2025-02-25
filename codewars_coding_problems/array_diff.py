# Description:
# Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.
# It should remove all values from list a, which are present in list b keeping their order.
# array_diff([1,2],[1]) == [2]
# If a value is present in b, all of its occurrences must be removed from the other:
# array_diff([1,2,2,2,3],[2]) == [1,3]

def array_diff(arr1:list, arr2:list)-> list[int]:
    #for i in range(len(arr1)):
    for b in arr2:
        for a in arr1:
            print(f"arr1 is {a} and arr2 is {arr2}")
            if a == b:
                arr1.remove(a)
    return arr1

print(array_diff([1,2,2,2,3],[2]))