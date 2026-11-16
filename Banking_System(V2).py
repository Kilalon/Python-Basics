current_balance = 0

def balance():
    print(f"Your current balance is: ${current_balance}")

def deposit(current_balance):
    deposit_amount = float(input("How much would you like to deposit?: "))
    current_balance += deposit_amount
    print(f"You have deposited an amount of ${deposit_amount}")
    print(f"Your current balance is now ${current_balance}")
    return current_balance

def withdraw(current_balance):
    withdraw_amount = float(input("How much would you like to withdraw?: "))
    
    if withdraw_amount > current_balance and current_balance != 0:
        withdraw_all = input(f"You do not have that much to withdraw, would you like to withdraw the remaining of ${current_balance} that you have left? (yes/no)").lower()
        if withdraw_all == "yes":
            current_balance = 0
            print("You have withdrawn all that is remained in your account!")
            return current_balance
        elif withdraw_all == "no":
            print("You havn't withdrawn anything from your account!")
    elif current_balance == 0:
        print("You  have zero dollars in your account!")
    else:
        current_balance -= withdraw_amount
        print(f"You have withdrawn an amount of ${withdraw_amount}")
        print(f"Your current balance is now ${current_balance}")
        return current_balance

while True:
    print("Would you like to check your balance, deposit, or withdraw?")
    user_input = input("Check balance / deposit / withdraw: ").lower()

    match user_input:
        case "check balance":
            balance()
        case "deposit":
            current_balance=deposit(current_balance)
        case "withdraw":
            current_balance=withdraw(current_balance)

    again = input("Would you like to proceed with anything else? (Yes/no): ").lower()
    if again == "no":
        break
print("Have a nice day!")