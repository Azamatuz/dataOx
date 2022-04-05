import random

class Elevator(object):
    def __init__(self):
        self.current_floor = 1 # on start stage elevator strts from 1st floor
        self.max_floor = random.randint(5, 20)
        self.capacity = 5
        self.free_space = self.capacity
        self.destination = 2 # by default destination is the next floor
        self.direction = 'Up'
        self.passanger_in_elevator = []
    def set_direction(self, str):
        self.direction = str
        
class Passanger(object):
    def __init__(self, max_floor):
        self.passanger_waiting = random.randint(0, 10)
        if self.passanger_waiting > 0:
            self.destination_list = [random.randint(1, max_floor) for i in range(self.passanger_waiting)]
        else:
            self.destination_list = []

# function removes passangers from elevator
def passanger_out(passanger_in_elevator, current_floor):
    passanger_in_elevator_update = []
    for i in passanger_in_elevator:
        if i != current_floor:
            passanger_in_elevator_update.append(i)
    return passanger_in_elevator_update

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

# function update elevetor's direction Up or Down
def up_or_down(destination_list, current_floor):
    if current_floor in destination_list:
        destination_list = sorted(passanger_out(destination_list, current_floor))
    else:
        destination_list = sorted(destination_list)
    dawn_list = [x for x in destination_list if x < current_floor]
    up_list = [x for x in destination_list if x > current_floor]
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
            print('Wait, NO passangers on the floor')   
        
    return elevator_status.direction
    
def elevator_simulation(arument):
    switcher = {
        'Up': elevator_go_up(),
        'Dawn': elevator_go_dawn()
    }
    return switcher.get(arument, '')    

def elevator_go_up():
    while elevator_status.current_floor <= elevator_status.destination:
        
        #elevator arrives to a new floor(or start moving)
        print((elevator_status.current_floor == elevator_status.destination))
        passangers = Passanger(elevator_status.max_floor)
        print('Current Floor', elevator_status.current_floor)
        # passangers leave elevetor
        elevator_status.passanger_in_elevator = passanger_out(elevator_status.passanger_in_elevator, elevator_status.current_floor)
        #checks passangers on the floor waitng for an elevator( how many and what floor they want to go)
        print('Passanger number on the floor', passangers.passanger_waiting)
        print(passangers.destination_list)
        if passangers.passanger_waiting > 0:
            #selects only who goes up
            passanger_going_up = [x for x in passangers.destination_list if x > elevator_status.current_floor]
            print('Destination list', passanger_going_up)
            # passangers enter elevator(first come first in)
            elevator_status.passanger_in_elevator = passanger_in(elevator_status.passanger_in_elevator, passanger_going_up)
            print('Passangers in elevator', elevator_status.passanger_in_elevator)
            # checks avalible room for new passangers
            elevator_status.free_space = elevator_status.capacity - len(elevator_status.passanger_in_elevator)
            print('Free room after new passangers entered', elevator_status.free_space)
            if elevator_status.destination < max(passangers.destination_list):
                elevator_status.destination = max(passangers.destination_list)
            print('Destination floor',elevator_status.destination)
            # checkes if elevetor reached the last froor destination
            if elevator_status.current_floor == elevator_status.destination:
                print('Last Floor')
                up_or_down(passangers.destination_list, elevator_status.current_floor)
            else:
                # if its not a lst floor it goes up
                elevator_status.current_floor +=1
        else:
            print('No passangers')

def elevator_go_dawn():
    while elevator_status.current_floor >= elevator_status.destination:
        #elevator arrives to a new floor(or starts moving)
        print((elevator_status.current_floor == elevator_status.destination))
        passangers = Passanger(elevator_status.max_floor)
        print('Current Floor', elevator_status.current_floor)
        # passangers leave elevetor
        elevator_status.passanger_in_elevator = passanger_out(elevator_status.passanger_in_elevator, elevator_status.current_floor)
        #checks passangers on the floor waitng for an elevator( how many and what floor they want to go)
        print('Passanger number on the floor', passangers.passanger_waiting)
        #selects only who goes down
        passanger_going_down_list = [x for x in passangers.destination_list if x < elevator_status.current_floor]
        print('Destination list', passanger_going_down_list)
        # passangers enter elevator(first come firs in)
        elevator_status.passanger_in_elevator = passanger_in(elevator_status.passanger_in_elevator, passanger_going_down_list)
        print('Passangers in elevator', elevator_status.passanger_in_elevator)
        # checks avalible room for new passangers
        elevator_status.free_space = elevator_status.capacity - len(elevator_status.passanger_in_elevator)
        print('Free room after new passangers entered', elevator_status.free_space)
        # selects the lowest floor passanger wants to go as a elevator's final destination
        if elevator_status.destination > min(passangers.destination_list):
            elevator_status.destination = min(passangers.destination_list)
        print('Destination floor',elevator_status.destination)
         # checkes if elevetor reached the last froor destination
        if elevator_status.current_floor == elevator_status.destination:
            print('First Floor')
            up_or_down(passangers.destination_list, elevator_status.current_floor)
        else:
            elevator_status.current_floor -=1
            
elevator_status = Elevator()
passangers = Passanger(elevator_status.max_floor)

print('Max Floor', elevator_status.max_floor)

elevator_simulation(elevator_status.direction)