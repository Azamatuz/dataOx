from random import random


import random
floor_number = random.randint(0, 20)
passenger_number = random.randint(0, 7)
print(floor_number, passenger_number)

def up_button(floor_number):
    for n in range(floor_number):
        print(n+1)

def down_button(floor_number):
    for n in range(floor_number, 0, -1):
        print(n)
        
print('Up')       
up_button(floor_number)
print('Down')
down_button(floor_number)