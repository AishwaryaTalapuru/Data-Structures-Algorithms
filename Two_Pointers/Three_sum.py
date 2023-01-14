#Given a sorted array, identify three numbers that add up to the target
def three_sum(arr, target):
    res = []
    for k in range(0, len(arr)-2, 1):
        j = len(arr)-1
        i = k+1
        while i < j:
            if arr[i]+arr[j]+arr[k]==target:
                res.append([arr[k], arr[i], arr[j]])
                break
            elif arr[i]+arr[j]+arr[k] > target:
                j-=1
            else:
                i+=1
    return res
#Time Complexity (Average case) - O(len(arr)-3)*O(len(arr)/2)
#Time Complexity (Best case) - O(len(arr)-3)*O(1)
#Time Complexity (Worst case) - O(len(arr)-3)*O(len(arr)-2)
#Space Complexity - O(1)

#Test cases
targets = [27, 100, 31, 11]
input_arr  = [1, 2, 4, 5, 6, 11, 15]
for elem in targets:
    print("The three numbers in the array that add up to the target ", elem , " is ", three_sum(input_arr, elem))
