# Homework Assignment: Arithmetic, Comparison, Logical, and Assignment Operators

# This Python file contains exercises and tasks based on the lesson covered today.
# Follow the instructions for each part, and make sure to complete all the exercises.

# Part 1: Definitions
# Instructions: Write the definitions of the following concepts in your own words in the space below each comment.


# 1. Arithmetic Operators
# Definition: Arithmetic operators is basically math 
#It contain multiplication, division, addition, subtraction, modulo, exponent, and floor division


# 2. Comparison Operators
# Definition: The Comparision operator is comparing the statement to 
#output true or false


# 3. Logical Operators
# Definition: Using or, and, and not. or is if eaither one of them is true, it consider it as true
#and is if both are true it consider it as true
# not is the outputting the opposite of the boolean


# 4. Assignment Operators
# Definition: Assignment operators use arithmetic but with a extra = sign
# It straight assign the value to the variable


# Part 2: Coding Exercises
# Solve the following exercises by writing the correct code beneath each comment.

# Exercise 1: Arithmetic Operations
# Given two numbers, x and y, calculate the following:
x = 10
y = 4

# 1. Determine the sum of x and y and print it.

sum= x+y
print(sum)

# 2. Determine the difference between x and y and print it.

difference= x-y
print(difference)

# 3. Determine the product of x and y and print it.

product= x*y
print(product)

# 4. Determine the floor division result of y divided by x.

floor_division= x//y
print(floor_division)

# Exercise 2: Comparison Operations
# Given two numbers, a and b, use comparison operators to check the following:
a = 8
b = 15

# 1. Is a greater than b? Print the result (True or False).

greater= a>b
print(greater)

# 2. Is a equal to b? Print the result (True or False).

equal= a=b
print(equal)

# 3. Is b greater than or equal to a? Print the result (True or False).

b_greater= b>a
print(b_greater)


# Exercise 3: Logical Operations
# Given two conditions, is_raining and is_windy, determine the following using logical operators:
is_raining = True
is_windy = False

# 1. Should we stay inside if it is both raining and windy? (Use AND operator)

should= is_raining and is_windy
print(should)

# 2. Can we go for a walk if it is either raining or windy? (Use OR operator)

can= is_windy or is_raining
print(can)

# 3. Is it not raining? (Use NOT operator)

not_rain= not is_raining
print(not_rain)

# Exercise 4: Assignment Operators
# Given a variable `c`, use assignment operators to perform the following operations:
c = 5

# 1. Add 10 to `c` using an assignment operator and print the new value of `c`.

c+=10
print(c)

# 2. Subtract 3 from `c` using an assignment operator and print the new value of `c`.

c-=3
print(c)

# 3. Multiply `c` by 2 using an assignment operator and print the new value of `c`.

c*=2
print(c)

# 4. Divide `c` by 4 using an assignment operator and print the new value of `c`.

c/=4
print(c)

# Exercise 5: Create Your Own Function
# Instructions: Write a Python function called `fizz_buzz` that takes an integer `n` as input.
# - If `n` is divisible by both 3 and 5, print "FizzBuzz"
# - If `n` is divisible only by 3, print "Fizz"
# - If `n` is divisible only by 5, print "Buzz"
# - Otherwise, print the value of `n`.
def fizz_buzz(n):
    m= int(n)
    if m%3 == 0 and m%5 == 0:
        print("FizzBuzz")
    if m%3 == 0 and m%5 != 0:
        print("Fizz")
    if m%3 != 0 and m%5 == 0:
        print("Buzz")


# Test the function with different values of n

fizz_buzz(15)
fizz_buzz(5)
fizz_buzz(3)
