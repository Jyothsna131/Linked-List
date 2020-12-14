# Linked List

# Create Node
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node

    def print_data(self):
        curr=self.head
        while(curr):
            print(curr.data)
            curr=curr.next

l1=LinkedList()
l=[1,2,3,10,9]
for ele in l:
    l1.insert(ele)
l1.print_data()
    
    
        
