class bank_account:
         def __init__(self,owner,balance):
            self.owner=owner
            self.balance=balance


         def deposit(self):
          q=int(input())
          self.balance=self.balance+q
          print(int(self.balance))

         def withdrawls(self):
            h=int(input())
            self.balance=self.balance-h
            if(int(self.balance)<0):
             print("There is no money")
             return
            else:
             print(self.balance)
             p.deposit()
             p.withdrawls()


p=bank_account("John",100)
p.deposit()
p.withdrawls()