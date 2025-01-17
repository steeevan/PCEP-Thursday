'''
Solving Problems with Loops and Lists
Lists: mutable collections of items that can be found by being indexed, sliced, and iterated
Loops:
    - for loops: iterate directly over items in a sequence
    - while loops: continue running while a condition is true.

'''

# numbers is a list
def ex1(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

#1 problem
# 
nums = [4,2,95,3]
print(ex1(nums))

# exercise # 2
# given data
nums = [1,2,3,4,5,6]

def ex2(numbers):
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

# Exercsies 3
# given data
nums = [10,20,30,40]

def ex3(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count if count > 0 else 0



# Exercsie 1 on SHeet

def unique_chars(s):
    from collections import Counter
    s = ''.join(filter(str.isalnum, s.lower()))
    count = Counter(s)
    return [char for char, freq in count.items() if freq == 1]

print(unique_chars("LeetCode"))