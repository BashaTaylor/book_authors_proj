class BankAccount:
    def __init__(self, intRate=0.01, balance=0):
        self.balance = balance
        self.intRate = intRate

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if(amount < self.balance):
            self.balance -= amount
        else:
            print("Unable to process the withdrawal. Insufficient funds: Charging a $5 fee.")
            self.balance -= 5
        return self

    def displayAccountInfo(self):
        print("Balance:", self.balance)
        return self
    
    def yieldInterest(self):
        if(self.balance >= 0):
            self.balance += self.balance*self.intRate
            self.intRate += self.balance * self.intRate
            print(f"Your monthly interest deposit is ${self.intRate}.")
        return self

# Update the User class __init__ method  
# Update the User class make_deposit method  
# Update the User class make_withdrawal method  
# Update the User class display_user_balance method

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount()

    def makeDeposit(self, amount):
        self.account.deposit(amount)
        print(f"Deposit amount ${amount}")
        return self

    def makeWithdrawal(self, amount):
        self.account.withdraw(amount)
        print(f"Withdrawal amount ${amount}")
        return self

    def displayUserBalance(self):
        self.account.displayAccountInfo()
        return self

matt = User("Matt Davis", "mcdavis@gmail.com")

matt.makeDeposit(500).makeWithdrawal(40).makeWithdrawal(500).displayUserBalance()
matt.account.yieldInterest().displayAccountInfo()
matt.displayUserBalance()