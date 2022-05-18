class BankAccount:
    """BankAccount which represents a bank account"""
    bank_fee = 0.95
    def __init__(self, accountNumber: int, name, balance: int):
        assert len(str(accountNumber)) >= 16, f"Account number {accountNumber} should contain at least 16 characters"
        assert balance >= 0, f"Balance {balance} is negative"
        self.accountNumber = accountNumber
        self.name = name
        self.balance = balance
    
    def Deposit(self, dep):
        if dep <= 0:
            print("Unsufficient sum")
        else:
            self.balance = self.balance + dep
    def Withdrawal(self, withdraw):
        if withdraw > self.balance:
            print("You don't have enough funds")
        else: 
            self.balance = self.balance - withdraw
    def bankFees(self):
        self.balance = self.balance * self.bank_fee
    def display(self):
        print("Account number: ", self.accountNumber)
        print("Account name: ", self.name)
        print("Balance: ", self.balance)

bank_account1 = BankAccount(1567468767657255, "Elena Danielyan", 1000000)

bank_account1.Deposit(-5000)
bank_account1.Withdrawal(1000002)
bank_account1.bankFees()
bank_account1.display()
