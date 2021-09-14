# class User:		# here's what we have so far
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.account_balance = 0
#     # adding the deposit method
#     def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
#         self.account_balance += amount	# the specific user's account increases by the amount of the value received
# guido = User("Guido van Rossum", "guido@python.com")
# guido.make_deposit(100)
# guido.make_deposit(200)
# print(guido.name)	# output: Guido van Rossum
# print("Balance: $",guido.account_balance)

# monty = User("Monty Python", "monty@python.com")
# monty.make_deposit(50)
# print(monty.name)	# output: Monty Python
# print("Balance: $",monty.account_balance)	# output: 50



# # User
class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_withdrawal(self, amount):	# takes an argument that is the amount of the withdrawal
        self.account_balance -= amount

    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount
    def display_user_balance(self):
        print (f"User: {self.name}, Balance: {self.account_balance}")
    # def transfer_money(self, other_user, amount ):
    #     self.account_balance -= amount
    #     self.other_user += amount
    

chris = User("Chris Davis", "chris@gmail.com")
jim = User("Jim Mathews", "jim@gmail.com")
jane = User("Jane Smith", "jane@gmail.com")

chris.make_deposit(100)
chris.make_deposit(140)
chris.make_deposit(520)
chris.make_withdrawal(40)
chris.display_user_balance()

jim.make_deposit(150)
jim.make_deposit(200)
jim.make_withdrawal(20)
jim.make_withdrawal(40)
jim.display_user_balance()

jane.make_deposit(2000)
jane.make_withdrawal(220)
jane.make_withdrawal(40)
jane.make_withdrawal(100)
jane.display_user_balance()





