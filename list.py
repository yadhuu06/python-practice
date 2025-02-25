# find the second largest of even numbers

arr=[12,32,412,35,45,87,420,41,65,44,65,98]
larg=0
seclarge=0

for i in arr:
    if i%2==0:
        if i >larg:
            seclarge=larg
            larg=i
        if i<larg and i>seclarge:
            seclarge=i
print(seclarge)
