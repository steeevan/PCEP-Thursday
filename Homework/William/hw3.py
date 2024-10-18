# Homework Assignment: Control Flow and Loops - Questions Only

# Instructions:
# Complete the following exercises using if-else, elif statements, loops, and control flow in Python.

# Exercise 1: Number Comparison
# Write a Python program that takes three numbers as input and determines the largest of the three numbers.
# Example:
# Input: Enter three numbers: 10, 20, 5
# Output: 20 is the largest number.
num1= int(input("first number"))
num2= int(input("second number"))
num3= int(input("third number"))
if num1 > num2 and num1> num3:
    print("number 1 is the largest")
elif num2>num1 and num2> num3 :
    print("Nunber two is the largest")
else:
    print ("number 3 is the largest")

# Exercise 2: Day of the Week
# Write a program that asks the user to enter a number (1-7) and prints the corresponding day of the week.
# Example:
# Input: Enter a number between 1 and 7: 3
# Output: Wednesday

day= int(input("Pick a number between 1:7"))
if day==1:
    print("monday")
elif day==2:
    print("tuesday")
elif day == 3:
    print("wedesday")
elif day==4:
    print("thursday")
elif day==5:
    print("friday")
elif day==6:
    print("saturday")
elif day==7:
    print("sunday")
else:
    print("not between 1:7")

# Exercise 3: Leap Year Checker
# Write a program that asks the user for a year and checks whether it is a leap year.
# Conditions for a leap year:
# - Divisible by 4.
# - If divisible by 100, it should also be divisible by 400.
# Example:
# Input: Enter a year: 2000
# Output: 2000 is a leap year.

year= int(input("what year is it"))
if year %4==0:
    if year%100==0:
        if year%400==0:
            print("It a leap year")

# Exercise 4: Simple Calculator
# Create a program that performs basic arithmetic operations.
# Ask the user to input two numbers and an operator (+, -, *, /).
# Use if-elif-else to perform the chosen operation and print the result.
# Example:
# Input: Enter first number: 12
# Input: Enter operator (+, -, *, /): *
# Input: Enter second number: 4
# Output: 12 * 4 = 48

a= int(input("first number"))
b= int(input("second number"))
c= str(input("pick a operation (*,/,+,-)"))
def calculate(num1,num2,oper):
    if oper=="*":
        return(num1*num2)
    elif oper == "/":
        return(num1/num2)
    elif oper =="+":
        return(num1+num2)
    elif oper=="-":
        return(num1-num2)
print(calculate(a,b,c))

# Exercise 5: Voting Eligibility
# Write a program that asks the user for their age and checks whether they are eligible to vote.
# If they are under 18, print how many years are left until they can vote.
# Example:
# Input: Enter your age: 16
# Output: You can vote in 2 years.
age = int(input("How old are you"))
if age >=18:
    print("you can vote")
else:
    age2=18-age
    print(f"You can't vote until {age2} more years")
