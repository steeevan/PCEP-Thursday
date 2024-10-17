# part 1

city='New York'
temperature=100.5
population=18999
is_raining=False

print(type(city))
print(type(temperature))
print(type(population))
print(type(is_raining))
print()

# part 2 \/

price=float(input('Price of product: $'))
quantity=int(input('Quantity of product(s):'))

# BONUS \/

username=input("input customer name: ")

# part 2 contunued \/
print()
total_cost=price*quantity
if price>0 and quantity>0:
    print(f'Your total cost (int): ${int(total_cost)}')
    print(f'Your total cost (float): ${float(total_cost)}')
    print(f'Thank you visiting Walmart Online Delivery, {username}. Please come back to waste your money even more.')
else:
    print('not a valid number')
print()
# HW1 extended
# part 1
import random
animals=['parrot', 'capuchin monkey', 'sheep']
favanimals=['dog', 'monkey', 'gorilla', 'pig', 'cow']

def modify_list():

    print(favanimals)
    favanimals.append(random.choice(animals))
    print(favanimals)
    favanimals[1]=random.choice(animals)
    print(favanimals)
    favanimals.remove('cow')
    print(favanimals)

modify_list()

coordinates=(4, 5, 7)
print (coordinates)
(x, y, z)=coordinates
print(x, y, z)
print()
bookinfo={
    'title': 'Percy Jackson and the Lightning theif',
    'author': 'Rick Riordan',
    'year_published': 2003
}
print()
print(bookinfo)
bookinfo['genre']='fantasy fiction'
bookinfo['year_published']=2005
bookinfo.pop('author')
print(bookinfo)

numbers={0,4,13,7,9,5}
print(numbers)
numbers2={1,2,3}
morenumbers={10,20,30}
print()
numbers.add(6)
numbers.remove(0)
numbers.union(morenumbers)
numbers.intersection(numbers2)

print(numbers)
