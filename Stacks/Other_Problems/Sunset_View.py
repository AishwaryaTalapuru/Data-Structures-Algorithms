"""
Sunset view - Question
Given a set of buildings in an array, process the buildings from east to west and return the list of buildings that have a sunset view. If a building is shorter than another building to its west then it looses its sunset view.
"""
"""
Stack data structure
"""

class Stack:
    def __init__(self):
        self.stack = [0]*100
        self.top = -1
    def push(self, elem):
        self.top+=1
        self.stack[self.top] = elem
    def pop(self):
        if self.top ==-1:
            return -1
        res = self.peek()
        self.top-=1
        return res
    def peek(self):
        if self.is_empty()==True:
            return -1
        return self.stack[self.top]
    def is_empty(self):
        if self.top == -1:
            return True
        return False
    def get_length(self):
        return self.top+1
    def get_elements(self):
        return self.stack[0: self.top+1]
#Time Complexity - Each stack operation - (push, pop, peek, is_empty, get_elements) have O(1) time complexity
#Space Complexity - O(100) for the stack
def get_building_list_with_sunset_view(buildings, stack):
    for elem in buildings:
        if stack.is_empty()==True:
            stack.push(elem)
        elif elem >= stack.peek():
            while elem >= stack.peek() and stack.is_empty()==False:
                el = stack.pop()
            stack.push(elem)
        elif elem < stack.peek():
            stack.push(elem)
    return stack.get_elements()
#Running Usecases
buildings = [[5, 6, 10, 9, 8, 5], [1, 2, 3, 7], [12, 2, 3, 5, 7], [7, 4, 3, 1]]
for building in buildings:
    stack = Stack()
    print("The list of buildings receiving the suset view is ", get_building_list_with_sunset_view(building, stack))
#Time Complexity - O(n), where n is the size of the input list of each building's height from east to west direction
#Space Complexity - O(m), where m is the list of the number of building's height that receives sunset