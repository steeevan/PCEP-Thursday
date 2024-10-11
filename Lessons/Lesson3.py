''' Lesson 3 Control Flow and Loops in Python
        Objectives: 
        - Understand how conditional and loop structures work in Python
        - Learn to control the flow of a Python program using if-else, elif, while and for loops
        - Master the user of special loop control statements: break, continue, pass
        - APply these concepts in practical'''


#1.1 If-esle Statements
# The if statement is used to execute a block of code if a certain condition is met. If the condition
# is not met, the code under else is executed.

'''
if condition:
    # code to execute if condition is True
else:
    # code to executre if condition is false
'''


# Example 1
x = 5
if x > 10:
    print("x is greater than 10")
else:
    print("x is not greater than 10")

# Activity 1
# Write a program that checks if a number entered by the user is positive, negative, or zero.
num = int(input("Enter a number: "))
if num < 0:
    print("num is negative")
elif num > 0:
    print("num is positive")
else:
    print("It is zero")


# 2.1 Definition
# The elif statement allows checking multiple condition after the initial if. It stands for "else if"
# and us used when more than two conditions are present

#Example 2
'''
if condition1:
    # Code if condition1 is True
elif condition2:
    # Code if condition1 is False but condition2 is True
else:
    # Code if neither condition1 nor condition2 is True
'''

x = 7
if x > 10:
    print(" x is greater than 10")
elif x == 7:
    print("x is equal to 7")
else:
    print("x is less than 10")

#Activity 2
'''
Create a program that takes a grade as input and prints out the letter grade using the following criteria:

A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: Below 60
'''

grade = int(input("Enter your grade: "))
if grade > 90:
    print("A")
elif grade < 90 and grade >= 80:
    print("B")
elif grade < 80 and grade >= 70:
    print("C")
elif grade < 70 and grade >= 60:
    print("D")
else:
    print("F")

# Activity 3
#Write a Python program that takes three numbers as input
# and determines the largest of the three numbers. Use if-elif-else statements to print which number is the largest.
a = int(input("Enter first numer: "))
b = int(input("Enter second numer: "))
c = int(input("Enter third numer: "))
# Example Input:
# Enter three numbers: 10, 20, 5
# Output: 20 is the largest number.
if a > b and a > c:
    print("a is bigger")
elif b > a and b > c:
    print("b is bigger")
elif c > a and c > b:
    print("c is bigger")
else:
    print("There all the same")


# 3.1 Definitino
# A while loop repeatedly executes a block of code as long as the condition is true.
# 3.2 Syntax
'''
while condition:
# code to execute while the condition is True.
'''

# Example
count = 0
while count < 500:
    print("the count is:",count)
    count += 1

# Activity:
#Write a program that prompts the user for a password. The program should continue asking until the correct password is entered.
correct_password = "Magikid"
guess = input("Enter your password: ")
while correct_password != guess:
    guess = input("Enter your password(Attempt failed): ")

print("Great Job you did it!")


# 4 Definition
# A for loop iterates over a sequence and executes a block of code for each item in the sequence
'''
for variable in sequence:
# code to exectte for each element in the sequence
'''
for i in range(5):
    print(i)



    # 5.1 Break
    # break is used to exit a loop permenantly
    for i in range(10):
        if i == 5:
            break
        print(i)


#5.2 Continue
# continue is used to skip the curent iteration and move to the next iteration
for i in range(5):
    if i == 3:
        continue
    print(i)
