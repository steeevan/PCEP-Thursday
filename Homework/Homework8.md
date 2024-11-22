### **Python Exceptions Homework Assignment**

#### **Objective:**
This homework assignment will reinforce your understanding of Python exceptions, how to handle them, and how to write robust error-handling code.

---

### **Part 1: Conceptual Questions**

1. **Short Answer Questions:**
   - What is the purpose of the `try` and `except` blocks in Python?
   - Describe the difference between `else` and `finally` in exception handling.
   - List three common exceptions in Python and give an example of when each might occur.

2. **Traceback Analysis:**
   Examine the following traceback:
   ```
   Traceback (most recent call last):
     File "main.py", line 5, in <module>
       result = 10 / 0
   ZeroDivisionError: division by zero
   ```
   - What type of exception occurred?
   - Which line of code caused the exception?
   - How would you fix this error?

---

### **Part 2: Coding Problems**

#### **Problem 1: File Handling**
Write a program that:
1. Prompts the user for a filename.
2. Attempts to open the file for reading.
3. If the file does not exist, catch the `FileNotFoundError` and display an error message.
4. Ensure the program prints "Operation complete" at the end using a `finally` block.

---

#### **Problem 2: Custom Exception**
Create a custom exception class called `NegativeNumberError`. Write a program that:
1. Asks the user to input a number.
2. Raises a `NegativeNumberError` if the input is a negative number.
3. Catches the exception and displays a message like "Negative numbers are not allowed!"

---

#### **Problem 3: Calculator with Exception Handling**
Write a program to create a simple calculator that:
1. Prompts the user for two numbers and an operator (+, -, *, /).
2. Handles the following exceptions:
   - `ZeroDivisionError` if the user attempts to divide by zero.
   - `ValueError` if the user enters non-numeric input.
   - A generic exception for unsupported operators.
3. Ensures the program continues to run until the user chooses to quit.

---

### **Part 3: Challenges**

#### **Challenge 1: Logging Exceptions**
Write a program that:
1. Prompts the user to enter a number.
2. Attempts to calculate the square root of the number using `math.sqrt()`.
3. Handles:
   - `ValueError` if the user enters a negative number.
   - `TypeError` if the user enters non-numeric input.
4. Logs any exceptions into a file called `error_log.txt`.

---

#### **Challenge 2: Nested Try Blocks**
Write a program that:
1. Prompts the user for two numbers and attempts to divide them.
2. Uses a nested `try` block to handle:
   - `ZeroDivisionError` if the second number is zero.
   - `ValueError` if the input is not numeric.
3. Ensures the program prints "Nested try block executed successfully" if no exceptions occur.

---

### **Part 4: Advanced Application**

#### **Advanced Challenge: ATM Simulator**
Create a program to simulate an ATM. The program should:
1. Have a balance of $500 initialized.
2. Allow the user to:
   - Check balance
   - Withdraw money
   - Deposit money
3. Handle the following exceptions:
   - `ValueError` for invalid inputs.
   - Custom exception `InsufficientFundsError` if the user tries to withdraw more than the available balance.
4. Ensure the program runs until the user chooses to exit.

Example Output:
```
Welcome to the ATM!
1. Check Balance
2. Withdraw Money
3. Deposit Money
4. Exit
Choose an option: 2
Enter withdrawal amount: 600
Error: Insufficient funds!
```

---
