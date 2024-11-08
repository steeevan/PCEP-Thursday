### **Homework Assignment: Functions in Python**

---

#### **Objective**:
To test your understanding of functions, including creating, using, and interacting with them. You will also apply concepts like parameters, return values, recursion, and decomposition.

---

### **Part 1: Basic Functions**
1. **Hello Function**  
   Write a function `say_hello()` that prints `"Hello, Python!"`.

   **Output Example**:
   ```
   Hello, Python!
   ```

2. **Square a Number**  
   Write a function `square(number)` that takes a number and returns its square.

   **Example**:
   ```python
   square(5)  # Output: 25
   ```

3. **Area of a Rectangle**  
   Write a function `calculate_area(length, width)` that calculates and returns the area of a rectangle.

   **Example**:
   ```python
   calculate_area(5, 3)  # Output: 15
   ```

---

### **Part 2: Intermediate Functions**
4. **Temperature Converter**  
   Write a function `convert_temperature(value, to_unit)` that converts a temperature value between Celsius and Fahrenheit. Include default parameters to set `to_unit="C"`.

   **Example**:
   ```python
   convert_temperature(100, "F")  # Output: 212.0
   convert_temperature(32)       # Output: 0.0
   ```

5. **Recursive Factorial**  
   Write a recursive function `factorial_recursive(n)` that calculates the factorial of a number.

   **Example**:
   ```python
   factorial_recursive(5)  # Output: 120
   ```

6. **Maximum of Three**  
   Create a function `find_max(a, b, c)` that returns the largest of three numbers.

   **Example**:
   ```python
   find_max(3, 7, 5)  # Output: 7
   ```

---

### **Part 3: Advanced Functions**
7. **Matrix Addition**  
   Write a function `add_matrices(matrix1, matrix2)` that takes two matrices (2D lists) of the same size and returns their sum.

   **Example**:
   ```python
   add_matrices([[1, 2], [3, 4]], [[5, 6], [7, 8]])
   # Output: [[6, 8], [10, 12]]
   ```

8. **Prime Checker**  
   Write a function `is_prime(number)` that returns `True` if the number is a prime number and `False` otherwise.

   **Example**:
   ```python
   is_prime(13)  # Output: True
   is_prime(16)  # Output: False
   ```

9. **Quadratic Solver**  
   Write a function `solve_quadratic(a, b, c)` that calculates the roots of the quadratic equation \(ax^2 + bx + c = 0\). Use conditional statements to check if the roots are real or imaginary.

   **Example**:
   ```python
   solve_quadratic(1, -3, 2)  # Output: (2.0, 1.0)
   ```

---

### **Part 4: Challenge Problems**
10. **Palindromic Words**  
    Write a function `is_palindrome(word)` to check if a word is a palindrome. Extend it to handle case sensitivity and spaces.

    **Example**:
    ```python
    is_palindrome("Racecar")  # Output: True
    is_palindrome("hello")    # Output: False
    ```

11. **Fibonacci Sequence**  
    Create a function `generate_fibonacci(n)` that generates the first `n` Fibonacci numbers using iteration.

    **Example**:
    ```python
    generate_fibonacci(6)  # Output: [0, 1, 1, 2, 3, 5]
    ```

12. **Sorting Algorithm**  
    Implement a function `sort_numbers(numbers)` that sorts a list of numbers in ascending order without using Python's built-in `sort()` method.

    **Example**:
    ```python
    sort_numbers([7, 3, 5, 1])  # Output: [1, 3, 5, 7]
    ```

---

#### **Instructions**:
1. Write your solutions in a `.py` file or notebook.
2. Test each function with at least two different sets of inputs.
3. Submit your file or screenshots of your results.

#### **Optional Bonus**:
- Try writing explanations for each function, describing how it works step-by-step.

---

Let me know if you'd like a rubric for grading this assignment!