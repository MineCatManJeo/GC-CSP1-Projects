# Gabriel Crozier, Comments Proficiency Test

class BankAccount: # defines class called bank account
    def __init__(self, account_number, balance=0): # Initial function in the class BankAccount
        self.account_number = account_number # Defines account number variable
        self.balance = balance # Defines balance variable

    def deposit(self, amount): # Defines deposit function
        if amount > 0: # Conditional if amount is greater than 0
            self.balance += amount # Adds amount to balance
            return True # Returns the value True
        return False # Returns false

    def withdraw(self, amount): # Defines the withdraw function
        if 0 < amount <= self.balance: # Conditional if 0 is less than amount and if amount is less than or equal to balance
            self.balance -= amount # Subtracts amount from balance
            return True # returns True
        return False # returns False

    def get_balance(self): # Defines get_balance function
        return self.balance # returns balance

def create_account(): # Defines create account function
    account_number = input("Enter account number: ") # Sets account num to an input from the user
    initial_balance = float(input("Enter initial balance: ")) # Also sets initial balance from user input
    return BankAccount(account_number, initial_balance) # Returns value from BankAccount class

def main(): # Defines main function
    accounts = {} # Declares accounts value
    while True: # Repeats next code until a break
        # Prints options
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ") # Let's you choose
        
        if choice == '1': # If user chose 1:
            account = create_account() # account is now the newly created account
            accounts[account.account_number] = account # Sets a value in a list to account
            print(f"Account {account.account_number} created successfully!") # prints success
        
        elif choice in ['2', '3', '4']: # If your choise is 2, 3, or 4
            account_number = input("Enter account number: ") # User inputs account number
            if account_number in accounts: # if the number is already in accounts continue
                account = accounts[account_number] # current account is now the account you chose
                if choice == '2': # If you chose 2
                    amount = float(input("Enter deposit amount: ")) # defines amount variable
                    if account.deposit(amount): # Deposits money and should return true
                        print(f"Deposited ${amount:.2f} successfully!") # if returned true print success
                    else:
                        print("Invalid deposit amount.") # if not print no success
                elif choice == '3': # if user inputted 3
                    amount = float(input("Enter withdrawal amount: ")) # defines amount
                    if account.withdraw(amount): # withdraws amount in this function and returns true / false
                        print(f"Withdrawn ${amount:.2f} successfully!") # if true print success
                    else:
                        print("Invalid withdrawal amount or insufficient funds.") # if false print no success
                else:
                    print(f"Current balance: ${account.get_balance():.2f}") # if you chose 4 get account balence
            else:
                print("Account not found.") # shows that account isn't found
        
        elif choice == '5': # if user inputted 5
            print("Thank you for using our banking system. Goodbye!") # prints exit
            break # leaves function
        
        else:
            print("Invalid choice. Please try again.") # Repeats loop because user was dumb

if __name__ == "__main__": # Makes sure the program only runs on the main.py file
    main()