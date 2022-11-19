from Stack import Stack
def get_binary_from_decimal(obj, number):
    while number >= 2:
        rem = number%2
        if rem!=0:
            number-=1
        number //=2
        obj.push(rem)
    #Time Complexity - O(log n) where n is the input number
    obj.push(number)
    binary_list = []
    while obj.is_empty()==False:
        binary_list.append(obj.pop())
    #Time Complexity - O(m) where m is O(log n)
    stack_output = [str(elem) for elem in binary_list]
    return "".join(stack_output)
#Time Complexity -  O(log n) + O(log n) => 2*O(log n) => log n
#Space Complexity - O(n)
#where n is the size of the input number 
inputs = [1, 2, 3, 67, 100]
for elem in inputs:
    stack_obj = Stack()
    binary_value = get_binary_from_decimal(stack_obj, elem)
    if bin(elem).replace("0b", "") == binary_value:
        print("The binary value of ", elem , " is ", binary_value)
#Total Time Complexity -  O(log n) + O(log n) => 2*O(log n) => log n 
#Total Space Complexity - O(n)
#where n is the input number

