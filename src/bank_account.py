class BankAccount():
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance+amount
        #self.balance = self.balance
        print("Rs.{} deposit accepted".format(amount))

    def withdrawal(self,amount):
        new_bal = self.balance-amount
        if new_bal<0:
            print("There are no sufficient funds")
        else:
            self.balance -= amount
            print("Rs.{} has been withdrawn and current balance is Rs.{}".format(amount,self.balance))
