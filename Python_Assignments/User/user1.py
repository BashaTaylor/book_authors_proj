#User
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def display_user_balance(self):
        print (f"User: {self.name}, Balance: {self.account_balance}")
        return self
    

chris = User("Chris Davis", "chris@gmail.com")
jim = User("Jim Mathews", "jim@gmail.com")
jane = User("Jane Smith", "jane@gmail.com")

chris.make_deposit(100).make_deposit(140).make_deposit(520).make_withdrawal(40).display_user_balance()

jim.make_deposit(150).make_deposit(200).make_withdrawal(20).make_withdrawal(40).display_user_balance()

jane.make_deposit(2000).make_withdrawal(220).make_withdrawal(40).make_withdrawal(100).display_user_balance()
