numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(numbers[1::2])
# discovered on the internet \/
print(numbers[-4:])

print(numbers[::-1])

fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]
fruits.append("kiwi")
fruits.insert(2, "orange")
fruits.remove("banana")
fruits.sort()
print(fruits.count("cherry"))

# used the internet to figure this one
evensquares = [x**2 for x in range(1, 21) if x % 2 == 0]
print(evensquares)

student_data = ("John", 18, "Physics", "A")
# found this out on the internet \/
name, grade = student_data[0], student_data[3]

studentdatalist = list(student_data)
studentdatalist[1] = 19
student_data = tuple(studentdatalist)

fruits=('apple','cherry', 'pineapple','orange','avocado')
def fruitswith_a(fruits):
    # found command '.startswith()' on the internet \/
    return [fruit for fruit in fruits if fruit.startswith('a')]
print(fruitswith_a)

student_scores = {"Alice": 85, "Bob": 78, "Clara": 92, "David": 88, "Eva": 74}
student_scores["Frank"] = 90
student_scores["Eva"] = 80
print(student_scores["Clara"])
del student_scores["Bob"]
average_score = sum(student_scores.values()) / len(student_scores)
print(average_score)

inventory = {"apple": 10, "banana": 20, "cherry": 15, "date": 5}
def instock(inv):
    # figured this out with lots of help \/
    return [fruit for fruit, quantity in inv.items() if quantity > 10]

sentence = "Python programming is fun and powerful."
print(sentence.upper())
print(len(sentence.split()))
print(sentence.replace("fun", "exciting"))
print(sentence[sentence.index("powerful"):sentence.index("powerful") + len("powerful")])

def palindrome(word):
    return word == word[::-1]

'''
By the way, I used the internet on a lot of the questions
because I wasn't sure how to solve it
'''
