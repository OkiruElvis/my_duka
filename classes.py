from datetime import datetime

today = datetime.today()
print(today)


# class Person:
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender

#     def talks(self,words):
#         print(f"{self.name} talks and said {words}")

#     def smiling(self,gesture):
#         print(f"{self.name} likes smiling {gesture}")

#     def display_info(self):
#         print('----------Object Info---------')
#         print(f'Name: {self.name}')
#         print(f'Age: {self.age}')
#         print(f'Gender: {self.gender}')

# #person1 object
# person1=Person('Jane Kamau', 24, 'Female')
# print(type(person1))
# # print(person1.name)
# # print(person1.age)
# # print(person1.gender)
# person1.display_info()
# person1.talks('OOP is very easy.')
# person1.smiling('making her very accomodative.')

# print('---------------------------------------------')

# #person2 object
# person2=Person('Jack',25,'Male')
# print(type(person2))
# # print(person2.name)
# # print(person2.age)
# # print(person2.gender)
# person2.display_info()
# person2.talks('Python is a very hard language.')
# person2.smiling('which makes it easy for anyone to mingle with him.')




# Task on OOP 1.Create a class called BankAccount with the following attributes: -account number -balance -owner name -date opened 
# 2.Give the above BankAccount class the following behaviour or methods: -deposit() -withdraw() -display_info() 
# 3.Create two BankAccount objects that can deposit, withdraw and display_info

# class BankAccount:
#     def __init__(self,acc_no,balance,owner_name,date_opened=today):
#         self.account_number = acc_no
#         self.balance = balance
#         self.owner_name = owner_name
#         self.date_opened = date_opened

#     def deposit(self,amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"{self.owner_name} deposited Ksh.{amount} to account: {self.account_number} \n New Balance is {self.balance}")
#         else:
#             print("Invalid amount entered,try again")


#     def withdraw(self,amount):
#         if amount > self.balance and amount < 0:
#             print("Cannot complete withdrawal,invalid amount")
#         else:
#             self.balance -= amount
#             print(f"{self.owner_name} has withdrawn Ksh.{amount} from account: {self.account_number} \n New Balance is {self.balance}")


#     def display_info(self):
#         print("-------My Bank Account Info-------")
#         print(f"Acc No: {self.account_number}")
#         print(f"Balance: {self.balance}")
#         print(f"Owner Name: {self.owner_name}")
#         print(f"Date Opened: {self.date_opened}")


# account1 = BankAccount("Acc001",0,"Jane")
# account1.deposit(10000)
# account1.withdraw(3000)
# account1.display_info()



class Animal:
    def __init__(self,name,type):
        self.name = name
        self.type = type

    def make_sound(self):
        print(f"{self.name} makes some sound")


class Dog(Animal):
    def __init__(self, name, type,age):
        super().__init__(name, type)
    
        self.age = age 

    def make_sound(self):
        print(f"{self.name} says woof!")


dog1 = Dog("Max","German Shepherd",5)
print(dog1.name)
dog1.make_sound()