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

last_week = ["milk", "bread", "eggs", "cheese", "apples"]  
this_week = ["bread", "oranges", "milk", "bananas"]
copies = []

for item in last_week:
    if item in this_week:
        copies.append(item)

print(copies)

# Exercsise #2
celsius = []
fahrenheit_temps = [32, 50, 77, 90]
for f in fahrenheit_temps:
    c = (f - 32) * (5/9)
    celsius.append(int(c))

print(celsius)

# 3
all_recipes = ["pasta with tomato sauce", "chicken curry", "avocado salad", "berry smoothie"]  
favorite_ingredients = ["avocado", "berry"]
fav_recipes = []
for recipe in all_recipes:
    for ingredient in favorite_ingredients:
        if ingredient in recipe:
            fav_recipes.append(recipe)
            break


    #4
all_task = []
personal_tasks = ["buy groceries", "call mom", "walk dog"]  
work_tasks = ["finish report", "team meeting", "call client"]

all_task += personal_tasks
all_task += work_tasks
all_task.sort()
print(all_task)

# 5
study_times = [30, 45, 60, 25, 50, 40, 35]
total_time = 0
for time in study_times:
    total_time += time
average_study_time = total_time / len(study_times)


#6
prices = [10.99, 25.50, 5.75, 15.00, 50.00]  
threshold = 20.00
below_threshold = []
for price in prices:
    if price < threshold:
        below_threshold.append(price)
