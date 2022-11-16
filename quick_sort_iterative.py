def swap(low, high, arr):
    temp = arr[low]
    arr[low] = arr[high]
    arr[high] = temp
    return arr
def quick_sort(arr):
    queue = []
    while len(arr)-1 > len(queue):
        pivot = 0
        while pivot in queue:
            pivot+=1
            if pivot == len(arr):
                pivot = 0
                break
        low = pivot
        high = len(arr)
        while low < high:
            if low < len(arr)-1:
                low+=1
            """
            Descending order
            while low < len(arr)-1 and arr[low]>arr[pivot]
            """
            while low < len(arr)-1 and arr[low]<arr[pivot]:
                low+=1
                if low == len(arr)-1:
                    break
            if high > 0:
                high-=1
            """
            Descending order
            while high > 0 and arr[high] <= arr[pivot]
            """
            while high > 0 and arr[high] >= arr[pivot]:
                high-=1
                if high == 0:
                    break
            if low < high:
                if high not in queue:
                    arr = swap(low, high, arr)
        if high not in queue:
            arr = swap(pivot, high, arr)
        queue.append(high)
    return arr
#Running Usecase
inputs = [[1, 3, 2, 4, 5], [1, 2, 4, 5], [5, 4, 2, 1], [7, 5, 9, 2, 1]]
for item in range(len(inputs)):
    print("The sorted lists are ", quick_sort(inputs[item]))