# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.
# Discuss in your group and come up with the attributes and three methods (behaviours)
# for each class and implement them
# Then do the following in the interpreter
# Create two instances of each class.
# Call each of the methods you defined.
class Account:
    balance=20000
    def __init__(self,name,number,balance):
        self.name=name
        self.number=number
        self.balance=balance
#Add these attributes and behaviours to the class Account
#Add attributes deposits and withdrawals in the init method which are empty lists
#by default and another attribute loan_balance which is zero by default.
        self.deposits=[]
        self.withdrawals=[]
        self.loan_balance=0
    def get_new_balance(self):
        return self.balance+self.deposits
    def get_details(self):
        return f"The owner of Account{self.number} is {self.name}."
    def confirm(self):
        return f"{self.name} is a KCB customer."
# Add a method check_balance which returns the account’s balance
    def check_balance(self):
        return self.balance
# Update the deposit method to append each withdrawal transaction to the deposits list.
#  Each transaction should be in form of a dictionary like this
# {
#    "amount": amount,
#    "narration": “deposit”
# }
    def check_deposit(self,amount):
        transaction = {"amount": amount, "narration": "deposit"}
        deposit_list=self.deposits.append(transaction)
        return deposit_list
# Update the withdrawal method to append each withdrawal transaction to the withdrawals list.
# Each transaction should be in form of a dictionary like like this
# {
#    "amount": amount,
#    "narration": “withdrawal”
# }
    def check_withdraw(self, amount2):
        transaction2 = {"amount": amount2, "narration": "withdrawal"}
        withdrawal_list=self.withdrawals.append(transaction2)
        return withdrawal_list
# Add a new method  print_statement which combines both deposits and withdrawals into one list and,
# using a for loop, prints each transaction in a new line like this
# deposit - 1000
# withdrawal - 500
    def print_statement(self):
        combined_list=self.deposits+self.withdrawals
        print(combined_list)
        for c in combined_list:
            print(f"{c['narration']} - {c['amount']}")
# Add a borrow_loan method which allows a customer to borrow if they meet these conditions:
# Account has no outstanding loan
# Loan amount requested is more than 100
# Customer has made at least 10 deposits.
# Amount requested is less than or equal to 1/3 of their total sum of all deposits.
# A successful loan increases the loan_balance by requested amount
    def borrow_loan(self,loan_amount):
        total_deposits = sum(transaction["amount"] for transaction in self.deposits)
        if self.loan_balance==0 and loan_amount>100 and len(self.deposits)>=10 and loan_amount > total_deposits / 3:
           return
        self.loan_balance+=loan_amount
        self.balance+=loan_amount
# Add a repay_loan method with this functionality
# A customer can repay a loan to reduce the current loan_balance
# Overpayment of a loan increases the accounts current balance
    def repay_loan(self,amount):
        self.loan_balance-=amount
        if amount>self.loan_balance:
            extra=self.loan_balance-amount
            self.balance+=extra
# Add a transfer method which accepts two attributes (amount and instance of another account).
# If the amount is less than the current instances balance, the method transfers the requested amount from the
# current account to the passed account. The transfer is accomplished by reducing the current account balance
# and depositing the requested amount to the passed account.
    def transfer(self,amount,other_account):
        other_account=Account
        if self.balance> amount:
            return
        self.balance -= amount
        other_account.check_deposit