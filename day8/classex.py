class Passbook:
    def __init__ (self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, balance):
        self.balance+=balance
        print(f"입금 잔액: {balance}", end="\t")
        print(f"현재 잔액: {self.balance}")
        print()
    
    def withdraw(self, m):
        if self.balance-m < 0 :
            print("잔액 부족", end='\t')
            print(f"현재 잔액: {self.balance}")
            print()
        else : 
            self.balance -= m
            print(f"출금 잔액: {m}", end="\t")
            print(f"현재 잔액: {self.balance}")
            print()

    def showInfo(self):
        print(f"예금주: {self.owner}",end="\t")
        print(f"현재 잔액: {self.balance}")
        print()

class MinusPassbook(Passbook):
    def withdraw(self, m):
        if self.balance - m < -1000000:
            print("잔액 부족", end="\t")
            print(f"현재 잔액: {self.balance}")
            print()
        else :
            self.balance -= m
            print(f"출금 잔액: {m}", end="\t")
            print(f"현재 잔액: {self.balance}")
            print()

account1 = Passbook("홍길동", 100000)
account1.showInfo()
account1.deposit(50000)
account1.withdraw(120000)
account1.withdraw(70000)

account2 = MinusPassbook("김철수", 100000)
account2.showInfo()
account2.withdraw(120000)
account2.withdraw(900000)
        