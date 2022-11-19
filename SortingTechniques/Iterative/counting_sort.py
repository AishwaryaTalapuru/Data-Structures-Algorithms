#Algorithm for counting sort
def counting_sort(arr):
    #count_arr
    count_arr = [0]*10
    for index in range(len(arr)):
        value = arr[index]
        count_arr[value]+=1
    #pre_sum array
    temp = 0
    for index in range(len(count_arr)):
        count_arr[index]+=temp
        temp = count_arr[index]
    sorted_arr = [0]*len(arr)
    for index in range(len(arr)):
        value = arr[index]
        new_index = count_arr[value]-1
        sorted_arr[new_index] = value
        """
        For Descending order
        new_index = count_arr[value]
        sorted_arr[len(arr)-new_index]=value 
        """
        count_arr[value]-=1
    return sorted_arr
#Running Usecase
inputs = [[1, 3, 2, 4, 5], [1, 2, 4, 5], [5, 4, 2, 1], [7, 5, 9, 2, 1]]
for elem in inputs:
    print("The ascending order of ", elem, " is ", counting_sort(elem))
#Time Complexity of counting sort - O(n+k)
#where n is the number of input elements
#k is the range of elements
#Space Complexity - O(n)