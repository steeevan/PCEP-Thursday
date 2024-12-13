'''
Lesson 9
Functions
    - Understand what a function is and its role in programming
    - learn how to defin and invoke functinos in python
    - debug commmon function-related issues
    - Explore different use cases for functions

'''

'''
Function - A block of organized, resusable code that performs a single action. Functinos help break donw complex 
            problems into smaller, manageble pieces

'''

def function_name(parameters):
    """docstring (optional)"""
    # code block 
    return value

# We use the keywork 'def' to initizialize the function
# Invocation is the process of calling or executing a function to perform its task

# Create a greeting functino
# write a functino that takes a users name and age as arguments and prints a personalize message

# Lets look into exercise folder 
# Exercise Lesson 9E

# We will use list comprehension
def categorize_numbers(numbers):
    even = [num for num in numbers if num % 2 == 0]
    odd = [num for num in numbers if num % 2 != 0]
    return even, odd

numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
even,odd = categorize_numbers(numbers)
print("Even: ", even)
print("Odd: ", odd)


def word_frequency(text):
    words = text.split()
    return {word: words.count(word) for word in set(words)}

text = "Hello Hello  william william william"
print(word_frequency(text))


def factorial(x):
    c = 1
    for i in range(1,x+1):
        c *= i
    return c


def factorial_sum(n):
    sum = 0
    for i in range(1,n+1):
        sum += factorial(i)
    return sum

print(factorial_sum(4))