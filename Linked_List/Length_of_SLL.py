from SLL import SLL
def get_length(head):
    count = 0
    temp = head
    while temp!=None:
        count+=1
        temp = temp.next

    return count
#Time Complexity - O(n)
#Space Complexity - O(1)
#Running Testcases
inputs = [[1, 2, 3], [], [1, 3]]
for elem in inputs:
    sll_obj = SLL()
    temp_head = sll_obj.insert(elem)
    print("The length of the linked list ",elem, get_length(temp_head))