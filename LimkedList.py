class node:
    def __init__(self,val):
        self.val=val
        self.next=None
    
class linkedList:
    def __init__(self):
        self.head=None
        
    def insert(self,val):
        newNode=node(val)
        
        if not self.head:
            self.head=newNode
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=newNode
            return 
   

    
    
li=linkedList()
li.insert(15)
li.insert(19)
li.insert(145)
li.insert(154)
        
       
        
        
        
        
        

        
        
        
        
