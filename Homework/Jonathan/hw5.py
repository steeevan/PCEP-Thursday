# 1.
numbers=(1,2,3,4,5,6,7,8,9,10)
print('length of numbers:',len(numbers))
print(numbers[0:3])
print(numbers[::-1])
print()

# 2.
peoplebook = {
    'Bob': 65,
    'Rob': 34,
    'Brian': 44,
    'Bruce': 105,
    'Terry': 57
}
peoplebook['Bryce']=21
del peoplebook['Bob']
# found the 'max' function on the internet
oldestperson=max(peoplebook, key=peoplebook.get)
print(oldestperson)

#3.
'''
def inputstring():
    string=(input('type in something (returns all uppercase, no vowels or digits): '))
    uh oh
    string.upper()
    string.replace('a','e','o','u','i', '')
    print(string)
inputstring()
'''
# 4.
students = [('John', 85), ('Alice', 92), ('Bob', 78)]
dictstudents=dict(students)
print(dictstudents)

# 5. I had help with the internet
def ispalindrome(stuff):
    
    normalized_str=''.join(stuff.split()).lower()
    
    return normalized_str==normalized_str[::-1]

string=input("input something: ")

if ispalindrome(string):
    print("Palindrome")
else:
    print("Not a palindrome")

#7.
def wordcount(sentence):
    # found this way of using commands on the internet
    words=sentence.lower().replace('.', '').split()
    worddict={}
    
    for word in words:
        if word in worddict:
            worddict[word]+=1
        else:
            worddict[word]=1
            
    return worddict

sentence="This is a test. This test is only a test."
print(wordcount(sentence))

# 8.
def mostfrequentcharacter(text):
    char_count={}
    # had help from internet
    for char in text.replace(' ', ''):
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1

    mostfrequent=max(char_count, key=char_count.get)
    return mostfrequent

text="hello world"
print(mostfrequentcharacter(text))

# 9.
def mergedictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    # had help from internet
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key]+=value
        else:
            merged_dict[key]=value
            
    return merged_dict

dict1 = {'a': 100, 'b': 200}
dict2 = {'a': 300, 'c': 400}
print(mergedictionaries(dict1, dict2))

# 10.
person1=("Rob", 30, "New York")
person2=("Bob", 25, "Los Angeles")
combinedtuple=person1+person2
name1,age1,city1,name2,age2,city2=combinedtuple

print("combined tuple: ", combinedtuple)
print("individual items: ")
print(name1, age1, city1)
print(name2, age2, city2)

'''
Again, I had a lot of help from the internet and a lot of things
I just found it out on the internet
'''
