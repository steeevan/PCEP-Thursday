## Part 1: Expression Evaluation

**Instructions:**

For each question below, **predict the exact output** that will be printed by Python 3. If multiple choices are given, select the **single correct** answer. Otherwise, provide the numeric/float/string output as appropriate.

---

### 1. Example 1

```python
print(5 * 2 + 8 / 4)
```

A. `14.0`

B. `14`

C. `6.0`

D. `8.0`

### 2. Example 2

```python
print(7 / 2 * 2)
```

A. `7.0`

B. `3.5`

C. `3`

D. `7`

### 3. Example 3

```python
print(2 ** -1 + 5 // 2)
```

A. `2.5`

B. `3.5`

C. `4`

D. `5.0`

### 4. Example 4

```python
print((4 - 2) ** 3 / 2 + 1)
```

A. `5.0`

B. `11.0`

C. `8`

D. `4.0`

### 5. Example 5

```python
print(3 * 2 ** 3)
```

A. `8`

B. `6`

C. `24`

D. `9`

### 6

```python
print(8 / (2 + 2) ** 2)
```

A. `0.5`

B. `2.0`

C. `2.5`

D. `4.0`

### 7

```python
print(-10 % 3)
```

A. `-1`

B. `2`

C. `-2`

D. `1`

### 8

```python
print(-3 ** 2)
```

A. `-9`

B. `9`

C. `-3`

D. `3`

### 9

```python
x = 2
x *= 3 + 2
x /= 2
print(x)
```

A. `5.0`

B. `4.0`

C. `8.0`

D. `3.0`

### 10

```python
print(1 + 2 ** 3 // 4 * 3.0)
```

A. `7.0`

B. `5.0`

C. `6.0`

D. `9.0`

### 11

```python
print(3 + 4 * 2)
```

*(Provide the numeric output—no multiple choice.)*

### 12

```python
print((2 + 5) // 3 * 2)
```

*(Provide the numeric output—no multiple choice.)*

### 13

```python
print(10 / 5 + 3 * 2)
```

*(Provide the numeric output—no multiple choice.)*

### 14

```python
print(10 // 5 + 3 / 2)
```

*(Provide the numeric output—no multiple choice.)*

### 15

```python
print(4 ** 2 - 2 ** 3)
```

*(Provide the numeric output—no multiple choice.)*

### 16

```python
print(3 + 3 * (2 + 4))
```

*(Provide the numeric output—no multiple choice.)*

### 17

```python
print((2 + 3) ** 2 / (4 - 2))
```

*(Provide the numeric output—no multiple choice.)*

### 18

```python
print(10 - 8 // 3)
```

*(Provide the numeric output—no multiple choice.)*

### 19

```python
print(10 - 8 / 3)
```

*(Provide the numeric output—no multiple choice; it will be a float.)*

### 20

```python
print(4 * 3 // 2 + 7 % 4)
```

*(Provide the numeric output—no multiple choice.)*

### 21

```python
print(2 * (5 + 3) / 4)
```

*(Provide the numeric output—no multiple choice.)*

### 22

```python
print((3 + 4) / 2 * 3)
```

*(Provide the numeric output—no multiple choice.)*

### 23

```python
print(25 // 10.0)
```

*(Provide the numeric output—no multiple choice; note the float divisor.)*

---

## Part 2: Coding Challenges

For each challenge, **write a short Python snippet** (or function) that does the requested task, demonstrating your knowledge of **operator precedence** and basic arithmetic operations.

1. **Exponentiate & Floor**
   * Write a function `floor_exponent(base, exponent, divisor)` that:
     1. Calculates `base ** exponent`.
     2. Performs floor division (`//`) by `divisor`.
     3. Returns the result.
   * Example call: `floor_exponent(2, 3, 3)` should return ` (2**3)//3 = 8//3 = 2`.
2. **Compute Weighted Expression**
   * Write a short program that:
     1. Takes three integer inputs aa, bb, and cc from the user (via `input()`).
     2. Computes the expression a2−b∗c+(b//a)a^2 - b * c + (b // a).
     3. Prints the result as an **integer** (floor if needed).
3. **Mixed Operators with Floats**
   * Define a function `mixed_arithmetic(a, b)` that:
     1. Converts `a` to float.
     2. Returns the result of `a / b + a * b - (a // b)`.
   * Demonstrate it with a couple of test calls, e.g., `mixed_arithmetic(7, 2)`.
4. **Practice with Modulo and Negative Numbers**
   * Create a program that prompts the user for  **two integers** , `x` and `y`.
   * Print out **both** `x % y` and `y % x`.
   * Discuss (in a brief comment) how Python handles the sign of the result for modulo with negatives.
5. **Bracket & Precedence**
   * Write a function `custom_calc(x, y, z)` that returns (x+y)∗∗z−x%y+x/(z−y)(x + y) ** z - x\%y + x / (z - y).
   * Show example calls with different integer/float combinations to highlight tricky precedence.
6. **Operator Precedence Self-Test**
   * Write a single line of code that prints the result of:
     10−2∗∗3//2+(3/2)  10 - 2 ** 3 // 2 + (3 / 2)
   * Run it and confirm the answer is as expected. Explain in a comment how you arrived at that result.

---
