#The purpose of exeption is to continue the code upon syntax error
#The keyword else is executed when no error happens. 
#The keyword finally is executed no matter what.
#Three common ValueError, TypeError, NameError

#At the line 5, there was a ZeroDivisionError which could be fixed by not dividing 

try:
  filename= input("Insert a filename")

except FileNotFoundError:
  print("Error")

finally:
  print("Finish")

#IDK how to open a file


class NegativeNumberError(Exception):
    if Exception < 0:
        print("Negative Number are not allowed")

def calculator(a,b,oper):
   if oper=="/":
      try:
         a/b
      except ZeroDivisionError or ValueError as e:
         print(f"The eroro is {e}")
   elif oper=="*":
      try:
         a*b
      except ZeroDivisionError or ValueError as e:
         print(f"The eroro is {e}")
   elif oper=="+":
      try:
         a+b
      except ZeroDivisionError or ValueError as e:
         print(f"The eroro is {e}")
   elif oper=="-":
      try:
         a-b
      except ZeroDivisionError or ValueError as e:
         print(f"The eroro is {e}")
   elif oper != "*" or oper !="/" or oper !="+" or oper !="-":
      print("not a operator")
   
a= int(input("Enter a number")) 
b= int(input("Enter a number")) 
o= input("Enter a operator between /,+,-,*")

while True:
    calculator(a,b,o)
    continu=input("DO you want to continue")
    if continu=="no":
       break


import math

num= int(input("Inter a number"))
try:
   value= math.sqrt(num)
except (ValueError or TypeError) as e:
   print(f"there is a error of {e} ")

#Idk how to do the last part

numa= int(input("Enter a number"))
numb= int(input("Enter a number"))
try:
   print(numa/numb)
except (ZeroDivisionError or ValueError) as e:
   print(f"The error is {e}")
else:
   print("Nested try block executed successfully")   

balance= 500
while True:
   ask=input("Enter 1 to check balance. Enter 2 to withdraw money. Enter 3 to deposit money")
   if ask=="1":
      print("$",balance)
      print("process done")
   elif ask=="2":
      try:
         amount=int(input("How many do you want to withdraw"))
      except (ValueError or NegativeNumberError) as e:
         print(f"There is a issue of {e}")
      else:
         try:
            balance-=amount
         except NegativeNumberError :
            print("Not enough money to withdraw")
      finally:
         print("process done")
   elif ask=="3":
      try:
         amount=int(input("How many do you want to add"))
      except (ValueError or NegativeNumberError) as e:
         print(f"There is a issue of {e}")
      else:
         balance+=amount
      finally:
         print("Process done")
   else:
      print("Invalid")
   contin= input("Do you want to continue: Yes or NO")
   if contin.upper()=="NO":
      break
         
      
