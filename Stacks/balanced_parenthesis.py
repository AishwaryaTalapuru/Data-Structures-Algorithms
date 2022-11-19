class Stack:
    def __init__(self):
        self.stack = []
    def push(self, element):
        self.stack.append(element)
    def pop(self):
        elem = self.stack[-1]
        self.stack = self.stack[:-1]
        return elem
    def peek(self):
        return self.stack[-1]
    def show(self):
        return self.stack[::-1]
    def get_length(self):
        return len(self.stack)
def check_parenthesis(a, obj):
    if len(a)%2==0:
        for elem in a:
            if elem == "(":
                obj.push(elem)
            if elem == ")":
                obj.pop()
        if obj.get_length()==0:
            return True
    return False
stack_obj = Stack()
#Running Usecase
inputs = ["(())", "()(())", "(", ")", "((((", "))()"]
for elem in inputs:
    print("Is the list of parenthesis ", elem , " balanced ? ", check_parenthesis(elem, stack_obj))
#Time Complexity - O(n) where n is the size of the input string
#Space Complexity - O(n) where n is the size of the input string