"""
Stack data structure
"""

class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1
    def push(self, elem):
        self.stack.append(elem)
        self.top +=1
    def pop(self):
        if self.top ==-1:
            return -1
        res = self.peek()
        self.top-=1
        return res
    def peek(self):
        return self.stack[self.top]
    def is_empty(self):
        if self.top == -1:
            return True
        return False
    def get_length(self):
        return self.top+1