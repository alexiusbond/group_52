fruits = ['apple', 'orange', 'strawberry']
animals = ['dog', 'cat', 'elephant', 'cow', 'rabbit']

for fruit in fruits:
    print(fruit)

for animal in animals:
    print(animal)
# O (F + A)

for animal in animals:
    for fruit in fruits:
        print(f'{animal} loves {fruit}')
# O (A * F)

a = len(fruits)
while a > 0:
    for animal in animals:
        print('hello')
    for fruit in fruits:
        print(fruit)
    a -= 1
# O F * (A + F) => F * A + F ** 2

def counter(num):
    print(num)
    if num > 0:
        counter(num - 1)

counter(3)