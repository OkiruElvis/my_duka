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

class BankAccount:
    def __init__(self, account_number, balance, owner_name, date_opened):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened

    # Deposit method
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited successfully.")
        print(f"New balance: {self.balance}")

    # Withdraw method
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.")
            print(f"New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    # Display account information
    def display_info(self):
        print("\n--- Bank Account Information ---")
        print(f"Account Number: {self.account_number}")
        print(f"Owner Name: {self.owner_name}")
        print(f"Balance: {self.balance}")
        print(f"Date Opened: {self.date_opened}")


# Creating the first BankAccount object
account1 = BankAccount("ACC001",50000,"Elvis Okiru","25-08-2026")

# Creating the second BankAccount object
account2 = BankAccount("ACC002",30000,"Wendy Albright","25-08-2026")


# Account 1 operations
account1.display_info()
account1.deposit(20000)
account1.withdraw(5000)
account1.display_info()


# Account 2 operations
account2.display_info()
account2.deposit(8000)
account2.withdraw(10000)
account2.display_info()