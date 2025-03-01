def merge(arr):
    if len(arr)==1:
        return arr
    n=len(arr)//2
    
    left=merge(arr[:n])
    right=merge(arr[n:])
    return mergeSort(left,right)

def mergeSort(left,right):
    i=j=0
    res=[]
    while i <len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res

arr=[12,3,5,2,12,4,76]
# print(merge(arr))


def insert(arr):
    for i in range(1,len(arr)):
        j=i-1
        key=arr[i]
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
print(insert(arr))