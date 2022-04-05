import random
from num2words import num2words

class Elevator(object):
    def __init__(self):
        self.top_floor = random.randint(1, 10)
        self.capacity = 5
        self.free_space = self.capacity
        self.destination = 2
        self.direction = 'Up'
        
class Floor(object):
    def __init__(self):
        self.passangers_number_wating = int
        self.destination_list = []
    def set_floor(self, max_floor):
        self.passangers_number_wating = random.randint(0, 10)
        self.destination_list = [random.randint(1, max_floor) for i in range(self.passangers_number_wating)]
        return self

elevator_status = Elevator()

def set_building():
    for i in range(elevator_status.top_floor):
        locals()[num2words(i)] = Floor()
        locals()[num2words(i)].set_floor(elevator_status.top_floor)
        print(locals()[num2words(i)].destination_list)
        
set_building()