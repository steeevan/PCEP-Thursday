tup= (1,2,3,4,5,6,7,8,9,0)
print(len(tup))
print(tup[0:3])
print(tup[::-1])
d= {"William":12,
    "James":13,
    "Yanming":11,
    "Logan":11,
    "Howard":11}
print(d)
d["Frank"]=11
print(d)
del d["James"]
print(d)
#Im not sure how to do it
print(d["William"])

string= "uno"
print(string.upper())
#Im not sure what you meant by digit
#del string[int]
string.replace("a","*")
string.replace("i","*")
string.replace("o","*")
string.replace("u","*")
string.replace("e","*")
print(string)
students = [('John', 85), ('Alice', 92), ('Bob', 78)]
d2=dict(students)
print(d2)

ages = {'Alice': 30, 'Bob': 25, 'Charlie': 30, 'Diana': 22}
print({value: key for key, value in ages.items()})

string2="A man a plan a canal Panama"
string2.replace(" ","")
re2=reversed(string2)
if re2==string2:
    print("palindrome" )
else:
    print("not a palindrome ")

sentence = "This is a test. This test is only a test."
This= "this"
is1="is"
a="a"
test="test"
only="only"
coun1=sentence.count(This)
coun2=sentence.count(is1)
coun3=sentence.count(a)
coun4=sentence.count(test)
coun5=sentence.count(only)
d3= {"This":coun1,
     "is":coun2,
     "a":coun3,
     "test":coun4,
     "only":coun5}

text = "hello world"
#NOt sure

dict1 = {'a': 100, 'b': 200}
dict2 = {'a': 300, 'c': 400}
dict3=dict1.update(dict2)
print(dict3)
tup2=(1,2,3)
tup3=(4,5,6)
print(tup2+tup3)
tup4=tup2+tup3
(a,b,c,d,e,f)=tup4
print(a,b,c)
print(d,e,f)
