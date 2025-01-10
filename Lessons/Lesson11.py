'''
Lesson 11
Loops in Python are powerful tools for iterating over sequences, performing repeated opeatins, 
and managing complex data transformations
- understand and use for and while loops to be able to complete complex sequences
- Employ-build int python functions
- Use comprehension methods
- handle nested loops

'''

# For loop Review
numbers = [10,20,30]
for num in numbers:
    print(num)

# while loop Review
i = 0
while i < 5:
    print(i)
    i += 1

# Advanced concepts
# using enumare() function
# enumerate() allows you to loop over an iterable while having an automatic counter. This
# is especially useful if you need both the index and the value:

fruits = ["apple", "banana", "cherry"]
for index,fruit in enumerate(fruits):
    print(index,fruit)


# Zip Method
# zip() allows parallel iteration over multiple iterables
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92 ]

for name,score in zip(names,scores):
    print(name, "has a score of", score)

# print the name and the score of the person using a different method

# nested loops
# nested loops let you iterate over multiple dimensions

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()


# print 4, 7, 3
#change  6 to 12, and 8 to 16

print(matrix[1][0])
matrix[1][2] = 12
print(matrix)

'''
Example 2: Nested Loops with Early Exit
Task: We want to find if there is a specific number (e.g., 5) in a matrix. 
If found, print its position and stop searching immediately.

Step by Step:

Iterate through each row with for i, row in enumerate(matrix).
Iterate through each element with for j, val in enumerate(row).
If val matches the target, print position and break.
To stop the outer loop, use a flag or break out of it after the inner break.
'''
target = 5
for i, row in enumerate(matrix):
    for j, val in enumerate(row):
        if val == target:
            print(f"Found {target} at position ({i}, {j})")
            found = True
            break
    if found:
        break


# analyze the code
nums = [2, 4, 6, 8, 10]
result = 0
for i, num in enumerate(nums):
    if i % 2 == 0:
        result += num
    else:
        result -= num
print(result)
'''
i = 0, num = 2: i % 2 == 0 is True, so result = 0 + 2 = 2
i = 1, num = 4: i % 2 == 1 is True, so result = 2 - 4 = -2
i = 2, num = 6: i % 2 == 0 is True, so result = -2 + 6 = 4
i = 3, num = 8: i % 2 == 1 is True, so result = 4 - 8 = -4
i = 4, num = 10: i % 2 == 0 is True, so result = -4 + 10 = 6
'''

'''
Task: You have three lists: one of employee names, one of their positions, and one of their salaries.
 Print a formatted string for each employee like "John is a Manager earning 75000" using zip().
'''
names = ["John", "Lisa", "Mark"]
positions = ["Manager", "Developer", "Designer"]
salaries = [75000, 65000, 60000]
