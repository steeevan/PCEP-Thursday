#homework 4

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
evens= numbers[0:9:2]
print(evens)
last= numbers[6:9]
print(last)
reverse= numbers[0:-9]
print(reverse)

fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]
fruits.append(fruits)
fruits.insert(2,"orange")
fruits.remove("banana")
fruits.sort()
howmany= 0
for i in range(fruits):
    if i == "cherry":
        howmany += 1

nums= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
num2=[]
for i in range(nums):
    if i % 2 ==0:
        i**2
        num2.append(i)


student_data = ("John", 18, "Physics", "A")
name= student_data[0]
grade= student_data[3]
list(student_data)[2]=19
tuple(student_data)

tuple_fruits = ["apple", "banana", "cherry", "date", "fig"]
def a (tup):
    for i in range (tup): # go through the list to see if there is a in the first character
        if i[0]==a:
            print(i)
a(tuple_fruits)

students_scores = {
    "Alice": 85,
    "Bob": 78,
    "Clara": 92,
    "David": 88,
    "Eva": 74
}
#asign a new key
students_scores["Frank"]=90
#replace the score
students_scores["Eva"]=80
print(students_scores["Clara"])
del students_scores["Bob"]
#obtain the total score:
total= students_scores["Alice"]+students_scores["Clara"]+students_scores["David"]+students_scores["Eva"]+students_scores["Frank"]
average= total/5  #divide to see the average 
print(average)

inventory = {
    "apple": 10,
    "banana": 20,
    "cherry": 15,
    "date": 5
}

def stock(dicts):
    for i in range (inventory.values):#going through to see if it greater than 10 each
        count+=1
        if i > 10:
            print(inventory[count])

sentence = "Python programming is fun and powerful."
sentence.upper()
words= sentence.find(" ")#finding how many spce which means how many words

new= sentence.replace("fun","exciting")
excite= sentence[30:37]#get the index of powerful

print(excite)
print(sentence)
print(words)
print(new)

"""
Note:
while doing homework it not loading the codes in the output

"""
