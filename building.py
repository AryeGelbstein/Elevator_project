import floor
from floor import *
from elevator import *


def calculate_time_by_distance(src, dest):
    # Calculates the estimated travel time for an elevator between two floors.
    # The time is based on the absolute distance between floors, the floor height, and the elevator's speed per floor.

    distance = abs(src - dest)
    return (distance / FLOOR_HEIGHT) * ELEVATOR_TRAVEL_TIME_PER_FLOOR


class Building:

    def __init__(self, num_of_floors, num_of_elevators, world):
        # Represents a building with multiple floors and elevators.
        # Initializes the floors and elevators, setting their initial positions within the given world.

        self.floors = [Floor(i) for i in range(num_of_floors)]
        elevator_initial_y = world.get_height() - MARGIN - FLOOR_HEIGHT
        self.elevators = [Elevator(i, elevator_initial_y, self.elevator_arrived_at) for i in range(num_of_elevators)]
        self.num_of_floors = num_of_floors
        self.num_of_elevator = num_of_elevators
        self.world = world


    def draw(self):
        # Draws the building, including all floors and elevators.
        # Loads floor and elevator images, scales them, and renders them on the screen.

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
        # Marks the elevator arrival at a specific floor.
        # Resets the button press state for the given floor.

        self.floors[level].button_pressed = False


    def assign_elevator(self, floor):
        # Assigns the best available elevator to a requested floor.
        # Calculates the estimated arrival time for each elevator and selects the one with the shortest time.

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
        best_elevator.add_task(floor, dest_y, best_arrival_time + ELEVATOR_STOPPING_TIME_AT_FLOOR)


    def update(self, pos):
        # Updates the state of the building based on user input and elevator movements.
        # Checks if a floor button was pressed and assigns an elevator accordingly.
        # Updates the location of all elevators in the building.

        if pos:
            for floor in self.floors:
                x, y = pos
                caller = floor.is_button_pressed(x, y)
                if caller is not None:
                    self.assign_elevator(caller)
        for elevator in self.elevators:
            elevator.update_location()
