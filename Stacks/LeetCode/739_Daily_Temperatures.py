"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""
class Solution(object):
    def dailyTemperatures(self, temperatures):
        temp = temperatures
        temp_stack = []
        index_stack = []
        res = [0]*len(temp)
        for item in range(len(temp)):
            if len(temp_stack)==0:
                temp_stack.append(temp[item])
                index_stack.append(item)
            elif len(temp_stack) >0 :
                if temp[item] > temp_stack[-1]:
                    while len(temp_stack)>0 and temp[item] > temp_stack[-1]:
                        a = temp_stack.pop()
                        b = index_stack.pop()
                        res[b] = item-b
                temp_stack.append(temp[item])
                index_stack.append(item)
        return res
#Time Complexity - O(n) where n is the size of the input list
#Space Complexity - O(n), because we are creating a result list of size n
#Running usecases
inputs = [[73,74,75,71,69,72,76,73], [30,40,50,60], [30,60,90]]
for elem in inputs:
    sol_obj = Solution()
    print("The list of warmer temperatures are : ", sol_obj.dailyTemperatures(elem))