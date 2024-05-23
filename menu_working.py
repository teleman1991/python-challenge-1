# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
                    
            # 2. Ask customer to input menu item number
            menu_item_number = input(f'Which item in the {menu_category_name} would you like?' )

            # 3. Check if the customer typed a number
            if menu_item_number.isdigit():
                # Convert the menu selection to an integer
                menu_item_number = int(menu_item_number)
            

                # 4. Check if the menu selection is in the menu items
            if menu_item_number in menu_items:
                    # Store the item name as a variable
                selected_item = menu_items[menu_item_number]
                print(f"You have selected {selected_item['Item name']} for ${selected_item['Price']}.")
                    # Ask the customer for the quantity of the menu item
                quantity = input("How many would you like to order? ")

                    # Check if the quantity is a number, default to 1 if not
                if not quantity.isdigit():
                    quantity = 1
                else:
                        quantity = int(quantity)
                    # Add the item name, price, and quantity to the order list
                order_list.append({
                     "Item name": selected_item['Item name'],
                     "Price": selected_item['Price'],
                     "Quantity": quantity
                })
                print(f"Added {quantity} x {selected_item['Item name']} to your order.")
                another_order = input("Would you like to order something else? (yes/no): ").strip().lower()
                if another_order != 'yes':
                    place_order = False
                    print("\nYour final order is:")
                    total_cost = 0
                    for item in order_list:
                        item_cost = item['Price'] * item['Quantity']
                        total_cost += item_cost
                        print(f"{item['Quantity']} x {item['Item name']} @ ${item['Price']:.2f} each = ${item_cost:.2f}")
                    print(f"Total cost: ${total_cost:.2f}")
                    print("Thank you for your order!")
                    print("Please come back and see us!!!")
            else:
                print("Invalid menu item number.")
        else:
            print("Invalid input, please enter a number.")
    else:
        print("Invalid menu number.")