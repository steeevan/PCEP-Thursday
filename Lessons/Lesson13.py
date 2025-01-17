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