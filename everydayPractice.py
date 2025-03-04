# # arr=["haii","hello",{"age":16},12,5.5,{"age":10}]
# # total=0
# # for i in arr:
# #     if type(i).__name__=="dict":
# #         total+=sum(i.values())
# # print(total)



# def merge(arr):
#     if len(arr)==1:
#         return arr
#     n=len(arr)//2
#     left=merge(arr[:n])
#     right=merge(arr[n:])
#     return mergeSort(left,right)
# def mergeSort (left,right):
#     i=j=0
#     res=[]
#     while i<len(left)and j<len(right):
#         if left[i]<right[j]:
#             res.append(left[i])
#             i+=1
#         else:
#             res.append(right[j])
#             j+=1
#     res.extend(left[i:])
#     res.extend(right[j:])
#     return res

# arr=[2,5,3,1,56,23,2,8,54]
# print("merge sort out:",merge(arr))


# def insertion(arr):
#     for i in range(1,len(arr)):
#         j=i-1
#         key=arr[i]
#         while j>=0 and arr[j]>key:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=key
#     return arr

# print("ins:",insertion(arr))
        
        
                 
            
             
        


 
def insert(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j]=key
    return arr
print("insertion",insert([12,4,5,3,23]))



def merge (arr):
    n=len(arr)//2
    if len(arr)==1:
        return arr
    left=merge(arr[:n])
    right=merge(arr[n:])
    return mergeSort(left,right)
def mergeSort(left,right):
    i=j=0
    res=[]
    while i<len(left)and j<len(right):
        if left[i]>right[j]:
            res.append(right[j])
            j+=1
        else:
            res.append(left[i])
            i+=1
            
    res.extend(left[i:])
    res.extend(right[j:])
    return res
print("merge",merge([21,4,5,23,21,2,97]))


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
    def display (self):
        current=self.head
        while current:
            print(current.data,end=" ")
            current=current.next
            
    def reverse(self):
        prev=None
        current=self.head
        while current:
            nextNode=current.next
            
            current.next=prev
            prev=current
            current=nextNode
        self.head=prev
        
        


li=linkedList()
li.insert(18)
li.insert(8)
li.insert(118)
li.insert(181)
li.display()
li.reverse()
li.display()

    
              
            
     
     
     
   
        