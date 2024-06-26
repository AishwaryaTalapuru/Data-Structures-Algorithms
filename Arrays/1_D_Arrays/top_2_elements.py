def top_2_elements(arr):
    #finding the first greatest
    first_max_elem = -2e9
    for elem in arr:
        first_max_elem = max(first_max_elem, elem)
    if first_max_elem == -2e9:
        #This means that there is no max elem
        #array may be empty
        return [-1, -1]
    second_max_elem = -2e9
    for elem in arr:
        if elem != first_max_elem:
            second_max_elem = max(second_max_elem, elem)
    if second_max_elem == -2e9:
        count = 0
        for elem in arr:
            if elem == first_max_elem:
                count +=1
        if count > 1:
            second_max_elem = first_max_elem
        else:
            second_max_elem = -1
    return [first_max_elem, second_max_elem]

def evaluator(arr):
    arr.sort(reverse=True)
    if len(arr)==0:
        return [-1, -1]
    if len(arr)==1:
        return [arr[0], -1]
    else:
        return [arr[0], arr[1]]

#Time Complexity - O(n)
#Space Complexity - O(1)

test_cases = [[1, 2, 3], [3, 2, 1], [3, 3, 3], [3], []]
for test_case in test_cases:
    print("Test case: ", test_case)
    print("Expected Result:  ", evaluator(test_case))
    print("Actual Result:  ",top_2_elements(test_case) )
    if top_2_elements(test_case) == evaluator(test_case):
        print("Passed")
    else:
        print("Failed")