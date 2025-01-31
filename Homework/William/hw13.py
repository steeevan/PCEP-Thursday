#homework
l=[1,2,3,4,5]
def reverse(lis):
    print(lis[::-1])
reverse(l)

nums=[5,7,10,13,15,18,20]

def determine(num,div):
    nuw_list=[]
    for i in num:
        if i % div ==0:
            nuw_list.append(i)
    print(nuw_list)

determine(nums,5)

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
def count(words, choice):
    count=0
    for i in words:
        if i.lower() == choice.lower():
            count+=1
    print(count)

count(words,"apple")

num_list=[-1, 2, -3, 4, -5]

def NOOOOOOOO_Negative(li):
    new_lis=[]
    for i in li:
        if i < 0:
            new_lis.append(0)
        else:
            new_lis.append(i)
    print(new_lis)

NOOOOOOOO_Negative(num_list)

def combine(l1,l2):
    l3= sorted(l1+l2)
    print(l3)

list1 = [1, 3, 5]
list2 = [2, 4, 6]
combine(list1,list2)

def find(list1,target):
    count=0
    activate=True
    for i in list1:
        count+=1
        if i == target:
            print(f"index: {count-1}")
            activate=False
    if activate :
        print(-1)
        

nums = [10, 20, 30, 40, 50]

find(nums,30)

def square(lis):
    new_lis=[]
    for i in lis:
        new_lis.append(i*i)
    print(new_lis)

lista=[1, 2, 3, 4]
square(lista)

fruits= ["apple", "banana", "apple", "orange", "apple", "banana"]

def most_frequent(li):
    print (max(set(li), key=li.count))

most_frequent(fruits)

numbers=[0, 1, 2, 0, 3, 0, 4]

def NOOOOOOOOOOOOOOOOOOOOOOOOOOOOO_zero(lis):
    new_lis=[]
    for i in lis:
        if i==0:
            pass
        else:
            new_lis.append(i)
    print(new_lis)

NOOOOOOOOOOOOOOOOOOOOOOOOOOOOO_zero(numbers)

def split(l):
    new1=[]
    new2=[]
    integer=len(l)//2
    int2= len(l)-integer
    new1.append(l[0:integer+1])
    new2.append(l[int2:len(l)])
    print(new1,new2)
lisb=[1, 2, 3, 4, 5]

split(lisb)




