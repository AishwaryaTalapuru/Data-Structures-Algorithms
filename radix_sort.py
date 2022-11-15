def counting_sort(arr, divident):
    #Use a key-value pair
    my_dict = {}
    for i in range(10):
        my_dict[i] = []       
    for value in arr:
        index = (value//divident)%10
        """
        For descending order
        my_dict[10-index-1].append(value)
        """
        my_dict[index].append(value)
    new_arr = []
    for key, value in my_dict.items():
        new_arr += value        
    return new_arr
def radix_sort(arr):
    max_elem = -2e9
    for elem in arr:
        if max_elem < elem:
            max_elem = elem        
    max_count = 0
    while max_elem > 0:
        max_elem//=10
        max_count +=1
    divident = 1
    count = 0
    while count < max_count:
        new_arr = counting_sort(arr, divident)
        divident *=10
        arr = new_arr
        count+=1
    return new_arr
#Running Usecase
inputs = [[11, 17, 9, 4, 65, 42], [111, 89, 660], [7700, 45], [93, 45, 1, 9, 0]]
for elem in inputs:
    print("The ascending order of ", elem, " is ", radix_sort(elem))