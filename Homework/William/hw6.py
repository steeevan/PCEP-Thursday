def say_hello():
    print("HEllo")
say_hello()

def square(num):
    return num*num
square(5)

def rectangle(l,w):
    return l*w
rectangle(2,3)

def convert(temp,unit_to="c"):
    if unit_to=="f":
        return temp*1.8+32
    elif unit_to=="c":
        return temp*0.8-32
convert(218)
convert(322,"f")

def fac(num):
    x=num
    for i in range(num-1):
        num-=1
        x=x*num
    return(x)
fac(5)

def find_max(*args):
    li=[]
    li.append(args)
    return max(li)
find_max(2,3,4,56)

def add_matrix(m1,m2):
    m3=m1+m2
    m4=m3[0]+m3[2]
    m5=m3[1]+m3[3]
    m8= [m4,m5]
    return 
print(add_matrix([[2,3],[2,4]],[[2,3],[4,5]]))
def prime(num):
    if num > 1:
    
        for i in range(2, (num//2)+1):
        

            if (num % i) == 0:
                print(num, "is not a prime number")
                break
        else:
            print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
prime(2)

def solve_quadratic(a, b, c):
    x=1
    return a*x**2 + b*x + c 
solve_quadratic(1,2,3)

def is_palindrome(a):
    b= a.reversed()
    if b==a:
        print("it is palindrone")
    else:
        print("It not")

def fibonacci():
    lis=[0]
    if len(lis)==1:
        lis.append(1)
        lis.append(1)
    for i in range(20):
        lis.append(lis[-1]+lis[-2])
    return(lis)
fibonacci()

def sort_num (lis=[1,3,2,4]):
    return sorted(lis)
sort_num()
