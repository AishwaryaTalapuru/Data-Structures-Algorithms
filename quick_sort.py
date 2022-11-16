def swap(arr, low, high):
    temp = arr[low]
    arr[low] = arr[high]
    arr[high] = temp
    return arr
def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot = arr[0]
    low = 0
    high = len(arr)
    while low < high:
        if low<len(arr)-1:
            low+=1
        while low <= len(arr)-1 and arr[low]<pivot:
            low+=1
            if low==len(arr)-1:
                break
        if high > 0:
            high-=1
        while high >= 0 and arr[high]>=pivot:
            high-=1
            if high==0:
                break
        if low < high:
            arr = swap(arr, low, high)
    arr = swap(arr, 0, high)
    return quick_sort(arr[0: high])+[arr[high]]+quick_sort(arr[high+1:])
#Running Usecase
inputs = [[1, 3, 2, 4, 5], [1, 2, 4, 5], [5, 4, 2, 1], [7, 5, 9, 2, 1]]
for elem in inputs:
    print("The ascending order of ", elem, " is ", quick_sort(elem))