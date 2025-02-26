
# ///////without argument


# def mydec(fun):
#     def wrapper():
#         print("before my function")
#         fun()
#         print("after my function")
#     return wrapper
    
# @mydec
# def myfun():
#     print("this is myfun here")


# myfun()

# //////with arg

# def mydec(fun):
#     def wrapper(a,b):
#         print(a+b)
#         return fun()
#     return wrapper
    
# @mydec
# def hello():
#     print('helloooo')

# hello(10,15)

import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record end time
        print(f"Execution Time: {end_time - start_time:.5f} seconds")  # Print time taken
        return result  # Return function result if needed
    return wrapper  # Return the wrapped function

@time_it
def compute():
    sum([i for i in range(1000000)])

compute()

