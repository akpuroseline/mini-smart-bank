#functions
def deposit(balance,amount):
    return balance + amount

def withdraw (balance,amount):
    return balance - amount

def display_balance(balance):
    print("Your balance is: ", balance)

#main program   

balance = 0
while True:
    print("Please select an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        amount = float(input("Enter the amount to deposit: "))
        balance = deposit(balance, amount)
        print("Deposit successful.")
    elif choice == '2':
        amount = float(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds.")
        else:
            balance = withdraw(balance, amount)
            print("Withdrawal successful.")
    elif choice == '3':
        display_balance(balance)
    elif choice == '4':
        print("Thank you for using the banking system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")