class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,newcome):
        
        self.newcome = newcome
        self.balance+=newcome

    def withdraw(self,outcome):
        
        self.outcome = outcome
        if self.balance >= outcome:
            self.balance-=outcome
        else:
            self.balance = 0

    def show(self):
        print(self.balance)


a = BankAccount("Altair",1000)
a.deposit(100)
a.withdraw(1500)
a.show()

