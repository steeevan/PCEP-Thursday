try:
    ipu= input("Enter a value")
    int_verson= int(ipu)
except Exception as e:
    print("There is a error of ", e)
else:
    print(f"The converted value : {int_verson}")

my_list = [10, 20, 30]
try:
    index= int(input("Enter a index "))
    item= my_list[index]
except Exception as e:
    print(f"There is a exeption of {e}")
else:
    print(f"Item found : {item}")

try:
    open("data.txt","a")
except Exception as e:
    print(f"There is a issue of {e}")
else:
    print("Read successfully")
finally:
    print("Operation Complete")


class NegativeNUm(Exception):
    if Exception < 0 :
        print("Negative number issue")

try :
    num=int(input("Inter a number above 0"))
    raise(NegativeNUm)
except Exception as e:
    print(f"There is a issue of {e}")
else:
    print(num)

try:
    de=int(input("Enter the denominator"))
    nu=int(input("Enter the numerator"))
    quotient= nu/de
except Exception as e :
    print(f"there is a error of {e}")
else:
    print(quotient)

my_lkst2=[]
while True:
    try:
        numa= int(input("Enter number"))
    except Exception:
        print("Stop")
        break
    else:
        my_lkst2.append(numa)

print(my_lkst2)
    
