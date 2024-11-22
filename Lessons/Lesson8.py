'''
Lesson 8
Exceptions in Python
Objectives:
    - UNderstand what exceptions are and why they occur
    - Leanr about common types of Python Exceptions
    - Know how to handle exceptions using  'try', 'except', 'else', and 'finally' 
    - Practice reading and interperting exception messages
    - Wrtie code to handle exceptions effectively
'''

'''
8.1 What are Exceptions?
Def:
    Exceptions are errors that occur during the execution of a program, disrupting the normal flow of instructions

Key Idea:
    Exceptions are raised when Pyton encounters an error it cannont handle automatically.
'''
# Example 8.1
# A division by zero error
'''
x = 10 / 0

Output:
Traceback (most recent call last):
  File "main.py", line 2, in <module>
    print(10 / 0)
ZeroDivisionError: division by zero


Python has several built-in exceptions. Below are the most common ones:

Exception	Description	Example
ZeroDivisionError	Raised when division by zero occurs	10 / 0
ValueError	Raised when a function receives an argument of the right type but inappropriate value	int('abc')
TypeError	Raised when an operation is applied to an object of inappropriate type	5 + "hello"
IndexError	Raised when accessing a sequence with an invalid index	my_list[10]
KeyError	Raised when accessing a dictionary with a nonexistent key	my_dict['key']
AttributeError	Raised when an attribute reference is invalid	'abc'.length()
ImportError	Raised when an import statement fails	import non_existent_module
FileNotFoundError	Raised when a file operation fails due to the file not being found	open('missing_file.txt')
NameError	Raised when a variable is not defined	print(undefined_variable)
AssertionError	Raised when an assert statement fails	assert 2 + 2 == 5
'''


# Handling Exceptions
# Pyton Provides a way to handle exception using the try and except blocks
# basic structure
'''
try:
    # code that might raise an exception
    pass
except ExceptionType:
    # code to handle the exception
'''

# Example 8.1
try:
    print(10 / 0)
except ZeroDivisionError:
    print("You cannont divide by Zero!")

# Catching multiple Exceptions
try:
    value = int("hello")
except (ValueError, TypeError) as e:
    print(f"An error occurred: {e}")

'''
Write a program to divide two numbers. 
If the user enters a zero as the denominator, handle the ZeroDivisionError and print an appropriate message.
Sample:
Enter numerator: 10
Enter denominator: 0
Error: You cannot divide by zero!
'''

try:
    a = int(input("Enter numerator: "))
    b = int(input("Enter denomenator: "))
    print(a/b)
except ZeroDivisionError:
    print("You cannont divide by zero, loser!")
    