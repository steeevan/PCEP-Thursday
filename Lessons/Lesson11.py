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


