class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        my_dict = {}
        stack = []
        for elem in nums2:
            if len(stack)==0:
                stack.append(elem)
            elif stack[-1] <= elem:
                while len(stack)>0 and stack[-1] <= elem:
                    my_dict[stack[-1]] = elem
                    stack = stack[:-1]
                stack.append(elem)
            else:
                stack.append(elem)
        for index in range(len(nums1)):
            if nums1[index] in my_dict:
                nums1[index] = my_dict[nums1[index]]
            else:
                nums1[index] = -1
        return nums1
obj =  Solution()
inputs1 = [[1, 2, 3, 4], [1, 7, 3, 4, 2], [4, 3, 2, 1, 5]]
inputs2 = [[2, 3], [7, 3], [3, 1]]
for index in range(len(inputs1)):
    next_greater_elem_list = obj.nextGreaterElement(inputs2[index], inputs1[index])
    print("The next greater element for every element in the list ", inputs1[index], " is ", next_greater_elem_list)
#Time Complexity - O(n) where n is the size of the input arr
#-> Best Case - O(n)
#-> Average Case - O(n log n)
#-> Worst Case - O(n**2)
#Space Complexity - O(n) where n is the size of the input
#-> As we implement a stack and store elements in it, we incur O(n) space