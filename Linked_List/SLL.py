from Node import Node
class SLL:
    def __init__(self):
        self.head = None
        self.prev = None
    def insert(self, val_list):
        for elem in val_list:
            node_obj = Node(elem, None)
            if self.head == None:
                self.head = node_obj
            else:
                self.prev.next = node_obj
            self.prev = node_obj
        return self.head
    def print_list(self):
        temp = self.head
        while temp!=None:
            print(temp.data, "---->", end=" ")
            temp = temp.next
        print("None")
                
            

