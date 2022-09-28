def linearSearch(numberList, numberToFind):
    
    for index, number in enumerate(numberList):
        if number == numberToFind:
            return index
    return -1

def binarySearch(numberList, numberToFind):

    midIndex = int((len(numberList) - 1)/2)
    mid = numberList[midIndex]

    if numberToFind == mid:
        return midIndex

    elif numberToFind > mid:
        return len(numberList[0:midIndex+1]) + binarySearch(numberList[midIndex+1:], numberToFind)

    elif numberToFind < mid:
        return binarySearch(numberList[0:midIndex], numberToFind)

    else:
        return -1

def findAllOccurences(numberList, numberToFind):

    index = binarySearch(numberList, numberToFind)
    indexList = [index]

    lIndex = index - 1
    while lIndex >= 0:
        if numberList[lIndex] == numberToFind:
            indexList.append(lIndex)
        else:
            break
        lIndex = lIndex - 1

    rIndex = index + 1
    while rIndex <= len(numberList) - 1:
        if numberList[rIndex] == numberToFind:
            indexList.append(rIndex)
        else:
            break
        rIndex = rIndex + 1

    return indexList

if __name__ == '__main__':

    rollList = [1, 2, 3, 6, 8, 10, 15, 15, 15, 90, 103, 110, 130, 150]
    print(linearSearch(rollList, 15))
    print(binarySearch(rollList, 15))
    print(findAllOccurences(rollList, 15)) #find one occurrence using binary search, then iteratively search right and left of the element

