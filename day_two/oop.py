class BankAccount:
    def withdraw(self):
        pass

    def deposit(self):
        pass

class SavingsAccount(BankAccount):      #class SavingsAccount inherits from class BankAccount
    def __init__(self, balance=500):    #constructor that takes self argument and sets balance to 500
        self.balance = balance

    def deposit(self, amount):          #deposit method that takes an argument called amounts
        if (amount <= 0):
            return "Invalid deposit amount" #return Invalid deposit amount if amount is negative
        else:
            self.balance += amount      #add amount to balance 
        return self.balance

    def withdraw(self, amount):         #withdraw method that takes an argument called amounts
        if(amount <= 0):
            return "Invalid withdraw amount"
        elif(self.balance <= 500):      #check if balance is less than or equal to 500
            return "Cannot withdraw beyond the minimum account balance"
        elif(amount > self.balance):    #check if amount is greater than balance
            return "Cannot withdraw beyond the current account balance"
        else:
            self.balance -= amount      #deduct amount from balance 
            return self.balance    


class CurrentAccount(BankAccount):      #class CurrentAccount inherits from class BankAccount
    def __init__(self, balance=0):      #constructor that takes self argument and sets balance to 0
        self.balance = balance

    def deposit(self, amount):
        if (amount <= 0):               
            return "Invalid deposit amount" #return Invalid deposit amount if amount is negative
        else:
            self.balance += amount       #add amount to balance 
            return self.balance

    def withdraw(self, amount):
        if (amount <= 0):                   #check if amount is less than 0
            return "Invalid withdraw amount"
        elif (amount >= self.balance):      #check if amount is greater than or equal to balance
            return "Cannot withdraw beyond the current account balance"
        else:
            self.balance -= amount          #deduct amount from balance
        return self.balance