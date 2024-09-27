"""
Lesson 1: Assigning Data Types to Variables & Performing Data Operations
This lesson covers how to assign data types to variables and perform basic operations on them.
"""

# --- Part 1: Assign Data Types to Variables ---
# Variables are storage locations for data. Data types define the kind of data stored.
# Python automatically assigns a type to a variable based on the value assigned.

# Example of assigning data types:
name = "Alice"      # string type (str)
age = 25            # Integer type (int)
height = 5.8        # Float type (float)
is_student = True   # Boolean type (bool)
my_list = [10,20,30]# List type (list)
my_dict = {         # dictionary (dictionary)
    "A": 10,
    "B":20
}

my_tup = (10,20,30)# tuple type (tup)
my_sets = {10,20,30} #set type (set)


# You can check the type of variable using the 'type()' function
print("Data types of variables:")
print(type(name))    # Output: <class 'str'>
print(type(age))     # Output: <class 'int'>
print(type(height))  # Output: <class 'float'>
print(type(is_student))  # Output: <class 'bool'>
print(type(my_list))    
print(type(my_dict))
print(type(my_tup))
print(type(my_sets))

# --- Part 2: Data Type Operations ---
# You can perform operations based on the data type.
# Strings: concatenation
greeting = "Hello " + name + "!"
print(greeting)

# Integers and floats: arithmetic operations
total_age = age + 5
print("In 5 years, Alice will be", total_age)

# Booleans: logical operations
status = not is_student
print("Student status:", status)

# --- Part 3: Lists ---
# Lists are ordered mutable collections. You can store ANY data type in a list
# Example of creating a list
fruits = ["apple", "Banana","cherry"]

# list operations
fruits.append("orange") # add an element to the end
fruits[1] = "blueberry"

print("\nList Operations:")
print("Updated Fruits List:", fruits)

# Access list elements by index:
first_fruit = fruits[0]
print("First fruit:", first_fruit)

# Remove an element from the list:
fruits.remove("cherry")
print("After removing 'cherry':", fruits)
# --- Part 4: Tuples ---

# Tuples are ordered, imutable collections. Once a tuple is created, it cannot be modified
# Example of creating a tuple
coordinates = (10.0, 20.0)

# Accessing tuple elements
x,y = coordinates

print("\nTuple Operations:")
print(f"Coordinates: x = {x}, y = {y}")

# You can check for elements in a tuple:
print("Is 10.0 in coordinates?", 10.0 in coordinates)

# -- Part 5: Dictionary ---
# Dictionaries are collections of key-value pairs. They are unordered and mutable.
# Example of creting a dictionary:
person = {
    "name": "Alice",
    "age": 25,
    "height": 5.8
}

# Dictionary operations:
person["age"] = 26  # Modify the value associated with a key
person["city"] = "New York"  # Add a new key-value pair

print("\nDictionary Operations:")
print("Updated Person Dictionary:", person)

# Access a value by its key:
print("Person's name:", person["name"])

# Remove a key-value pair:
del person["height"]
print("After removing height:", person)


# -- Part 6: Sets --
# Sets are unordered collections with no duplicate elements. Sets are mutable
# Example of creatin a set
unique_numbers = {1,2,3,3,4}

# Set operations:
unique_numbers.add(5)  # Add an element to the set
unique_numbers.discard(2) # remove an eletment from the set

print("\nSet Operations:")
print("Updated Set:", unique_numbers)

# Set operations (union, intersection):
even_numbers = {2, 4, 6}
union_set = unique_numbers.union(even_numbers)  # Union of two sets
intersection_set = unique_numbers.intersection(even_numbers)  # Intersection of two sets


print("Union of sets:", union_set)
print("Intersection of sets:", intersection_set)


# Let's summarize what we've learned:
# 1. Lists: Ordered, mutable collections. Use for storing multiple items.
# 2. Tuples: Ordered, immutable collections. Use when you need a fixed collection of items.
# 3. Dictionaries: Key-value pairs, unordered, mutable. Use when you need to map keys to values.
# 4. Sets: Unordered collections with no duplicates, mutable. Use for unique items and set operations.