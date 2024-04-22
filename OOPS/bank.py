class bank:
    def __init__(self,accno,name,balance):
        self.accno=accno
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance+=amt
        return self.balance
    def withdraw(self,amt):
        if amt>self.balance:
            return "Insufficient balance"
        else:
            self.balance-=amt
            return self.balance
    def bal_enq(self):
        return self.balance
a,b,c=[x for x in input().split()]  
d=int(input("deposite amount:"))
e=int(input("withdraw amount:"))
p=bank(a,b,c)
print(p.deposit(d))
print(p.withdraw(e))
print(p.bal_enq())
