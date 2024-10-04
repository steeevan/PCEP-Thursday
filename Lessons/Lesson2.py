# 1. Arithmetic Operations
# Arithmetic operations are used to perform basic mathematical calculations

# lets make two variabls
a = 10          # INTEGER TYPES
b = 3           # INTEGER TYPES

# Performing arithmetic operations
sum_result = a + b  # Addition: 10 + 3 = 13
difference = a - b  # Subtraction: 10 - 3 = 7
product = a * b  # Multiplication: 10 * 3 = 30
quotient = a / b  # Division: 10 / 3 = 3.333...
floor_division = a // b  # Floor Division: 10 // 3 = 3 (quotient without remainder)
remainder = a % b  # Modulus: 10 % 3 = 1 (remainder after division)
power = a ** b  # Exponentiation: 10 ** 3 = 1000 (10 raised to the power of 3)

# Print the results
print("Arithmetic Operations:")
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")
print(f"Floor Division: {floor_division}")
print(f"Remainder: {remainder}")
print(f"Power: {power}")
print()  # Blank line for readability

# Arithmetic CHallenge
# Given
c = 5
# Find the result and print
# a + b + c = d
d = a + b + c
# d - a = e
e = d - a
# e + d = f
f = e + d
# f // 2 = g
g = f // 2
# c**2 = z
z = c ** 2
# Print all variables/results
print(f"a:{a} - b:{b} - c:{c} - d:{d} - e:{e} - f:{f} - g:{g} - z:{z}")

# 2. Comparison Operations
# Comparison operators are used to compare values and return a Boolean result (True or False)

x = 5
y = 8

# comparing values

is_greater = x > y  # False, because 5 is not greater than 8
is_equal = x == y  # False, because 5 is not equal to 8
is_not_equal = x != y  # True, because 5 is not equal to 8
is_less_or_equal = x <= y  # True, because 5 is less than or equal to 8

# Print the comparison results
print("Comparison Operations:")
print(f"Is x greater than y? {is_greater}")
print(f"Is x equal to y? {is_equal}")
print(f"Is x not equal to y? {is_not_equal}")
print(f"Is x less than or equal to y? {is_less_or_equal}")
print()  # Blank line for readability

# Assignment operators are used to assign values to variables. 
# These operators include simple assignment, addition assignment, subtraction assignment, etc.

# Simple assignment operator: Assigns value to a variable
x = 10  # Assigning value 10 to variable x
print(f"Simple assignment: x = {x}")

# Addition assignment operator: Adds a value to the variable and assigns the result to the same variable
x += 5  # Equivalent to x = x + 5
print(f"Addition assignment: x += 5 -> x = {x}")

# Subtraction assignment operator: Subtracts a value from the variable and assigns the result to the same variable
x -= 3  # Equivalent to x = x - 3
print(f"Subtraction assignment: x -= 3 -> x = {x}")

# Multiplication assignment operator: Multiplies the variable by a value and assigns the result to the same variable
x *= 2  # Equivalent to x = x * 2
print(f"Multiplication assignment: x *= 2 -> x = {x}")

# Division assignment operator: Divides the variable by a value and assigns the result to the same variable
x /= 4  # Equivalent to x = x / 4
print(f"Division assignment: x /= 4 -> x = {x}")

# Modulus assignment operator: Takes modulus of the variable with a value and assigns the result to the same variable
x %= 3  # Equivalent to x = x % 3
print(f"Modulus assignment: x %= 3 -> x = {x}")

# Exponentiation assignment operator: Raises the variable to the power of a value and assigns the result
x **= 2  # Equivalent to x = x ** 2
print(f"Exponentiation assignment: x **= 2 -> x = {x}")

# Floor division assignment operator: Divides the variable by a value and takes the floor of the result
x //= 2  # Equivalent to x = x // 2
print(f"Floor Division assignment: x //= 2 -> x = {x}")

# 3. Logical Operations
# Logical operators are used to combine multiple conditions

is_raining = True
is_cold = False

# using logical operators
stay_home = is_raining and is_cold  # False, both conditions need to be True for AND
go_outside = is_raining or is_cold  # True, at least one condition is True for OR
not_raining = not is_raining  # False, negates the value of is_raining

# Print the logical operations results
print("Logical Operations:")
print(f"Stay home (is raining AND is cold): {stay_home}")
print(f"Go outside (is raining OR is cold): {go_outside}")
print(f"Is it not raining? {not_raining}")
print()  # Blank line for readability