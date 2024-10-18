# excercise 1
num1=int(input('Enter first number: '))
num2=int(input('Enter second number: '))
num3=int(input('Enter third number: '))
if num1>num2 and num1>num3:
    print(f'{num1} is the greatest number')
elif num2>num1 and num2>num3:
    print(f'{num2} is the greatest number')
elif num3>num1 and num3>num2:
    print(f'{num3} is the greatest number')
else:
    print('All numbers are identical')

# exercise 2 

day=int(input('Enter a number 1-7: '))
week_days=['monday', 'tuesday', 'wednesday','thursday','friday','saturday','sunday']


if 1<=day and day<=7:
    print(f'Day of the week: {week_days[day-1]}')
else:
    print("Either that's not between 1-7 or you didn't input a number")

# excercise 3
# I don't know how to do this
'''
ask=input('Enter the year: ')
if ask%4==0 or ask%100==0 and ask%400==0:
    print(f'{ask} is a leap year. Hooray!')
else:
    print(f'{ask} is not a leap year. Wompity womp womp')
'''
# excercise 4

number1=int(input("number 1: "))
operator=str(input("operator (*, /, +, -):"))
number2=int(input("number 2:"))

if operator=="*":
    print ("answer:", number1*number2)
elif operator=="/":
    print ("answer:", number1/number2)
elif operator=="+":
    print ("answer:",number1+number2)
elif operator=="-":
    print ("answer:", number1-number2)
else:
    print ("Does not compute")

# excercise 5

age=int(input('How old are you? '))
if age>=18:
    print('you are eligible to vote')
else:
    print(f'you have {18-age} years until you can vote')

