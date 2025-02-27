# # Write a function analyze_data_types(lst) that takes a list of elements and
# # returns a dictionary with counts of each data type.

# data = [1, 2.5, "hello", True, (1, 2), [3, 4], {1, 2}, {"key": "value"}, False, 3.14]
# def analyze_data_types(data):
#     a={}
#     for i in data:
#         typ=type(i).__name__
#         if typ in a:
#             a[typ]+=1
#         else:
#             a[typ]=1
#     return a
        

# print(analyze_data_types(data))


# student={"name":"aleena"
#          ,"age":19
#          ,"course":"bcom"
#          ,"place":"kannur"}
# print(student)
# student.pop("age")
# print(student)



# q
# Create a function word_count(sentence) that returns a dictionary where:

# Keys are unique words in the sentence.
# Values are the number of times each word appears.

# sentence = "python is fun and learning python is great"
# def word_count(sentance):
#     wordCount={}
#     word=sentance.split()
#     for i in word:
#         if i in wordCount:
#             wordCount[i]+=1
#         else:
#              wordCount[i]=1
#     return wordCount
            
    
# print(word_count(sentence))


# students = {
#     "Alice": {"Math": 85, "Science": 90, "English": 88},
#     "Bob": {"Math": 92, "Science": 89, "English": 84},
#     "Charlie": {"Math": 78, "Science": 80, "English": 85}
# }



# def top_student(students):
#     myout={}
#     for i in students:
#         total=students[i]["Math"]+students[i]["Science"]+students[i]["English"]
#         myout[i]=total
#     mx=max(myout,key=myout.get)
#     return myout[mx]


# print(top_student(students))



# q
# products = [
#     {"name": "Laptop", "price": 800, "stock": 10},
#     {"name": "Phone", "price": 600, "stock": 5},
#     {"name": "Tablet", "price": 300, "stock": 0},
#     {"name": "Headphones", "price": 150, "stock": 7},
#     {"name": "Monitor", "price": 200, "stock": 3}
# ]

# top_n_expensive(products, 3)


# You have multiple sales records stored in a list of dictionaries, where each dictionary represents a sale with product, quantity, and price.

# Your task is to merge sales records by product and calculate the total revenue per product.








# q.
# Find the highest-paid employee in each department.
# Calculate the total salary expenditure per department.
# Return a new dictionary with department-wise highest salaries and total expenditures.


employees = {
    "HR": [
        {"name": "Alice", "salary": 50000},
        {"name": "Bob", "salary": 55000}
    ],
    "Engineering": [
        {"name": "Charlie", "salary": 80000},
        {"name": "David", "salary": 90000},
        {"name": "Eve", "salary": 85000}
    ],
    "Marketing": [
        {"name": "Frank", "salary": 60000},
        {"name": "Grace", "salary": 62000}
    ]
}


# heighest paid employee of each department

# for i in employees:
#     depvise={}
#     heighest=0
#     for j in employees[i]:
        
#         if j["salary"]>heighest:
#             heighest=j["salary"]
#             new=j
#     depvise[i]=new
#     print(depvise)

# import itertools


# players = ["Alice", "Bob", "Charlie", "David"]
# new=list(itertools.combinations(players,2))
# print(new)
            

        

    