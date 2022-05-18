class BankAccount:
    
    '''This class represents a bank account, having as attributes 
    > account number
    > name of the account owner
    > the account balance'''

    fee = 0.95

    def __init__(self, accountNumber: int, name: str, balance: int):
        assert balance >= 0, f"balance {balance} is not greater than or equal to 0"
        
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    
    def __repr__(self):
        return f"{self.accountNumber}, {self.name}, {self.balance}"
    
    def bankFees(self):
        self.balance = self.balance * BankAccount.fee

    def deposit(self, x: int):
        self.balance += x
         
    def withdrawal(self, y: int):
        assert y <= self.balance, f"you don't have enough funds, your balance is {self.balance}"
        self.balance -= y 
    
    def display(self):
        print (f"({self})")
        

account1 = BankAccount(2410029002651, "liza safaryan", 0)
account2 = BankAccount(2410029002651, "samvel poghosyan", 6500)       