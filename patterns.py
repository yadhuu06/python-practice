n=3
# out:
# ***
# **
# *
for i in range(n,0,-1):
    for j in range(i):
        print("*" ,end="")
    print()
    



# out:
#     * * *
#      * *
#       *

for i in range(n,0,-1):
    
    print(" " * (n - i) + "* " * i)  


n=5

# out:
# 1
# 2 3
# 4 5 6


n=3
k=1
for i in range(1,n+1):
    for j in range(i):
        print(k,end=" ")
        k+=1
    print()
    
n=4
for i in range(n):
    a=" "*i
    b=n-i
    print(a+"*"*b)      
       


    
    

       