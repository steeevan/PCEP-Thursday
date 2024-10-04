# --- LESSON 1 HOMEWORK ---

# Part 1: Assign Data Types
# TODO: Assign appropriate data types to the following variables:
# - city (string)
# - temperature (float)
# - population (integer)
# - is_raining (boolean)

city = "New York"
temperature = 20.5
population = 30000000
is_raining = False  

# TODO: Print the type of each variable
# Example: print(type(city))

print(type(city))
print(type(temperature))
print(type(population))
print(type(is_raining))

# Part 2: Type Conversion & Operations
# TODO: Write a Python script that:

# 1. Takes user input for a product's price (float) and quantity (int).
# 2. Calculates the total cost as price * quantity.
# 3. Convert the total cost to an integer and print both float and integer values.

# TODO: Add code here to prompt for price and quantity inputs

product= float(input("What the price of the products"))
product2= int(input("what the quantity of the products"))
cost= product*product2

# TODO: Calculate total cost
total_cost = cost

# TODO: Print total cost as float and integer

print("Total cost (float):", total_cost)
print("Total cost (int):", int(total_cost))

# BONUS:
# TODO: Prompt for the user's name and print a message
# Example: print(f"Thank you, {name}, for your purchase of {quantity} items.")

name= str(input("What your name."))
print(f"Thank you, {name}, for purchase of {product2} items.")
"""
Homework for Lesson 1 (Extended): Lists, Tuples, Dictionaries, and Sets
Please complete the sections marked as "TODO".
"""

# Part 1: Lists
# TODO: Create a list of your favorite animals. Add at least 5 animals to the list.
# Perform the following operations:
# 1. Add a new animal to the list.
# 2. Modify the second animal in the list.
# 3. Remove the last animal from the list.
# 4. Print the final list.

animals = ["dog","cat","bird","hamster","bunny"]  # TODO: Add your favorite animals here
print("\n")
print (animals)
# TODO: Add code to perform the operations on the animals list

animals[1]="snake"
animals.remove("bird")
animals.append("fish")

print(animals)
# Part 2: Tuples
# TODO: Create a tuple representing the coordinates of a point in 3D space (x, y, z).
# Print the values of x, y, and z.

coordinates = (100,100,100)  # TODO: Create a tuple with 3 values

# TODO: Unpack the tuple and print each value

x,y,z=coordinates
print(x,y,z)

# Part 3: Dictionaries
# TODO: Create a dictionary to store information about a book.
# The dictionary should have the keys: "title", "author", "year_published".
# Perform the following operations:
# 1. Add a new key "genre".
# 2. Modify the "year_published" value.
# 3. Remove the "author" key.
# 4. Print the final dictionary.

book = {"title":"wow",
        "author":"Michel Jackson",
        "year published": 1990
        } 
print(book)

# TODO: Add code to perform the operations on the dictionary

book["genre"]= "informational"
book["year published"]= 1999
del book["author"]
print(book)

# Part 4: Sets
# TODO: Create a set of unique numbers. Add at least 5 numbers.
# Perform the following operations:
# 1. Add a new number to the set.
# 2. Remove a number from the set.
# 3. Perform a union with another set {10, 20, 30}.
# 4. Perform an intersection with another set {1, 2, 3}.
# 5. Print the final set.

numbers = set(10,20,30,40,50) 

# TODO: Add code to perform the operations on the set
numbers.add(60)
numbers.remove(10)

set2= set(10,70)
numbers.union(set2)

numbers.intersection(set2)

print(numbers)