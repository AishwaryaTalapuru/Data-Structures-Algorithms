def merge_sort(one, two):
    if len(one)==0 and len(two)==0:
        return []
    if len(one)==0:
        return two
    if len(two)==0:
        return one
    pt_1, pt_2 = 0, 0
    new_arr = []
    while pt_1 <= len(one)-1 and pt_2 <= len(two)-1:
        if one[pt_1] == two[pt_2]:
            new_arr.append(one[pt_1])
            new_arr.append(two[pt_2])
            pt_1+=1
            pt_2+=1
        elif one[pt_1] < two[pt_2]:
            new_arr.append(one[pt_1])
            pt_1+=1
        else:
            new_arr.append(two[pt_2])
            pt_2+=1
    if pt_1 <= len(one)-1:
        new_arr+=one[pt_1: ]
    if pt_2 <= len(two)-1:
        new_arr+=two[pt_2: ] 
    return new_arr
#Time Complexity - O(n+m) where n is the size of list1 (one) and m is the size of list2 (two)
#Space Complexity - O(n+m) as we have used a new array called "new_arr" that is used to store sorted list
#Overall Time Complexity - 0(N) -roughly
def merge(arr):
    if len(arr)<=1:
        return arr
    if len(arr)%2 == 0:
        mid = len(arr)//2
    else:
        mid = (len(arr)//2)+1
    one = merge(arr[0: mid])
    two = merge(arr[mid: ])
    three = merge_sort(one, two)
    return three
#Time Complexity - O(log n) where n is the size of arr
#Space Complexity - O(1) as we have not used any memory in the merge function

#Total Time Complexity - O(log n)*O(n+m) = O((n+m)logn) => O(nlogn)  where n is the size of list1 (one) and m is the size of list2 (two)
#Total Space Complexity - O(1)+O(n+m) = O(n+m) => O(n) where n is the size of list1 (one) and m is the size of list2 (two)
#Running Usecase
inputs = [[1, 3, 2, 4, 5], [1, 2, 4, 5], [5, 4, 2, 1], [7, 5, 9, 2, 1]]
for item in range(len(inputs)):
    print("The sorted lists are ", merge(inputs[item]))