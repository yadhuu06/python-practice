def quick(arr):
    if len(arr)==0:
        return arr
    pivot=arr[0]
    left=[x for x in arr if x<pivot]
    mid=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]
    return quick(left)+mid+quick(right)
arr=[1,4,23,5,12,9]
print(quick(arr))
    