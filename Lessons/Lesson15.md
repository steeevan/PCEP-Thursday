
### **Lesson Title: Iterating with List Slicing in Python**
**Objective:**  
By the end of this lesson, students will be able to:
- Understand list slicing in Python.
- Use loops with list slicing to manipulate and process data.
- Apply list slicing within `for` loops to iterate over portions of a list.
- Solve exercises that involve list slicing and iteration.

---

## **1. Introduction to List Slicing**
Python’s **list slicing** allows extracting a subset of a list using the syntax:

```python
list[start:stop:step]
```

- `start`: The starting index (inclusive).
- `stop`: The stopping index (exclusive).
- `step`: The step size for skipping elements (default is `1`).

### **Examples:**
```python
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(numbers[2:6])   # Output: [2, 3, 4, 5]
print(numbers[:5])    # Output: [0, 1, 2, 3, 4]
print(numbers[3:])    # Output: [3, 4, 5, 6, 7, 8, 9]
print(numbers[::2])   # Output: [0, 2, 4, 6, 8]
print(numbers[::-1])  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (Reverse list)
```

---

## **2. Using Loops with List Slicing**
We can use list slicing inside `for` loops to iterate over selected portions of a list.

### **Example 1: Iterating over a Sliced List**
```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

for fruit in fruits[1:4]:  # Extracts elements from index 1 to 3
    print(fruit)
```
**Output:**
```
banana
cherry
date
```

### **Example 2: Iterating with Step**
```python
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for num in numbers[::2]:  # Picks every second number
    print(num)
```
**Output:**
```
10
30
50
70
90
```

### **Example 3: Looping Over a Reversed List**
```python
names = ["Alice", "Bob", "Charlie", "David"]

for name in names[::-1]:  # Reverse iteration
    print(name)
```
**Output:**
```
David
Charlie
Bob
Alice
```

---

## **3. Exercises**
### **Exercise 1: Print Every Third Element**
Given a list, print every third element using slicing.

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# Your Code Here
```
**Expected Output:**
```
1
4
7
10
```

---

### **Exercise 2: Print the Middle Elements**
Extract the middle three elements from a list and iterate over them.

```python
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink"]
# Your Code Here
```
**Expected Output:**
```
green
yellow
purple
```

---

### **Exercise 3: Reverse and Print Every Other Element**
Reverse the list and print every second element.

```python
words = ["dog", "cat", "elephant", "tiger", "lion", "bear"]
# Your Code Here
```
**Expected Output:**
```
bear
tiger
cat
```

---

## **4. Challenges**
### **Challenge 1: Sum of Every Second Number**
Write a program that calculates the sum of every second number in a list.

```python
nums = [5, 10, 15, 20, 25, 30, 35, 40]
# Your Code Here
```
**Expected Output:**
```
Sum: 100
```

---

### **Challenge 2: Check if a Word is a Palindrome**
Use slicing inside a loop to check if a word is a palindrome.

```python
word = "racecar"
# Your Code Here
```
**Expected Output:**
```
Yes, it's a palindrome!
```

---

## **5. Summary**
- List slicing allows selecting portions of a list.
- Using slicing with `for` loops helps process parts of a list efficiently.
- You can iterate through slices, use steps, and reverse iterate using `[::-1]`.

