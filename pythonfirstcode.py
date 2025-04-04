class Account:
    def __init__(self, balance, account_no):
        self.balance = int(balance)  # Convert balance to an integer
        self.account_no = account_no
        
    def debit(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else: 
            self.balance -= amount  # Correct subtraction
            print(f"Amount debited: {amount}. New balance: {self.balance}")

    def credit(self, amount):
        self.balance += amount  # Correct addition
        print(f"Amount credited: {amount}. New balance: {self.balance}")

    def prt(self):
        print("Your account balance is:", self.balance)
    
# Creating an instance of Account
s1 = Account(1000, "1010301")  # Balance should be an integer

# Performing transactions
s1.debit(int(input('Withdraw: ')))   
s1.credit(int(input('Deposit: ')))  
s1.prt()        # Print balance


