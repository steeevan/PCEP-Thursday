'''
Lesson 15
Determine the ouput of Functions

Students will learn how to eread and analyze functions to determine their outputs

'''

# Review
# A function is a block of resusable code
# Example 1
def greet():
    print("Hello, world!")

greet()

# Question: What is the output of this function?

# Example 2
def add_five(x):
    return x + 5

print(add_five(3))

# Question: What is the output?

# Example 3
def subtract(a, b):
    return a - b

print(subtract(10, 3))

# Determine the output


# Example 4
def power(base, exponent=2):
    return base ** exponent

print(power(4))  
print(power(3, 3))


# determine the output

# Example 5
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_list([1, 2, 3, 4, 5]))

#Determine the output
def multiply_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

print(multiply_list([2, 3, 4]))

# Deterine the output

# Example 6
def outer_function(x):
    def inner_function(y):
        return y * 2
    return inner_function(x) + 3

print(outer_function(4))


# Determine the output
def mystery_function(x, y=3):
    return x * y + 2

print(mystery_function(5))
print(mystery_function(2, 4))


def count_down(n):
    for i in range(n, 0, 1):
        print(i)
    print("Blast off!")

count_down(3)

#determine he output
#1
def mystery(x):
    return x + 2

print(mystery(5) * 3)

#2
def double(x):
    return x * 2

print(double(4) + double(2))

#3
#debug battler
def add_numbers(a, b):
print(a + b)

# 4 debug
def square(n):
    return n ** 2
print(square())



