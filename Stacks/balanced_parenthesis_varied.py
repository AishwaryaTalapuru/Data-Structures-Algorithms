from Stack import Stack
def check_parenthesis(a, obj):
    brackets = {"{":"}", 
                 "(" :")", 
                 "[": "]"}
    if len(a)%2==0:
        for elem in a:
            #Time Complexity of "in" operation is O(1) for dictionary keys
            if elem in brackets.keys():
                obj.push(elem)
            #Time Complexity of "in" operation is O(n) for dictionary values 
            #where "n" is the size of the dictionary
            #Time Complexity worst case is O(n/2)
            elif elem in brackets.values():
                opening_bracket = obj.pop()
                if opening_bracket == -1 or brackets[opening_bracket] != elem:
                    return False
            else:
                return False
        if obj.get_length()==0:
            return True
    return False
#Running Usecase
inputs = ["{[()]}", "()(())", "(", ")", "((((", "))()", ""]
#Time Complexity of Iteration is O(n) where n is the size of the string
for index in range(len(inputs)):
    stack_obj = Stack()
    print("Is the list of parenthesis ", inputs[index] , " balanced ? ", check_parenthesis(inputs[index], stack_obj))
#Total Time Complexity for one string is O(n)*O(m) 
# where n is the size of the input string
# m is the number of closing braces in the input string
#Space Complexity -O(1)