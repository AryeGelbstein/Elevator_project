import floor
from floor import *
from elevator import *


def calculate_time_by_distance(src, dest):
    distance = abs(src - dest)
    return (distance / FLOOR_HEIGHT) * ELEVATOR_TRAVEL_TIME_PER_FLOOR


class Building:

    def __init__(self, num_of_floors, num_of_elevators, world):
        self.floors = [Floor(i) for i in range(num_of_floors)]
        elevator_initial_y = world.get_height() - MARGIN - FLOOR_HEIGHT
        self.elevators = [Elevator(i, elevator_initial_y, self.elevator_arrived_at) for i in range(num_of_elevators)]
        self.num_of_floors = num_of_floors
        self.num_of_elevator = num_of_elevators
        self.world = world


    def draw(self):
        floor_image = pygame.image.load(FLOOR_IMAGE_PATH)
        floor_image = pygame.transform.scale(floor_image, (FLOOR_WIDTH, FLOOR_HEIGHT))
        elevator_image = pygame.image.load(ELEVATOR_IMAGE_PATH)
        elevator_image = pygame.transform.scale(elevator_image, (ELEVATOR_WIDTH, ELEVATOR_HEIGHT))

        canvas = self.world
        for floor_num in range(self.num_of_floors - 1):
            self.floors[floor_num].draw(floor_image, canvas)
        self.floors[-1].draw(floor_image, canvas, spacer_color=WHITE)
        for elevator in self.elevators:
            elevator.draw(elevator_image, canvas)


    def elevator_arrived_at(self, level):
        self.floors[level].button_pressed = False

    # def floor_under_treatment(self, dest_y):
    #     if any(dest_y in elevator.queue
    #            or dest_y == elevator.current_dest_y
    #            for elevator in self.elevators):
    #         return True

    def assign_elevator(self, floor):
        world_height = self.world.get_height()
        dest_y = world_height - (floor + 1) * FLOOR_HEIGHT - MARGIN

        best_arrival_time = float("inf")
        best_elevator = self.elevators[0]

        for elevator in self.elevators:
            src_y = elevator.y
            if elevator.queue:
                _, src_y = elevator.queue[-1]
            trip_time = calculate_time_by_distance(src_y, dest_y)
            arrival_time = elevator.time_when_free + trip_time
            if arrival_time < best_arrival_time:
                best_arrival_time = arrival_time
                best_elevator = elevator
        best_elevator.add_task(floor, dest_y, best_arrival_time + 2)


    def update(self, pos):
        if pos:
            for floor in self.floors:
                x, y = pos
                caller = floor.is_button_pressed(x, y)
                if caller is not None:
                    self.assign_elevator(caller)
        for elevator in self.elevators:
            elevator.update_location()
