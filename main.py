import datetime as dt  # To provide date and time on the bill


# Items are stored in a Dictonary where the key is the item name and the value is the cost of the item.
items = {"test": 20}

# main system
print("Welcome to the billing system version 1.0.0")
x = str(dt.datetime.now())
print(x[:19])
_main = 1
while _main != 0:
    # Take input for basic commands
    command = input("$ What do you want to use? (type help or manual for more info): ")
    if command == "help" or command == "manual" or command == "?":
        # help command
        print("#----------------------------------------------------------------------------#")
        print("                       Billing software Guide")
        print("""The system supports adding items and making bills printing bills keeping stock of items\n
                 The following are the list of commands the can be used\n 
                 (the commands in the bracket are aliases of the original command)
                 bill (bi/bil)- To start the billing process. \n
                 exit (quit) - Exit the system
                 inventory (inv) - To open stock manager\n
                    Sub commands in inventory 
                        add - add item
                        remove(rem)- remove item
                        modify(mod)-change the value of an item
                        """)
    elif command == "bill":
        # billing command
        # Creates billing instance and starts the bill process
        customer_name = input("$ Enter customer name: ")  # Entering customer name
        j = 0
        item_list = {}
        total = 0
        while j != 1:
            # Main billing loop
            product = input("$ Add a product. (type f to finish): ")
            if product in items.keys():
                cost = items.get(product)
                item_list[product] = cost
                print(f"Added {product} to the bill for {cost}")
                total += cost

            elif product == "f":
                # Checking main loop ending and printing the bill
                print(f"Printing the bill for {len(item_list)} items")
                print("#------------------------------------------------------#")
                print("Product               \n")
                for m in item_list:
                    print(f"{m} ")
                print(f"Subtotal: {total}")
                print("Thank you for shopping vist again")
                print("#------------------------------------------------------#")
                j += 1

            elif product not in items:
                # Checking for errors
                print(f"The item {product} is not in the inventory, please check the spelling")
                continue

    elif command == "inv":
        # Main system for inventory
        print("#------------------------------------------------------#")
        print("Welcome to inventory type help for more info")
        h = 0
        # Input commands for inventory
        while h != 1:
            inv_command = input("$ Use inventory commands (type e to exit): ")
            if inv_command == "check":
                # Check commands checks for items in inventory
                for f, d in items.items():
                    print(f"{f}        {d}")
                continue

            elif inv_command == "add":
                # Add command adds an item to the inventory
                new_item = input("Add a new item to inventory (add a name and press enter): ")
                new_item_cost = input("Add a new item cost to inventory (add the cost and press enter): ")
                items[new_item] = new_item_cost
                print(f"Added {new_item} for {new_item_cost}")
                continue

            elif inv_command == "remove":
                # Remove command removes an item from the inventory
                rem_item = input("Remove an item from inventory: ")
                items.pop(rem_item)
                continue

            elif inv_command == "modify":
                # Modify command modifies an item
                change_item = input("Name the item to be changed: ")
                changed_item = input("Name the new item name: ")
                change_item_cost = int(input("Change an item: "))

                if change_item not in items:
                    # Checking if te item exists
                    print("The item is not in the inventory, use add command to add the missing item")

                elif change_item in items:
                    # Making the modifications
                    items.pop(change_item)
                    items[change_item] = change_item_cost
                    print(f"Added {changed_item} for {change_item_cost}")
                    continue

            elif inv_command == "order":
                # Order command orders an item
                g = 0
                print("Add the items to this list that are to be ordered to add to the inventory type b to break")
                items_to_be_orderd = []

                while g != 1:
                    # Create a new list for order
                    item_for_order = input("Add item")
                    if item_for_order == "b":
                        g += 1
                    else:
                        items_to_be_orderd.append(item_for_order)
                print("The following items are to be ordered")
                for r in items_to_be_orderd:
                    # Printing the order
                    print(r, " ", end=" ")
                    print()

            elif inv_command == "exit":
                # Exit command exits the inventory
                print("Exiting inventory")
                h += 1
    elif command == "exit":
        # Exit command exits the Main system
        print("Exiting the system............................")
        break
