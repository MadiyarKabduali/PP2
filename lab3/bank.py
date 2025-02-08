class Account:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self,amo):
        self.balance+=amo
        print(f"Dep:{amo} balance:{self.balance}")
    
    def withdraw(self,amo):
        if amo>self.balance:
            print("No balance")
        else:
            self.balance -= amo
            print(f"Wdrw:{amo} balance: {self.balance}")
acc = Account("John", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(150)