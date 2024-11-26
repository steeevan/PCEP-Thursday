# Part 1. Conceptual questions
# 1. Short aswer questions
#   -'Try' attempts the code given and 'except' handles exceptions with the code given
#   -'Else' runs if there is no problem with the code given to 'try' and 'finally' will always run
#   -3 Common exceptions: ValueError, TypeError, SyntaxError

# 2. Traceback analysis
#   -ZeroDivisionError
#   -result=10/0
#   -I can fix this error by not trying to divide by zero (basically, just have IQ and you'll be fine)

# Part 2. Coding problems
# Problem 1. File handling
# I used AI by the way because I wasn't able to solve this by myself
try:
    filename=input("Enter the filename: ")

    with open(filename, 'r') as file:
        print("File contents:")
        print(file.read())

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")

finally:
    print("Operation complete")

# Problem 2: Custom exception
# NegativeNumberError was done by AI. All other parts done by me.
class NegativeNumberError(Exception):
    '''Exeption raised for negative number input.'''
    pass

def moneyconverter():
    try:
        number1=float(input('Enter a positive number: '))

    except (NegativeNumberError, TypeError) as e:
        print('I told you specifically to put in a POSITIVE number, are you smart or somthing?')
        print('OR maybe you decided that a number was equal to a string, so you entered that instead.')
        print()
        print(f'This was your error: {e}')
    
    else:
        print('Converting number to YesBux')
        print('...')
        print('......')
        print('.........')
        print('CONVERSION_101...YESx21...(*^*(&()))')
        print()
    
    finally:
        if Exception:
            print('Failed to complete operation. Try again? ')
            print('[yes]')
            print('[no]')
            ask=input('')

            if ask=='yes':
                moneyconverter()
            
            else:
                print()
                print('Shutting Down.')
        else:
            print('Successfully completed operation.')
            moneyconverter()



moneyconverter()

# Problem 3: Calculator with Exeption handling
def calculator():
    number1=int(input('number 1: '))
    operator=str(input('operator (*, /, +, -): '))
    number2=int(input('number 2: '))
    try:
        if operator=='*':
            print ('answer:', number1*number2)
        elif operator=="/":
            print ('answer:', number1/number2)
        elif operator=="+":
            print ('answer:',number1+number2)
        elif operator=="-":
            print ('answer:', number1-number2)
        else:
            print ("That's not a valid operator.")

    except ZeroDivisionError as e1:
        print()
        print("You can't divide by zero!")
        print(f'Error: {e1}')

    except ValueError as e2:
        print()
        print(f"System cannot process non-numerical inputs. Error: {e2}")

    finally:
        if Exception:
            print('Try again? ')
            print('[yes]')
            print('[no]')
            ask=input('')

            if ask=='yes':
                calculator()
            
            else:
                print('Shutting down.')
        
        else:
            print()
            calculator()

calculator()

# Part 3: Challenges
# Challenge 1: Logging exceptions
# Ok so I have absolutely no idea how to log errors into another txt file so yeah (AI)
import math
import logging

# Set up logging configuration
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    try:
        user_input = input("Please enter a number: ")
        
        number = float(user_input)

        if number < 0:
            raise ValueError("Cannot compute the square root of a negative number.")
        result = math.sqrt(number)
        print(f"The square root of {number} is {result}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
        logging.error(f"ValueError: {ve}")
    
    except TypeError as te:
        print(f"Error: {te}")
        logging.error(f"TypeError: {te}")
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()

# Challenge 2: Nested try blocks
def nested_tryblocks():
    a=int(input('Enter first number: '))
    b=int(input('Enter second number: '))
    try:
        print(a/b)
    
    except ZeroDivisionError as e:
        print(f'Error: {e}')
    
    except ValueError as e2:
        print(f'Error: {e2}')
    
    else: 
        print('Nested try block executed successfully')
    
    finally:
        print('Finish')
    
nested_tryblocks()

# Part 4: Advanced Application
# Adcanced challenge: ATM simulator
class InsufficientFundsError(Exception):
    '''Exception raised for withdrawing more than you have.'''
    print('Insufficient Funds!')
    pass

def ATM():
    balance=500
    print()
    print('Welcome to the ATM!')
    print('1. Check Balance')
    print('2. Withdraw Money')
    print('3. Deposit Money')
    print('4. Exit')
    ask3=int(input('Choose an option: '))

    try:
        if ask3==1:
            print(f'Balance: {balance}')
            ask3
        
        elif ask3==2:
            wd_amount=int(input('Enter withdrawal amount: '))
            balance-=wd_amount
            ask3
        
        elif ask3==3:
            dp_amount=int(input('Enter deposit amount: '))
            balance+=dp_amount
            ask3
        
        elif ask3==4:
            print('Exiting the ATM. Have a good rest of your day!')
        
        else:
            pass
    
    except ValueError as e:
        print(f'Error; {e}')
    
    except InsufficientFundsError as e2:
        print(f'Error: {e2}')

    else:
        a1=input('Continue?'
                 '[yes]'
                 '[no]').lower()
        
        if a1=='yes':
            ATM()
        else:
            print('Exiting the ATM. Have a good rest of your day!')

            
            
