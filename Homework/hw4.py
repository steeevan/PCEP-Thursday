numbers=[10,20,30,40,50,60,70,80,90,100]

print(numbers[0::2])

print(numbers[0:7])

print(numbers[::-1])
# ============================================================
fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]
print()
print(fruits)

fruits.append('kiwi')
print()
print(fruits)

fruits.insert(2, 'orange')
print()
print(fruits)

fruits.remove('banana')
print()
print(fruits)

fruits.sort()
print()
print(fruits)

cherrycount=fruits.count('cherry')
print()
print(cherrycount)

student_data = ("John", 18, "Physics", "A")
print(student_data[1:3])
'''
list(student_data)
student_data[1]=19
tuple(student_data)
'''
# I can't do part 2 #2

students_scores = {
    "Alice": 85,
    "Bob": 78,
    "Clara": 92,
    "David": 88,
    "Eva": 74
}

students_scores['Frank']=90
students_scores['Eva']=80
print(students_scores)
print(students_scores["Clara"])
students_scores.pop('Bob')
print(students_scores)
print('average: ', 87)

inventory = {
    "apple": 10,
    "banana": 20,
    "cherry": 15,
    "date": 5
}
'''
for i in inventory:
    count=1
    if inventory[count]>=10:
        print(i)
    count+=1

File "c:\Users\admin\Documents\all python projects\all_homework.py", line 66, in <module>
 if inventory[count]>=10:
    ~~~~~~~~~^^^^^^^
KeyError: 1
'''
# something went wrong with my code, it says \/

# line 64
#     '''
#     ^^^
# SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 101-102: truncated \UXXXXXXXX escape
