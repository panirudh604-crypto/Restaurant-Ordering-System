#RESTAURANT ORDERING SYSTEM..........

menu = {'Burger':120,
        'Pizza':250,
        'Shawarma':140,
        'Fried Rice':160,
        'Chicken Biryani':180,
        'Veg Noodles':150,
        'Sandwich':90,
        'French Fries':100,
        'Coffee':50,
        'Lime Juice':80,
        'Chocolate Milkshake':140,
        'Ice Cream':70}
order = {}
saved_orders = []
def display_menu():
    print('=' * 79)
    print(f'{'Restaurant Ordering System':^75}')
    print('=' * 79)
    print("1. View Menu")
    print("2. Place Order")
    print("3. View Current Order")
    print("4. Update Quantity")
    print("5. Remove Item")
    print("6. Search Menu Item")
    print("7. Generate Bill")
    print("8. Save Order")
    print("9. View Previous Orders")
    print("10. Exit")
    print("-" * 79)
    print()

def view_menu():
    print()
    print("=" * 60)
    print(f'{'MENU':^55}')
    print("=" * 60)
    print(f'{'Item':<50} {'Price'}')
    print('-' * 60)
    for k, v in menu.items():
        print(f"{k:<50} \u20B9 {v}")
    print('-' * 60)
    print()

def place_order():
    while True:
        while True:
            item = input("\nEnter item: ").title()
            if item not in menu:
                print(f"{item} is not available.")
            else:
                break
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    print()
                else:
                    break
            except ValueError:
                print("Please enter a valid number.")
                print()
        if item in order:
            order[item] += quantity
        else:
            order[item] = quantity
        print(f"{item} added successfully.")
        while True:
            more = input("\nWould you like to add another item? (Y/N): ").upper()
            if more == "Y":
                break
            elif more == "N":
                print()
                return
            else:
                print("Invalid choice.Please enter Y or N.")

def view_current_order():
    if not order:
        print("Your order is empty.")
        print()
    else:
        total = 0
        print()
        print("=" * 62)
        print(f'{'CURRENT ORDER':^55}')
        print("=" * 62)
        print(f'{"Item":<30}{"Qty":>8}{"Price":>10}{"Total":>12}')
        print('-' * 62)
        for item, quantity in order.items():
            price = menu[item]
            subtotal = price * quantity
            total += subtotal
            print(f'{item:<30}{quantity:>8}{("₹" + str(price)):>10}{("₹" + str(subtotal)):>12}')
        print("-" * 62)
        print(f'{"Grand Total"}{("₹" + str(total)):>49}')
        print()

def update_quantity():
    if not order:
        print("Your order is empty.")
        print()
    else:
        while True:
            check = input("\nEnter item to update:").title()
            if check not in order:
                print(f"{check} not found in your order.")
                print()
            else:
                break
        while True:
            try:
                qty = int(input("Enter new quantity:"))
                if qty <= 0:
                    print("Invalid quantity.Please enter a valid number.")
                    print()
                else:
                    order[check] = qty
                    print(f'Quantity of {check} updated successfully.')
                    print()
                    break
            except ValueError:
                print("Invalid quantity.Please enter a valid number.")
                print()

def remove_item():
    if not order:
        print("Your order is empty.")
        print()
    else:
        while True:
            item_remove = input("\nEnter item to remove:").title()
            if item_remove not in order:
                print(f"{item_remove} not found in your order.")
                print()
            else:
                order.pop(item_remove)
                print(f"{item_remove} removed successfully.")
                print()
                break

def search_item():
    while True:
        item = input("\nEnter item to search:").title()
        if item in menu:
            print(f"\n{item} is available.")
            print(f"Price: ₹{menu[item]}")
            print()
            break
        else:
            print(f"{item} is not available.")
            print()

def generate_bill():
    if not order:
        print("Your order is empty.")
        print()
    else:
        total = 0
        print()
        print("=" * 62)
        print(f'{'RESTAURANT BILL':^55}')
        print("=" * 62)
        print(f'{"Item":<30}{"Qty":>8}{"Price":>10}{"Total":>12}')
        print('-' * 62)
        for item, quantity in order.items():
            price = menu[item]
            subtotal = price * quantity
            total += subtotal
            print(f'{item:<30}{quantity:>8}{("₹" + str(price)):>10}{("₹" + str(subtotal)):>12}')
        print("-" * 62)
        print(f'{"Grand Total"}{("₹" + str(total)):>49}')
        print()
        print("Bill generated successfully.")
        print("=" * 62)
        print()

def save_order():
    if not order:
        print("Your order is empty.")
        print()
    else:
        saved_orders.append(order.copy())
        print("Order saved successfully.")
        print()

def previous_orders():
    if not saved_orders:
        print("No saved orders found.")
        print()
    else:
        print('\n' + '=' * 65)
        print(f'{'PREVIOUS ORDERS':^65}')
        print("=" * 65)
        for i, old_order in enumerate(saved_orders, start=1):
            print(f"\nOrder {i}")
            print("-" * 65)
            print(f'{"Item":<30}{"Qty":>8}{"Price":>12}{"Total":>15}')
            print("-" * 65)
            total = 0
            for item, qty in old_order.items():
                price = menu[item]
                subtotal = price * qty
                total += subtotal
                print(f'{item:<30}{qty:>8}{("₹" + str(price)):>12}{("₹" + str(subtotal)):>15}')
            print("-" * 65)
            print(f'{"Grand Total":<50}{("₹" + str(total)):>15}')
        print("\nEnd of saved orders.")
        print("=" * 65)
        print()

while True:
    display_menu()
    try:
        choice = int(input("Enter your choice:"))
        if choice == 1:
          view_menu()

        elif choice == 2:
            place_order()

        elif choice == 3:
            view_current_order()

        elif choice == 4:
            update_quantity()

        elif choice == 5:
            remove_item()

        elif choice == 6:
            search_item()

        elif choice == 7:
            generate_bill()

        elif choice == 8:
            save_order()

        elif choice == 9:
            previous_orders()

        elif choice == 10:
            print("\nThank you for visiting the Restaurant.")
            print("Have a great day!")
            break
        else:
            print("\nInvalid choice.Please enter a number between 1 and 10.")
            print()
    except ValueError:
        print("\nPlease enter a valid number.")
        print()
