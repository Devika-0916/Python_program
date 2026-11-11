class BankAccount:
    def __init__(self):
        self.balance=0
        print("Welcom to the bank")
    def deposite(self):
        amount=float(input("Enter amount to be deposited:"))
        self.balance+=amount
        print("Amount deposited:",amount)
    def withdraw(self):
        amount=float(input("Enter amount to be withdran:"))
        if self.balance>=amount:
            self.balance -=amount
            print("Amount Withdrawn:",amount)
        else:
            print("Insufficient balance")
    def display(self):
        print("Net available balance=",self.balance)

account1=BankAccount()
account1.deposite()
account1.withdraw()
account1.display()




