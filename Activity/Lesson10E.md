Below are two exercise activities, each divided into three parts. These activities are intended to help reinforce the concepts you've learned about `try` and `except` in Python.

---

## Activity 1

### Part A
**Objective:** Introduce a `try/except` block to handle known error scenarios.

**Task:**
1. Write code that attempts to convert a user-provided input string into an integer.
2. If the input is not a valid integer (e.g., "abc"), print: `"Invalid integer input."`
3. Otherwise, print: `"Valid integer: <converted_value>"`

**Example Expected Behavior:**
- Input: `"123"` => Output: `"Valid integer: 123"`
- Input: `"xyz"` => Output: `"Invalid integer input."`

### Part B
**Objective:** Use multiple `except` blocks to handle different exception types.

**Task:**
1. Create a list, for example: `my_list = [10, 20, 30]`.
2. Prompt the user for an index and try to print the item at that index.
3. If a `ValueError` occurs (the user didn’t provide a number), print: `"Please enter a numeric index."`
4. If an `IndexError` occurs (the index is out of bounds), print: `"Index out of range."`
5. If no exception occurs, print: `"Item: <item_value>"`

**Example Expected Behavior:**
- Input: `"1"` => Output: `"Item: 20"`
- Input: `"abc"` => Output: `"Please enter a numeric index."`
- Input: `"10"` => Output: `"Index out of range."`

### Part C
**Objective:** Use `else` and `finally` in conjunction with `try/except`.

**Task:**
1. Write code that attempts to read from a file named `"data.txt"`.
2. If `data.txt` is found and readable, print: `"File read successfully!"` inside the `else` block.
3. If the file is not found, print: `"File not found."`
4. Regardless of success or failure, print: `"Operation complete."` in the `finally` block.

**Example Expected Behavior:**
- If `data.txt` exists:  
  Output:
  ```
  File read successfully!
  Operation complete.
  ```
- If `data.txt` is missing:  
  Output:
  ```
  File not found.
  Operation complete.
  ```

---

## Activity 2

### Part A
**Objective:** Practice raising and catching custom exceptions.

**Task:**
1. Define a custom exception class named `NegativeNumberError`.
2. Write code that:
   - Prompts the user for a number.
   - Raises `NegativeNumberError` if the user inputs a number less than zero.
   - Otherwise, prints the number.
3. If `NegativeNumberError` is raised, catch it and print: `"Negative numbers are not allowed."`

**Example Expected Behavior:**
- Input: `5` => Output: `"You entered: 5"`
- Input: `-3` => Output: `"Negative numbers are not allowed."`

### Part B
**Objective:** Catch multiple exceptions in one `except` block using a tuple.

**Task:**
1. Prompt the user for input to perform a division: first ask for a numerator and then a denominator.
2. Attempt to perform the division.
3. Use a single `except (ValueError, ZeroDivisionError) as e:` block to handle both:
   - `ValueError` if inputs are not numbers.
   - `ZeroDivisionError` if the denominator is zero.
4. If an exception occurs, print: `"Error occurred:"` followed by the exception message.
5. If no error occurs, print the result of the division.

**Example Expected Behavior:**
- Numerator: `"10"` and Denominator: `"2"` => Output: `5.0`
- Numerator: `"abc"` and Denominator: `"2"` => Output: `"Error occurred: invalid literal for int() ..."`
- Numerator: `"10"` and Denominator: `"0"` => Output: `"Error occurred: division by zero"`

### Part C
**Objective:** Use `try/except` for data validation inside a loop.

**Task:**
1. Create a loop that keeps asking the user for integers.
2. If the user inputs a valid integer, append it to a list.
3. If the user inputs a non-integer, catch the `ValueError`, print `"Invalid input, stopping."`, and break out of the loop.
4. After the loop ends, print the list of all successfully entered integers.

**Example Expected Behavior:**
- Inputs: `10`, `20`, `30`, `abc`  
  Output:
  ```
  Invalid input, stopping.
  [10, 20, 30]
  ```
  
- Inputs: `5`, `6`, `7` (then user ends input by sending a non-integer, say `"end"`)  
  Output:
  ```
  Invalid input, stopping.
  [5, 6, 7]
  ```

---

**By completing these activities, you’ll gain hands-on experience with Python’s error handling mechanisms, including handling multiple exceptions, using `else` and `finally` blocks, raising custom exceptions, and leveraging `try/except` logic in real-world scenarios.**