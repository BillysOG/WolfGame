import random as r
import time as t

def spin_row():
    symbols = ["⭐", "🍒", "🍕", "🌭", "🍔"]
    return [r.choice(symbols) for _ in range(3)]

def print_row(rng):
    print(*rng,sep=" ")
    if len(set(rng)) == 1:
        print("CONGRATULATIONS! YOU WON THE JACKPOT!")
        return 1
    elif len(set(rng)) == 2:
        print("Congrats! You won!")
        return 0
    else:
        print("Too bad! Better luck next time!")
        return -1

def get_payout(won,bet):
    if won == 0:
        x = bet * 2
    elif won == 1:
        x = bet * 10
    else:
        x = 0
    return x

def main():
    balance = 100

    print("******************************")
    print("Welcome to the casino!")
    print("Symbols : ⭐ 🍒 🍕 🌭 🍔")

    while balance > 0:
        print("******************************")
        print(f"Your balance is ${balance}!")
        try:
            bet = int(input("How much do you want to bet? : "))
        except ValueError:
            print("Input Invalid, Try again!")
            continue
        if bet > balance:
            print("Insufficient funds! Try again.")
            continue
        elif bet < 0:
            print("Invalid, bet must be greater than 0")
            continue
        else :
            balance -= bet
            print("Spinning.....\n")
            t.sleep(1)

            rng = spin_row()
            won = print_row(rng)
            money_won = get_payout(won,bet)
            if money_won > 0:
                print(f"You won ${money_won}")
            else:
                print("You didn't win anything!")
            balance += money_won
    print("\n******************************")
    print("Game over, you ran out of money!")
    print("HA HA HA LOSER!")

if __name__ == "__main__":
    main()