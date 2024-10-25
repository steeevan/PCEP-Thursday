'''
Lesson Plan: Collecting and Processing Data with Tuples, Dictionaries, and Strings
- Understand how to collect and process data using tuples and dictionaries in Python
- Learn how to operate with strings, including basic and advanced string manipulation
- apply these concepts through exercises and activities
'''

# 5.1 Tuples
'''
A tuple is a collection of ordered , immutable elemts in Pyton. ONce a tuple is created
its elements cannot be modified.
'''
# Example 5.1.1
# Create a tuple
my_tuple = (1,2,3)
my_tup = () # Empty Tuple
my_tupC = tuple()
my_tupL = tuple([1,2,3])
coord = (5,10)

# Unpacking a tuple
x,y = coord  # x = 5, and y = 10
single_tup = (5,)
single_tup2 = 4,
'''
Indexing: Accessing elements using their index.
Slicing: Retrieving a subset of elements.
Unpacking: Assigning tuple elements to variables.
Concatenation: Joining two or more tuples together.
'''
print(my_tuple)
print(my_tupL)
print(my_tupC)
print(my_tup)
print(coord)
print(x)
print(y)
print(single_tup)
print(single_tup2)

'''
Exercises for Tuples
1. Create a tuple with five elements and print the second and last elements.
2. Unpack the values from a tuple containing three elements into three different variables.
3. Create two tuples and concatenate them into one.
'''
#1 
tup5 = (5,4,3,2,1)
print(tup5[1],tup5[4])

#2
coord = (4,6,10)
x,y,z = coord
print(x,y,z)

#3
ctup = tup5 + coord
print(ctup)

'''
5.2 Dictionaries
A dictionary is a collection of key-value pairs. Each key must be unique and immutable
(such as a string or a number) but values can be mutable, and of any type
'''

# 5.2.1 Syntax
# create a dictionary
my_dict = {'name': "John",'age':25,'city':'Los Angeles'}
# make an empty dictionary
my_dict2 = {}
my_dict2 = dict() # using a dictionary constructor
my_dict3 = dict(name='John',age=25,city='Chino Hills')
data = [('name', "Mr E"), ('age',25), ('city', 'Los Angeles')]

my_data_dict = dict(data)
print(my_dict)
print(my_dict2)
print(my_dict3)
print(my_data_dict)

# Using comprehension
my_comp_dict = {x: x**2 for x in range(1,6)}
print(my_comp_dict)

sample = my_dict

# Accessing values by keys
person = sample['name']
print(person)

# Updating a dictionary using get
sample['name'] = "William"
print(sample.get('name'))
print(sample)
'''
- Adding/Updating values: dict[key] = value
- Removing items: del dict[key] or dict.pop(key)
- Iterating through dictionaries: Use .items() to loop over key-value pairs.
'''

'''
Acvitities 5.2 Dictionary
1. Create a dictionary of three items and print each key and its corresponding value.
2. Add a new key-value pair to an existing dictionary.
'''

#1
d = {"name":"Mr E", "grade": "A+", "level":"noob"}
print(d)
print(d.keys())
print(d.values())
print(d.items())
#2
d['student'] = "9th grade"
print(d)

'''
5.3 String
A string a sequence of characters. Strings are immutable in Python, meaning they cannoy
be changed after created
'''

# 5.3.1
# SYntax
my_string = "Hello World"
my_string = 'Hellow World'

my_str = str()

multiline_string = """This is a
multiline string."""

char_list = ['H', 'e', 'l', 'l', 'o']
my_string = ''.join(char_list)  # 'Hello'

'''
String methods
.upper(): Converts string to uppercase.
.lower(): Converts string to lowercase.
.strip(): Removes leading and trailing whitespace.
.replace(): Replaces a substring with another substring.
.split(): Splits a string into a list based on a delimiter.
.join(): Joins a list of strings into a single string.

Activity String
1. Write a program that takes a user’s full name and prints the initials in uppercase.
2. Create a program that takes a sentence and counts how many times a specific letter appears.
3. Create a program that replaces all spaces in a sentence with underscores.
'''
#1
fname = "estevan"
lname = "anguiano"
print( fname , lname, sep=" ")
print(fname[0].upper(), lname[0].upper(), sep=".")
fullname = fname + lname
print(fullname.count('n'))
