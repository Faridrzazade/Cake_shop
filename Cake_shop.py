
import random 
import time

cakes = {
    "Chocolate Cake": {
        "name": "Chocolate Cake",
        "ingredients": ["chocolate", "flour", "sugar", "eggs"],
        "price": 25,
        "regular": True,
        "sweet": True,
        "stock": 10
    },

    "Vanilla Cake": {
        "name": "Vanilla Cake",
        "ingredients": ["vanilla", "flour", "sugar", "eggs"],
        "price": 20,
        "regular": True,
        "sweet": True,
        "stock": 5
    },

    "Carrot Cake": {
        "name": "Carrot Cake",
        "ingredients": ["carrots", "flour", "sugar", "eggs"],
        "price": 28,
        "regular": True,
        "sweet": False,
        "stock": 8
    },

    "Fruit Cake": {
        "name": "Fruit Cake",
        "ingredients": ["fruit", "flour", "sugar", "eggs"],
        "price": 30,
        "regular": True,
        "sweet": True,
        "stock": 6
    }
}
def show_available_cakes():
    print("available cakes:")
    for cake in cakes:
        print(f"-{cake}: ${cakes[cake]["price"]}")

def calculate_price(cake_name, quantity, want_full=True):
    if cake_name not in cakes:
        print("We dont have that cake.")
        return 0

    if quantity > cakes[cake_name]["stock"]:
        print("we dont have enough stock for that cake.")
        return 0
    cake_price = cakes[cake_name]["price"]
    total_price = cake_price * quantity

    if not want_full:
        total_price /= 2

    return total_price

def sell_cake():
    print("Welcome to our cake shop!")
    show_available_cakes()

    cake_choice = input("Plese select a cake \n:").title()
    quantity = int(input("How many do you want? \n:"))
    want_full = input("do you want the full cake? (yes/no) \n :").lower() == "yes"

    price = calculate_price(cake_choice, quantity, want_full)
    if price > 0:
        print(f"Total price: ${price}")

        update_cash_register(price)

        update_stock(cake_choice, quantity)
    else:
        print("Sorry, we couldnt process your order.")

def update_cash_register(amount):
    print("Updating cash register...")
    time.sleep(2)
    print(f"Added ${amount} to cash register.")

def update_stock(cake_name, quantity_sold):
    cakes[cake_name]["stock"] -= quantity_sold

sell_cake()