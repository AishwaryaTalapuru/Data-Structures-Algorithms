def linear_search(arr, elem, index):
    if index >= len(arr):
        return -1
    if arr[index]==elem:
        return index
    return linear_search(arr, elem, index+1)
#Time Complexity - O(n)
#Space Complexity - O(1)
input_arr = [1, 2, 56, 78]
elems = [1, 34, 72, 56, 78]
for elem in elems:
    index = linear_search(input_arr, elem, 0)
    if index == -1:
        print("The element ", elem , " is not present in the list ", input_arr)
    else:
        print("The element ", elem , " is present at index ", index, " in the list ", input_arr)