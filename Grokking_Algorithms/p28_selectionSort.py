def findSmallest(arr):
    min = arr[0]
    min_index = 0
    for i in range(1,len(arr)):
        if arr[i] < min:
            min = arr[i]
            min_index = i
    return min_index


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        min = findSmallest(arr)
        newArr.append(arr.pop(min))
    return newArr


l01 = [5,4,3,7,9,1,2,6]
print(selectionSort(l01))