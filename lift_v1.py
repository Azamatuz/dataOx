import random
from num2words import num2words

class Elevator(object):
    def __init__(self):
        self.top_floor = random.randint(5, 10)
        self.current_floor = 1
        self.capacity = 5
        self.free_space = self.capacity
        self.destination = 2
        self.direction = 'Up'
        
class Floor(object):
    def __init__(self):
        self.passangers_number_wating = int
        self.destination_list = []
    def set_floor(self, max_floor, current_floor):
        
        self.passangers_number_wating = random.randint(0, 10)
        self.destination_list = [i for i in [random.randint(1, max_floor) for i in range(self.passangers_number_wating)] if i not in current_floor]
        return self

        


elevator_status = Elevator()
floor_init = Floor()


    

def up_direction(top_floor):
    floor = 0
    while floor <= top_floor:
        yield floor
        floor += 1
        
up_floor = up_direction(elevator_status.top_floor)




#while elevator_status.current_floor <= elevator_status.top_floor:
 #   print(locals()[num2words(next(up_floor))].destination_list)
print('Top Floor', elevator_status.top_floor)
for i in range(elevator_status.top_floor):
    locals()[num2words(i)] = Floor()
    locals()[num2words(i)].set_floor(elevator_status.top_floor, elevator_status.current_floor)
    print(locals()[num2words(i)].destination_list)
    
while elevator_status.current_floor <= elevator_status.top_floor:
    print('Current floor is ', elevator_status.current_floor)
    print(locals()[num2words(next(up_floor))].destination_list)
    elevator_status.current_floor +=1