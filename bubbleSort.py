def bubble (arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        
    return arr

arr=[12,4,45,2,3]
print(bubble(arr))