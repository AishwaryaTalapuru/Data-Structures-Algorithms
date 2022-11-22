"""
You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

"""
class Solution(object):
    def removeDuplicates(self, s, k):
        if len(s)==0:
            return s
        stack = []
        num_stack =[]
        for elem in s:
            if len(stack) > 0 and elem == stack[-1]:
                stack.append(elem)
                num_stack[-1]+=1
                if num_stack[-1]==k:
                    a = num_stack.pop()
                    while len(stack)>0 and elem == stack[-1]:
                        b = stack.pop()
            else:
                stack.append(elem)
                num_stack.append(1)
        return "".join(stack)
#Time Complexity - O(n)*O(m) where n is the size of the input where m lies in the range [1, n/k] where k is the number of times a character repeats and it has to be removed
#Space Complexity -O(n) as we create a stack 
#Running Usecase
inputs = ["abcd", "deeedbbcccbdaa"]
k = [2, 3]
for elem in range(len(inputs)):
    sol_obj = Solution()
    print("The original string is ", inputs[elem] , " and modified string is ", sol_obj.removeDuplicates(inputs[elem], k[elem]))

