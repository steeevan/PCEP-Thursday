
1. **Imports and Constants:**
   - The `os` module is used to check if the inventory file exists.
   - The `json` module handles reading from and writing to the inventory file in JSON format.
   - The `sys` module allows the program to exit gracefully.
   - `INVENTORY_FILE` is a constant that holds the name of the inventory file.

2. **Function: `load_inventory`**
   - Checks if the `inventory.txt` file exists.
   - If not, it creates the file and initializes it with an empty list.
   - If the file exists, it attempts to load the JSON data. If the file is corrupted or contains invalid JSON, it initializes an empty inventory.

3. **Function: `save_inventory`**
   - Saves the current state of the inventory back to the `inventory.txt` file in a readable JSON format with indentation.

4. **Function: `add_item`**
   - Prompts the user to enter the item's name, quantity, and cost.
   - Validates the inputs to ensure quantity is a non-negative integer and cost is a non-negative number.
   - Checks for duplicate items by comparing item names (case-insensitive).
   - Appends the new item to the inventory and saves the updated inventory.

5. **Function: `remove_item`**
   - Prompts the user to enter the name of the item to remove.
   - Searches for the item in the inventory (case-insensitive).
   - Removes the item if found and saves the updated inventory.

6. **Function: `update_item`**
   - Prompts the user to enter the name of the item to update.
   - If the item exists, displays its current details.
   - Offers the user options to update quantity, cost, or both.
   - Validates the new inputs and updates the item accordingly.
   - Saves the updated inventory.

7. **Function: `view_inventory`**
   - Checks if the inventory is empty. If not, it displays all items in a neatly formatted table with columns for Item Name, Quantity, and Cost.

8. **Function: `display_menu`**
   - Displays the main menu options to the user.

9. **Function: `main`**
   - Loads the inventory at the start.
   - Enters an infinite loop where it displays the menu and prompts the user for their choice.
   - Calls the corresponding function based on the user's input.
   - Exits the program gracefully when the user chooses to exit.

10. **Entry Point:**
    - The `if __name__ == "__main__":` block ensures that the `main` function runs when the script is executed.

### Running the Application

1. **Prerequisites:**
   - Ensure you have Python 3 installed on your system.

2. **Setup:**
   - Save the Python code in a file named `inventory_management.py`.
   - Ensure that the script is in a directory where you have read and write permissions.

3. **Execution:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing `inventory_management.py`.
   - Run the script using the command:
     ```
     python inventory_management.py
     ```
4. **Usage:**
   - Upon running, the application will display a menu with options to add, remove, update, view items, or exit.
   - Follow the on-screen prompts to interact with the inventory.

### Sample Interaction

```
===== Inventory Management System =====
1. Add Item
2. Remove Item
3. Update Item
4. View All Items
5. Exit
Enter your choice (1-5): 1
Enter item name: Apples
Enter quantity: 50
Enter cost per item: 0.5
Item 'Apples' added successfully.

===== Inventory Management System =====
1. Add Item
2. Remove Item
3. Update Item
4. View All Items
5. Exit
Enter your choice (1-5): 4

Item Name           Quantity   Cost      
----------------------------------------
Apples              50         $0.50     
----------------------------------------

===== Inventory Management System =====
1. Add Item
2. Remove Item
3. Update Item
4. View All Items
5. Exit
Enter your choice (1-5): 5
Exiting the Inventory Management System. Goodbye!
```

### Conclusion

This Inventory Management System provides a foundational tool for managing inventory data using Python's core data structures and file handling capabilities. The modular design ensures that each functionality is encapsulated within its function, promoting code readability and maintainability. Further enhancements can include features like search functionality, data sorting, and a graphical user interface (GUI) for improved user experience.

Happy coding!