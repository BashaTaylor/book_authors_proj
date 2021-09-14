# The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given,
# the balance of the account should initially be set to that amount; otherwise, the balance should start at $0.
# The account should also have an interest rate, saved as a decimal (i.e. 1% would be saved as 0.01),
# which should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)

# The class should also have the following methods:

# deposit(self, amount) - increases the account balance by the given amount
# withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds;
# if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
#
# display_account_info(self) - print to the console: eg. "Balance: $100"
# yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)

class BankAccount:
    def __init__(self, intRate=0, balance=0):
        self.intRate = intRate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit amount is ${amount}")
        return self

    def withdraw(self, amount):
        if(amount < self.balance):
            self.balance -= amount
            print(f"Withdrawal of ${amount}. New balance is ${self.balance}")
            return self
        else:
            self.balance -= 5
            nsf_fee = 5
            print(f"Insufficient funds to make this withdrawal. You are charged a ${nsf_fee} fee. Your balance is: ${self.balance}.")
        return self

    def displayAccountInfo(self):
        print(f"Current balance is: ${self.balance}")
        return self

    def yieldInterest(self):
        if(self.balance > 0):
            self.balance += (self.balance * self.intRate)
            self.intRate += self.balance * self.intRate
            print(f"Your monthly interest deposit is ${self.intRate}")
        return self

    def check_interest(self):  
        print(f"Interest is {self.intRate}%")
        return self


checking_account = BankAccount(0.01, balance=722)
savings_account = BankAccount(0.02, 1000)

checking_account.deposit(2000).deposit(200).deposit(50).withdraw(20).yieldInterest().displayAccountInfo()

savings_account.check_interest().deposit(1150).deposit(60).withdraw(100).withdraw(20).withdraw(3000).withdraw(20).yieldInterest().displayAccountInfo()



