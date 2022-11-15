def counting_sort(arr, divident):
    #Use a key-value pair
    my_dict = {}
    for i in range(10):
        my_dict[i] = [] 
    #Time Complexity - O(n)
    #where "n" is the size of the input      
    for value in arr:
        index = (value//divident)%10
        """
        For descending order
        my_dict[10-index-1].append(value)
        """
        my_dict[index].append(value)
    #Time Complexity - O(n)
    #where "n" is the size of the input 
    new_arr = []
    for key, value in my_dict.items():
        new_arr += value        
    return new_arr
    #Time Complexity - O(n)
    #where "n" is the size of the input 
    #Total Time Complexity of "counting_sort" is  - O(n)
def radix_sort(arr):
    max_elem = -2e9
    for elem in arr:
        if max_elem < elem:
            max_elem = elem   
    #Time Complexity - O(n)
    #where "n" is the size of the input      
    max_count = 0
    while max_elem > 0:
        max_elem//=10
        max_count +=1
    #Time Complexity - O(n)
    #where "n" is the size of the input 
    divident = 1
    count = 0
    while count < max_count:
        new_arr = counting_sort(arr, divident)
        divident *=10
        arr = new_arr
        count+=1
    return new_arr
    #Time Complexity - O(k*n)
    #where "n" is the size of the input 
    #where "k" is the length of the largest item
    #Time Complexity - O(k*n)
    #where "n" is the size of the input 
    #Total Time Complexity of "counting_sort" is  - O(n)
    #The time complexity of radix sort is given by the formula,T(n) = O(d*(n+b)), where d is the number of digits in the given list, n is the number of elements in the list, and b is the base or bucket size used, which is normally base 10 for decimal representation.
#Running Usecase
inputs = [[11, 17, 9, 4, 65, 42], [111, 89, 660], [7700, 45], [93, 45, 1, 9, 0]]
for elem in inputs:
    print("The ascending order of ", elem, " is ", radix_sort(elem))
