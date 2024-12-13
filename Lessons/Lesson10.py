'''
Lesson 10 Advanced Error Handling 
INstead of having your program stop abrublyt you can gracefully andle the situdation. inform 
the user and reover to continue execution
- When dealing wit user input, network request, file operations, or device intreactions, exceptions are likely. Handling these exceptions prevents
  confusing error messages form reaching end users
- By anticipating possible points of failure and handling them, you write more
  reliale code that can run in production
'''
# basic Syntax for try and except
'''
try:
    # code that moght cause an error
    pass
except SomeException:
# code that runs if some exception is raised in the try block

try: you place the code that might fail or raise and exception inside the try block
except: You specify hich exceptions you want to catch. If tht specific exception
        is raised the code in except runs
if no exception occurs, the excpet block is skipped.
if an exception occurs that is not caugt by the provided except clauses, the exception propagets updates
potentially ending the program if not handled elsewhere

'''

# Example 1 Divind by zero
try:
    a = int(input("Enter a numerator: "))
    b = int(input("Enter a denomenator: "))
    result = a / b
    print(f"{a} / {b} = {result}")
except ZeroDivisionError:
    print("You loser, you cannot divide by zero!")


# Example 2 Handling INvalid User Input
user_input = "abc"
try:
    number = int(user_input)  # ValueError if input is not a number
    print("Converted number:", number)
except ValueError:
    print("Invalid input! Please enter a number.")


#Example 3 Catching multiple exception types

my_list = [1, 2, 3]
index = 5

try:
    print("Item:", my_list[index])
except IndexError:
    print("The index is out of range!")
except TypeError:
    print("Invalid type used for indexing!")


# Sometimes you may wnt to catch any type of exception, regardless of what it is:
try:
    x = int("abc")
except Exception as e:
    print("An error occured",e)

# Using the else clause
# an else clause on a try-except block runs only if no eception was raised in the try block:
try:
    number = int("123")  # No error
except ValueError:
    print("This will not run since there's no error.")
else:
    print("Successfully converted number:", number)


# using the finally cluase
# a finaly block always runs, regardless of wheter an exception happend. This is useful
# for cleanup operations, like cloisng a file, or releasing a resourse

file_name = "nonexistent_file.txt"
try:
    file = open(file_name, "r")
    content = file.read()
except FileNotFoundError:
    print("File not found:", file_name)
else:
    print("File content:", content)
finally:
    print("Finally block runs no matter what!")


# handle many exceptions in a singe except block
try:
    # Raise a TypeError for demonstration
    result = "string" + 5
except (TypeError, ValueError) as e:
    print("An error occurred:", e)


# Creating custom exception classes
class MyCustomError(Exception):
    pass

try:
    raise MyCustomError("Something went wrong in my custom logic!")
except MyCustomError as e:
    print("Custom error caught:", e)

