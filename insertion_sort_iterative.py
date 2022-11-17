#Insertion sort
def insertion_sort(arr):
    for p1 in range(1, len(arr)):
        i = p1-1
        while i>=0:
            if arr[i] > arr[p1]:
                temp = arr[i]
                arr[i] = arr[p1]
                arr[p1] = temp
                p1 = i
            i-=1
    return arr
#Time Complexity - O(n*n)
#Space Complexity - O(1)
#Running Usecase
inputs = [[1, 3, 2, 4, 5], [1, 2, 4, 5], [5, 4, 2, 1], [7, 5, 9, 2, 1]]
for item in range(len(inputs)):
    print("The sorted lists are ", insertion_sort(inputs[item]))
