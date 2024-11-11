# Part 1 (Basic Functions)
# 1. Hello function
def sayhello():
    print('Hello, Python!')

sayhello()

#2. Square a number
def square(num):
    return num**2

print(square(5))

# 3. Area of a rectangle
def calculate_area(length, width):
    return length*width

print(calculate_area(5,3))

# Part 2: Intermediate Functions
# 4. Temperature converter
def convert_temp(value, to_unit='C'):
    if to_unit=='F' or to_unit=='f':
        return (value*9/5)+32
    else:
        return (value-32)*5/9

print(convert_temp(100,'F'))
print(convert_temp(32))

# 5. Recursive factorial
import math
def factorialrecursive(num):
    return math.factorial(num)

print(factorialrecursive(5))

# 6. Maximum of three
def find_max(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    else:
        return 'All numbers are identical'

print(find_max(3,7,5))

# Part 3: Advanced functions
# 7. Matrix addition
def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print('not the same size')
    # I had help with this one \/
    result = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]
    
    return result

matrix3 = [[1, 2], [3, 4]]
matrix4 = [[5, 6], [7, 8]]
print(add_matrices(matrix3, matrix4))

# 8. Prime checker
def is_prime(number):
    if number <= 1:
        return False
    # Had help with this one \/
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


print(is_prime(10))
print(is_prime(12))

# 9. Quadratic solver
# I had a lot of help involving multiple websites
def solve_quadratic(a, b, c):
    discriminant=b**2 - 4*a*c
    
    if discriminant>0:
        root1=(-b+math.sqrt(discriminant)) / (2 * a)
        root2=(-b-math.sqrt(discriminant)) / (2 * a)
        return (root1, root2)
    
    elif discriminant==0:
        root=-b/(2*a)
        return (root,)
    
    else:
        realPart=-b/(2 * a)
        imaginaryPart=math.sqrt(-discriminant)/(2 * a)
        return (complex(realPart, imaginaryPart), complex(realPart,-imaginaryPart))


print(solve_quadratic(1, -3, 2))
print(solve_quadratic(1, 2, 5))

'''
We have already done the challenge problems in previous lessons
'''
