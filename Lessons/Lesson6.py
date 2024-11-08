'''
Python PCEP Lesson: Functions
1. Lesson Objectives
Understand what functions are and their importance in code decomposition.
Learn how to organize the interaction between functions and their environment.
Explore different types of functions: with/without parameters, returning/non-returning values.
Gain hands-on experience through examples and exercises.

'''


# 6.1 Functios
# A function is a resusable block of code that performs a specific task

def function_name(parameters):
    #code block
    return value
'''
Parameters: Variables listed in the function definition to pass data into the function
Arguments: Actual values provided to the function when calling it
Return Values: the output produced bu the function, returned using the 'return' statement
Scope: Defines where a variable/function can be accessed (local or global)
'''

'''
6.2
Types of Functions
'''

# 6.2.1 Functions without Parameters
def greet():
    print("Hello World")

greet()     # invocate our function

# 6.2.2 Functions with Paramters
# Functions can accept input values to modify their behaviour
def greet_person(name):
    print(f"hello {name}")

greet_person("Mr E")    #invocates the function with a paremeter
# Here the 'name' is a paramenter which is a local variable for the function
# 'Mr E' is the Argument given to the function greet_person

#6.2.3 Function with Default Parameters
# Functions where parameters are given default values in the case they are not given
# any arguments when invocated

def greet_person(name="Guest"):
    print(f"Hello {name}")

greet_person()
greet_person("Mr Estevan")

# 6.2.4 Functions with Returning Values
# Functions that compute and return a result
def add(x,y):
    return x + y

result = add(3,5)   # result = 8
print(result)


# 6.2.5 Void functions (Non-returning Functions)
# Functions that do not return a value, performs only actions

def display_message():
    print("This is a void function")

display_message()

# 6.3 Organizing Functions
# Decompose Code
# Break code into smaller, resusable pieces

def calculate_area_rectangle(length,width):
    return length * width

def display_area(length,width):
    area = calculate_area_rectangle(length,width)
    print(f"The area is {area} square units")

display_area(5,10)

#6.3.2 Function Interaction
# Functions can call each ohter and share results
def get_input():
    return int(input("Enter a number: "))

def square_number(num):
    return num ** 2

def main():
    number = get_input()
    result = square_number(number)
    print(f"The square of {number} is {result}.")

main()

# 6.4 Advanced Functions
# Recursive Functions
# Functions that call themselves
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# 6.4.2 Lambda Functions
# Anonymous functions created using the lambda keyword

square = lambda x: x**2
print(square(4))


#6.4.3 Functions with variable number of Arguments
# Using the *args for positional arguments and **kwargs for keyword arguments
def flexible_function(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

flexible_function(1,2,3,name="Alice",age=25)

'''
1. Basic Function: Write a function multiply(a, b) that returns the product of two numbers.Assign
it to variable called "Product" and print it out

2. Default Parameters: Create a function introduce(name, age=18) that prints a default age if 
not provided.
Use examples to test

3. Interaction Between Functions: Create a program with get_data(), 
process_data(), and display_result() functions.
'''
#1
def multiply(a,b):
    return a * b
Product = multiply(5,10)

#2
def introduce(name,age=18):
    print(f"{name} is {age} years old")
introduce("Mr E")

#3
def get_data():
    return int(input("Enter a number:"))
def process_data():
    x = get_data()
    return x + 5
def display_data():
    y =process_data()
    print(y)


display_data()
