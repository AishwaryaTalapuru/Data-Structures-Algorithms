from Stack import Stack
def reverse_string(stack_obj, input_string):
    for elem in input_string:
        stack_obj.push(elem)
    reversed_string_list = []
    while stack_obj.is_empty() == False:
        reversed_string_list.append(stack_obj.pop())
    return "".join(reversed_string_list)
#Time Complexity - O(n) where n is the size of the input
#Space Complexity - O(n) where n is the size of the input
inputs = ["a", "ab", "aaa", "-1", "aishwarya", "pop"]
for elem in inputs:
    stack_obj = Stack()
    reversed_string = reverse_string(stack_obj, elem)
    if reversed_string == elem[::-1]:
        print("The reverse of a string ", elem , " is ", reversed_string)
#Total Time Complexity - 1*O(n) where n is the size of the input string 
#Total Space Complexity - 1*O(n) where n is the size of the input string 
