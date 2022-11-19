def binary_search(arr, low, high, value):
    if low <= high:
        mid = (low+high)//2
        if mid < low or mid > high:
            return False
        if arr[mid] == value:
            return True
        if value > arr[mid]:
            return binary_search(arr, mid+1, high, value)
        else:
            return binary_search(arr, low, mid-1, value)
    return False
inputs = [[1, 2, 3, 4, 5], [1, 2, 4, 5], [1, 2, 4, 5], [1, 2, 9, 5, 7], []]
to_find = [3, 3, 6, 0, 13]
for index in range(len(inputs)):
    high = len(inputs[index])-1
    print("Is the element ", to_find[index], " in the list ", inputs[index], ": ", binary_search(inputs[index], 0, high, to_find[index]))
#Time Complexity - O(log n) where n is the size of the input arr
#Space Compleixty - O(1)