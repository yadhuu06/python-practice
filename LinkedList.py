class node:
    def __init__(self,data):
        self.data=data 
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newNode=node(data)
        
        if not self.head:
            self.head=newNode
            return 
        current=self.head
        while current.next:
            current=current.next
        current.next=newNode
    def display(self):
        current=self.head
        while current:
            print(current.data ,end="   ")
            current=current.next
    def reverse(self):
        current=self.head
        prev=None
        while current:
            nextNode=current.next
            current.next=prev
            prev=current
            current=nextNode
        self.head=prev
        
        
            
        

li=linkedList()
li.insert(10)
li.insert(20)
li.insert(30)
li.display()
li.reverse()
li.display()

        
        
        
 #  1->2->3->4->5
 
        

        
        
        
        
