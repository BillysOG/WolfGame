shop = {"pizza" : 5.50,
        "fries" : 2.50,
        "soda" : 3.00,
        "popcorn" : 7.00,
        "mash potatoes" : 8.50,
        "wedges" : 7.00,
        "burger" : 8.00,
        "hotdog" : 6.50,}

cart = []
total = 0

print("----------- MENU -----------")
for key,value in shop.items():
    print(f"{key:14} : ${value:.2f}")
print("----------------------------")

while True:
    bought = input("What do you want to buy? (q to quit) : ").lower()
    if bought == "q":
        break
    elif shop.get(bought) is not None:
        cart.append(bought)

cart_items = ", ".join(cart)
total = sum(shop[bought] for bought in cart)
print("----------------------------")
print(f"You have bought : {cart_items}")
print(f"Your total is   : ${total:.2f}")
print("----------------------------")