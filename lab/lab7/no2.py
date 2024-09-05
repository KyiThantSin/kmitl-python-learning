class BankAccount:
    def __init__(self, bank_name, owner_name, account_number, current_balance = 0):
        self.bank_name = bank_name
        self.owner_name = owner_name
        self.account_number = account_number
        self.current_balance = current_balance

    def deposit(self, amount = 0):
        self.current_balance += amount
    
    def withdraw(self, amount = 0):
        if amount < self.current_balance:
            self.current_balance -= amount
        else:
            print("Not Enough. Your current Balance", self.current_balance)
   
    def print_out(self):
        print("Bank Name: ", self.bank_name)
        print("Owner Name: ", self.owner_name)
        print("Account Number: ", self.account_number)
        print("Current Balance: $", self.current_balance,)


user = BankAccount("SCB", "John", "23463")
user.deposit(4000)
user.withdraw(2000)
user.print_out()