def merge(arrA, arrB):
    arrA.sort()
    arrB.sort()
    leftA = 0
    leftB = 0
    mergedArr = []

    while leftA < len(arrA) and leftB < len(arrB):
        if arrA[leftA] < arrB[leftB]:
            mergedArr.append(arrA[leftA])
            leftA += 1
        else:
            mergedArr.append(arrB[leftB])
            leftB += 1

    mergedArr.extend(arrA[leftA:])
    mergedArr.extend(arrB[leftB:])
    return mergedArr