def binary_search(arr, value):
    low = 0
    high = len(arr)-1
    while low >= 0 and high <= len(arr)-1 and low <= high:
        mid = (low+high)//2
        if arr[mid] == value:
            return True
        elif value > arr[mid]:
            low = mid+1
        else:
            high = mid-1
    return False
inputs = [[1, 2, 3, 4, 5], [1, 2, 4, 5], [1, 2, 4, 5], [-1, 1, 2, 9, 5, 7], []]
to_find = [3, 3, 6, -1, 13]
for index in range(len(inputs)):
    print("Is the element ", to_find[index], " in the list ", inputs[index], ": ", binary_search(inputs[index], to_find[index]))
#Time Complexity - O(log n) where n is the size of the input arr
#Space Complexity - 0(1) 