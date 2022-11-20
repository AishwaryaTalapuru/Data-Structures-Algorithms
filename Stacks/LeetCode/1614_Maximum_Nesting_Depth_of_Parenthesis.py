class Solution(object):
    def maxDepth(self, s):
        max_open_brace, open_brace = 0, 0
        for elem in s:
            if elem == "(":
                open_brace +=1
            elif elem == ")":
                open_brace -=1
            if max_open_brace < open_brace:
                max_open_brace = open_brace
        return max_open_brace
    #Time Complexity - O(n)
    #Space Complexity - O(1)
    #Running UseCases
obj = Solution()
inputs = ["((()))", "()(())", "", "()"]
for elem in inputs:
    print("The maximum nesting depth of ", elem , " is ", obj.maxDepth(elem))