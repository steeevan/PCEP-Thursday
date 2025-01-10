import os
import json
import sys

# Define the inventory file path
INVENTORY_FILE = 'inventory.txt'

def load_inventory():
    '''
    Load inventory from the INVETORY_FILE
    if the file does not exist, create it and return an empty list
    '''
    if not os.path.exists(INVENTORY_FILE):
        with open(INVENTORY_FILE,'w') as f:
            json.dump([], f)
        return []
    with open(INVENTORY_FILE, 'r') as f:
        try:
            inventory = json.load(f)
            if not isinstance(inventory,list):
                print("Corrupted inventory file. Initializing empty inventory")
                return []
            return inventory
        except json.JSONDecodeError:
            print("Error reading inventory file. Initializing empty inventory")
            return []
        

def save_inventory(inventory):
    '''
    save the inventory list to the inventory file in JSON format
    '''
    with open(INVENTORY_FILE, 'w') as f:
        json.dump(inventory,f, indent=4)


def add_item(inventory):
    '''
    add a new item to the inventoy
    '''
    name = input("Enter item name: ").strip()
    if any(item['name'].lower() == name.lower() for item in inventory):
        print(f"Item '{name}' already exists in the inventory")
        return
    try:
        quantity = int(input("Enter quantity: "))
        if quantity < 0:
            raise ValueError
    except ValueError:
        print("Invalid quantity. Please enter a non-negative integer.")
        return
    try:
        cost = float(input("Enter cost per item: "))
        if cost < 0:
            raise ValueError
    except ValueError:
        print("Invalid Cost. PLease enter a non-negative number.")
        return
    item = {
        'name': name,
        'quantity': quantity,
        'cost': cost
    }
    inventory.append(item)
    save_inventory(inventory)
    print(f"Item '{name}' added successfully")


def remove_item(inventory):
    '''
    Remove an existing item from the inventory
    '''
    name = input("Enter the name of the item to remove: ").strip()
    for item in inventory:
        if item['name'].lower() == name.lower():
            inventory.remove(item)
            save_inventory(inventory)
            print(f"Item '{name}' removed successfully")
            return
    print(f"Item '{name}' not found in the inventory")


def update_item(inventory):
    '''
    update the quantity or cost of an existing item
    '''
    name = input("Enter the name of the item to update: ").strip()
    for item in inventory:
        if item['name'].lower() == name.lower():
            print(f"Current details of '{name}': Quantity = {item['quantity']}, Cost = {item['cost']}")
            print("What would you like to update?")
            print("1. Quantity")
            print("2. Cost")
            print("3. Both")
            choice = input("Enter your choice(1/2/3): ").strip()
            if choice == '1':
                try:
                    quantity = int(input("Enter new quantity: "))
                    if quantity < 0:
                        raise ValueError
                    item['quantity'] = quantity
                except ValueError:
                    print("Invalid quantity. Updated aborted.")
                    return
            elif choice == '2':
                try:
                    cost = float(input("Enter new cost: "))
                    if cost < 0:
                        raise ValueError
                    item['cost'] = cost
                except ValueError:
                    print("Invalid cost. Update aborted.")
                    return
                
            elif choice == '3':
                try:
                    quantity = int(input("Enter new quantity: "))
                    if quantity < 0:
                        raise ValueError
                    cost = float(input("Enter new cost: "))
                    if cost < 0:
                        raise ValueError
                    item['quantity'] = quantity
                    item['cost'] = cost
                except ValueError:
                    print("Invalid input. Update aborted.")
                    return
            else:
                print("Invalid choice. Updated aborted")
                return
            save_inventory(inventory)
            print(f"Item '{name}' updated successfully.")
            return
    print(f"Item '{name}' not found in the inventory")


def display_menu():
    '''
    Display the main menu options
    '''    
    print("\n===== Inventory Management System =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Update Item")
    print("4. View All Items")
    print("5. Exit")

def main():
    '''
    The main functino to run the inventory management system
    '''
    inventory = load_inventory()
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()
        if choice == '1':
            add_item(inventory)
        elif choice == '2':
            remove_item(inventory)
        elif choice == '3':
            update_item(inventory)
        elif choice == '4':
            print(inventory)
        elif choice == '5':
            print("Exiting The inventory Management system. Goodbye!")
            sys.exit()
        else:
            print("Invalid Choice. Please select a valid option (1-5).")
        


            
        



main()



