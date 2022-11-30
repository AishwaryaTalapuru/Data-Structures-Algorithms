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