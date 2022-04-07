import random

class Elevator(object):
    def __init__(self):
        self.current_floor = 1
        self.max_floor = random.randint(1, 20)
        self.capacity = 5
        self.free_space = self.capacity
        self.destination = 2
        self.direction = 'Up'
    def set_current_floor(self, floor):
        self.current_floor = floor
    def set_direction(self, str):
        self.direction = str
        
        
        
# checking passangers leaving elevator
elevator_status = Elevator()


passanger_in_elevator = [4,5,6,7,1,3,7,5]
current_floor = 5
def passanger_out(passanger_in_elevator, current_floor):
    passanger_in_elevator_update = []
    for i in passanger_in_elevator:
        if i != current_floor:
            passanger_in_elevator_update.append(i)
    return passanger_in_elevator_update
print(passanger_out(passanger_in_elevator, current_floor))

# checking passangers enetering elevator
passanger_in_elevator = [1]
passanger_going_up = [2]
def passanger_in(passanger_in_elevator, passanger_going_up):
    passanger_in_elevator_update = []
    passanger_in_elevator.extend(passanger_going_up)
    for i in range(5):
        try:
            passanger_in_elevator_update.append(passanger_in_elevator[i])
        except IndexError:
            pass
    return passanger_in_elevator_update

print(passanger_in(passanger_in_elevator, passanger_going_up))

destination_list = [5] # [1, 3, 5, 7, 8, 2, 4, 6, 8]
current_floor = 5
dawn_list = []
up_list = []
def up_or_down(destination_list, current_floor):
    print(destination_list)        
    if current_floor in destination_list:
        destination_list = sorted(passanger_out(destination_list, current_floor))
    else:
        destination_list = sorted(destination_list)
    print(destination_list)
    dawn_list = [x for x in destination_list if x < current_floor]
    print(dawn_list)
    up_list = [x for x in destination_list if x > current_floor]
    print(up_list)
    if len(dawn_list) > len(up_list):
        elevator_status.set_direction('Down')
    elif len(dawn_list) < len(up_list):
        elevator_status.set_direction('Up')
    else:
        if destination_list:
            if current_floor - min(dawn_list) >  max(up_list) - current_floor:
                print('down')
                elevator_status.set_direction('Down')
            else:
                elevator_status.set_direction('Up')
                print('UP')
        else:
            print('NO passangers')    
    return elevator_status.direction
print(up_or_down(destination_list, current_floor))
