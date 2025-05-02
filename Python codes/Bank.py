def show_balance():
    print("------------------------")
    print(f"Your balance is ${balance:.2f}")
    print("------------------------")

def deposit(amount):
    print("------------------------")
    print(f"You added ${amount:.2f} to your balance")
    return amount

def withdraw(amount):
    if amount <= 0:
        print("------------------------")
        print("Must be a number bigger than 0! Try again.")
        return 0
    if amount > balance:
        print("------------------------")
        print("Insufficient funds! Try again.")
        return 0
    else:
        return amount

balance = 0.0

def main():

    global balance
    print(f"------------------------")
    print("Welcome to the bank")
    print("Options: balance, deposit, withdraw, q (quit)")

    while True:
        do = input("What do you want to do? (q to quit) : ").lower()
        if do == "balance":
            show_balance()
        elif do == "deposit":
            balance += deposit(float(input("------------------------\nPlease enter the deposit amount : ")))
        elif do == "withdraw":
            balance -= withdraw(float(input("------------------------\nPlease enter the withdraw amount : ")))
        elif do == "q":
            break
        else:
            print("------------------------")
            print( "Your input is invalid! Try again.")
            print("------------------------")

    print("------------------------")
    print(f"You exited with a balance of ${balance:.2f}.")
    print("------------------------")

if __name__ == "__main__":
    main()   