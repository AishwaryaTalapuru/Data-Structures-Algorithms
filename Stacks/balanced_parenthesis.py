from Stack import Stack 
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