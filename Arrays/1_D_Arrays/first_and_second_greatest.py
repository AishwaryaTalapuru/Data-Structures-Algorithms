def first_and_second_greatest(arr):
    #finding the first greatest
    first_max_elem = -2e9
    for elem in arr:
        first_max_elem = max(first_max_elem, elem)
    if first_max_elem == -2e9:
        #This means that there is no max elem
        #array may be empty
        return [-1 -1]
    second_max_elem = -2e9
    for elem in arr:
        if elem != first_max_elem:
            second_max_elem = max(second_max_elem, elem)
    if second_max_elem == -2e9:
        second_max_elem = -1
    return [first_max_elem, second_max_elem]
    