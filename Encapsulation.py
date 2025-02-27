# class Account:
#     def __init__(self,balance):
#         self.__balance=balance
#     def deposit(self,amt):
#         self.__balance+=amt
#         return
#     def withdrowal(self,amt):
#         if amt<self.__balance:
#             self.__balance-=amt
#             return print("success")
#         return print( "insufficient balance")
#     def GetBalance(self):
#         return print("your balance is",self.__balance)
        

# ac=Account(15000)
# ac.deposit(10000)
# ac.withdrowal(15000)
# # print(ac.__balance)"only with the proper way can acces th protected variables" no direct acces is allowed
# ac.GetBalance() 

