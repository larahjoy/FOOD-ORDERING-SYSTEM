import datetime

# --- URBANBUN FOOD ORDERING SYSTEM ---

# Menu dictionary with items and prices
menu = {
    1: {"name": "The Classic", "price": 120},
    2: {"name": "Smoked Duo", "price": 189},
    3: {"name": "Golden Chick", "price": 159},
    4: {"name": "Truffle Fries", "price": 99},
    5: {"name": "Choco Urban Bliss", "price": 129},
    6: {"name": "Berry Cream Puff", "price": 119},
    7: {"name": "Lemon Fizz Cooler", "price": 89},
    8: {"name": "Choco Mocha Rush", "price": 110},
    9: {"name": "Urban Combo Meal", "price": 299},
    10: {"name": "Urban Burger Steak", "price": 189},
}

#  
def display_menu():
    print("\n🍔🍟 Welcome to UrbanBun Menu 🍹🍰")
    print("\nFOODS:")
    for key, item in menu.items():
        if key <= 4:
            print(f"{key}. {item['name']} – ₱{item['price']}")
    print("\nDESSERTS:")
    for key, item in menu.items():
        if 5 <= key <= 6:
            print(f"{key}. {item['name']} – ₱{item['price']}")
    print("\nDRINKS:")
    for key, item in menu.items():
        if 7 <= key <= 8:
            print(f"{key}. {item['name']} – ₱{item['price']}")
    print("\nOTHERS:")
    for key, item in menu.items():
        if key >= 9:
            print(f"{key}. {item['name']} – ₱{item['price']}")

# Function to display cart
def show_cart(cart):
    if not cart:
        print("\n🛒 Your cart is empty.")
        return
    print("\n--- 🧾 CURRENT CART ---")
    total = 0
    for i, (name, qty, price) in enumerate(cart, start=1):
        item_total = qty * price
        total += item_total
        print(f"{i}. {name} x{qty} = ₱{item_total:.2f}")
    print(f"Subtotal: ₱{total:.2f}")

# --- MAIN PROGRAM LOOP ---
while True:
    cart = []  # reset cart for every new order session

    while True:
        print("\n======= URBANBUN ORDERING SYSTEM =======")
        print("1. View Menu & Add Items")
        print("2. View Cart")
        print("3. Remove Item")
        print("4. Confirm Order")
        print("5. Cancel Order & Exit")

        choice = input("Enter your choice (1-5): ")

        # ADD ITEMS
        if choice == "1":
            display_menu()
            try:
                while True:
                    item_num = int(input("\nEnter item number (1-10) or 0 to stop: "))
                    if item_num == 0:
                        break
                    elif item_num in menu:
                        qty = int(input(f"Enter quantity for {menu[item_num]['name']}: "))
                        if qty <= 0:
                            print("Quantity must be greater than 0.")
                            continue
                        cart.append((menu[item_num]['name'], qty, menu[item_num]['price']))
                        print(f"✅ Added {qty} x {menu[item_num]['name']} to cart.")
                    else:
                        print("Invalid item number.")
            except ValueError:
                print("Invalid input, please enter a number.")

        # VIEW CART
        elif choice == "2":
            show_cart(cart)

        # REMOVE ITEM
        elif choice == "3":
            if not cart:
                print("Your cart is empty.")
            else:
                show_cart(cart)
                try:
                    remove_num = int(input("\nEnter item number to remove: "))
                    if 1 <= remove_num <= len(cart):
                        removed = cart.pop(remove_num - 1)
                        print(f"❌ Removed {removed[0]} from cart.")
                    else:
                        print("Invalid item number.")
                except ValueError:
                    print("Invalid input.")

        # CONFIRM ORDER
        elif choice == "4":
            if not cart:
                print("Your cart is empty. Add items first!")
                continue

            print("\n--- 🧾 ORDER SUMMARY ---")
            subtotal = 0
            for name, qty, price in cart:
                total = qty * price
                subtotal += total
                print(f"{name} x{qty} = ₱{total:.2f}")

            vat = subtotal * 0.10
            total_bill = subtotal + vat

            print(f"\nSubtotal: ₱{subtotal:.2f}")
            print(f"VAT (10%): ₱{vat:.2f}")
            print(f"TOTAL BILL: ₱{total_bill:.2f}")

            confirm = input("\nConfirm your order? (yes/no): ").lower()
            if confirm != "yes":
                print("Returning to main menu...")
                continue

            # --- PAYMENT PROCESS ---
            print("\n💳 PAYMENT OPTIONS")
            print("1. Cash")
            print("2. GCash")
            print("3. Card")

            payment_choice = input("Choose payment method (1-3): ")
            method = ""
            change = 0

            # UPDATED CASH SECTION WITH NOTIFICATION
            if payment_choice == "1":
                method = "Cash"
                while True:
                    try:
                        cash = float(input("Enter cash amount: ₱"))
                        if cash >= total_bill:
                            change = cash - total_bill
                            print(f"Payment successful! Change: ₱{change:.2f}")
                            break
                        else:
                            print("\n❌ PAYMENT FAILED")
                            print("We cannot take your money because it is LESS than the total bill.")
                            print(f"Your payment: ₱{cash:.2f}")
                            print(f"Total Needed: ₱{total_bill:.2f}")
                            print("Please enter an amount equal to or greater than the total.\n")
                    except ValueError:
                        print("Enter a valid amount.")

            elif payment_choice == "2":
                method = "GCash"
                input("Enter GCash number: ")
                print("Processing GCash payment... ✅")

            elif payment_choice == "3":
                method = "Card"
                input("Enter card number: ")
                print("Processing card payment... ✅")

            else:
                print("Invalid payment option.")
                continue

            # --- RECEIPT GENERATION ---
            now = datetime.datetime.now()
            print("\n===================================")
            print("          URBANBUN RECEIPT")
            print("===================================")
            print(f"Date: {now.strftime('%Y-%m-%d  %H:%M:%S')}")
            print("-----------------------------------")
            for name, qty, price in cart:
                item_total = qty * price
                print(f"{name:<25} x{qty:<2} ₱{item_total:>7.2f}")
            print("-----------------------------------")
            print(f"Subtotal:          ₱{subtotal:.2f}")
            print(f"VAT (10%):         ₱{vat:.2f}")
            print(f"TOTAL:             ₱{total_bill:.2f}")
            print(f"Payment:           {method}")
            if method == "Cash":
                print(f"Change:            ₱{change:.2f}")
            print("===================================")
            print("✅ THANK YOU FOR ORDERING AT URBANBUN!")
            print("        PLEASE COME AGAIN! 🍔\n")

            # Ask if user wants to order again
            again = input("Would you like to place another order? (yes/no): ").lower()
            if again == "yes":
                break  # restart order
            else:
                print("👋 Thank you for visiting UrbanBun! Have a great day!")
                exit()

        # CANCEL ORDER
        elif choice == "5":
            print("Order cancelled. Thank you for visiting UrbanBun!")
            exit()

        else:
            print("Invalid choice. Please choose 1–5.")