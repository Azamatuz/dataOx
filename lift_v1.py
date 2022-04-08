import random
from num2words import num2words

class Elevator(object):
    def __init__(self):
        self.top_floor = random.randint(5, 10)
        self.current_floor = 1
        self.capacity = 5
        self.free_space = self.capacity
        self.passangers_in_elevator = []
        self.destination = 2
        self.direction = 'Up'
        
class Floor(object):
    def __init__(self):
        self.passangers_number_wating = int
        self.destination_list = []
    def set_floor(self, max_floor, current_floor):
        self.current_floor_list = [current_floor]
        self.passangers_number_wating = random.randint(0, 10)
        self.destination_list = [i for i in [random.randint(1, max_floor) for i in range(self.passangers_number_wating)] if i not in current_floor]
        return self

# function add passangers to elevetor
def passanger_in(passanger_in_elevator, passanger_on_floor):
    passanger_in_elevator_update = []
    passanger_in_elevator.extend(passanger_on_floor)
    for i in range(5):
        try:
            passanger_in_elevator_update.append(passanger_in_elevator[i])
        except IndexError:
            passanger_in_elevator_update
    return passanger_in_elevator_update

# passangers ready to go up or down
def up_down_lists(destination_list, current_floor):
    up_list = []
    down_list = []
    for iindex, value in enumerate(destination_list):
        if value < current_floor:
            down_list.append(value)
        else:
            up_list.append(value)
    return up_list, down_list

elevator_status = Elevator()
floor_init = Floor()


    

def up_direction(top_floor):
    floor = 0
    while floor <= top_floor:
        yield floor
        floor += 1

def down_direction(top_floor):
    floor = top_floor
    while 1 >= top_floor:
        yield floor
        floor -= 1
        
up_floor = up_direction(elevator_status.top_floor)

print('Top Floor', elevator_status.top_floor)
for i in range(elevator_status.top_floor):
    locals()[num2words(i)] = Floor()
    ignor_floor = [i+1]
    locals()[num2words(i)].set_floor(elevator_status.top_floor, ignor_floor)
    print(i+1, locals()[num2words(i)].destination_list)
    
while elevator_status.current_floor <= elevator_status.top_floor:
    print('Current floor is ', elevator_status.current_floor)
    up_list, down_list = up_down_lists(locals()[num2words(next(up_floor))].destination_list, elevator_status.current_floor)
    elevator_status.passangers_in_elevator = passanger_in(elevator_status.passangers_in_elevator, up_list)
    print('Waiting', locals()[num2words(next(up_floor))].destination_list)
    print('In Elevator', elevator_status.passangers_in_elevator )
    elevator_status.current_floor +=1