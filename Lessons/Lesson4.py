''' Lesson 4
 Data Structures in Python
 - Vectors
 - index and slice list
 - basic  list methods
 - iterate through list with loops
 - the 'in' ad 'not in' keywords
 - and list comprehensions
'''

# 4.1 Vectors (Lists)
# A list is mutable, ordered collection of items in Python. List can contain items of ANY
# data types and are defined using square brackets '[]'

# Example 4.1
fruits = ["apple", "Banana", "cherry"]

# We could operate on this list using the following basic methods
# Accesssing elements and re assigning

#Example 4.2 Re assign apple to orange
print(fruits)
fruits[0] = "orange"
print(fruits)

#Example 4.3
# add to this list using append
fruits.append("pear")
print(fruits)

#Example 4.4
# Chose an item to remove
fruits.remove("cherry")
print("Removed Cherry -- ", end="")
print(fruits)

# Example 4.5
# Pop method
lilfruit = fruits.pop()
print(f"Removed {lilfruit} from {fruits}")

yellowfruits = ["banana", "Lemon"]
redfruits = ["apples", "watermelon"]
allfruits = yellowfruits + redfruits
print(f"I added yellowfruits {yellowfruits} + redfruits {redfruits} = allfruits {allfruits}")

# Activity 1
# Create a list that contains 5 book names and print
# Then add 3 more books using methods and print
# then remove the 3rd book from the list and print
# THen pop the last book and print


# 4.2 Indexing and Slicing
'''
Indexing allows access to individual elements in a list
Slicing is used to access a range of elements within a list
'''

#Example 4.2
numbers = [1,2,3,4,5,6]
print(numbers[2]) # output 3
print(numbers[1:4]) # output [2,3,4] (slicing)
print(numbers[-1]) # output the last 

# Activity 2
scores = [45,67,89,23,56]
# Print the first two elements Output : [45, 67]
# print last three elements Output: [89, 23, 56]
# Slice from the first two elements and save in variable
# slice the last 3 elements and save in variables
# and combine both sub list in different order

# Activity 3
numbers = [2, 5, 8, 12, 16, 25, 30, 35, 42, 50]
'''
** hint ** list[start:end:step]

1. Extract every third element from the list.
2. Reverse the list using slicing.
3. Extract all elements from the list except the first two.
4. Create a new list with only the elements that are divisible by 5.
'''

# Activity 4
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
'''
1. Extract the first column of the matrix (i.e., [1, 4, 7]).
2. Extract the diagonal elements [1, 5, 9].
3. Reverse the second row of the matrix.
'''

#1
first_column = matrix[0:1][0:1]
print(first_column)