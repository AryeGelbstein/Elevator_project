import pygame.mixer
from building import *


class Elevator:

    def __init__(self, num, initial_y, building_call_back_function):
        # Initializes an elevator object.
        # Each elevator has a unique number, position, destination tracking, and a queue for floor requests.
        # It also maintains status flags like busy state and timing information.

        self.num = num
        self.queue = []
        self.y = initial_y
        self.current_dest_y = None
        self.current_dest_floor = 0
        self.busy = False
        self.last_update = 0
        self.wait_start_time = 0
        self.time_when_free = 0.0
        self.building_call_back_function = building_call_back_function


    def add_task(self, floor, dest_y, finish_time):
        # Adds a floor request to the elevator's queue.
        # Updates the estimated time when the elevator will be free.

        self.queue.append((floor, dest_y))
        self.time_when_free = finish_time

    def get_next_task(self):
        # Retrieves the next destination from the elevator's queue.
        # Updates the elevator's current destination and marks it as busy.

        if not self.busy and self.queue:
            self.current_dest_floor, self.current_dest_y = self.queue.pop(0)
            self.busy = True
            self.last_update = pygame.time.get_ticks() # current timestamp in ms

    def arrived(self):
        # Handles elevator arrival at the destination floor.
        # Plays a sound, records the arrival time, and notifies the building to update the floor state.

        pygame.mixer.music.play()
        self.wait_start_time = pygame.time.get_ticks()
        self.building_call_back_function(self.current_dest_floor)


    def update_location(self):
        # Updates the elevator's position based on its destination.
        # Moves the elevator step-by-step toward the target floor, handles arrival logic, and manages waiting times.
        # If the elevator has completed its task, it retrieves the next request from the queue.

        self.time_when_free = max(self.time_when_free, pygame.time.get_ticks() / 1000)
        if self.busy:
            dest = self.current_dest_y
            y = self.y
            if y != dest:
                current_time = pygame.time.get_ticks() # current timestamp in ms
                elapsed_time = current_time - self.last_update
                travel_distance = round((elapsed_time * PIXELS_PER_SECOND) / 1000) # converting from ms to seconds
                direction = 1 if y < dest else -1
                self.y += direction * min(travel_distance, abs(y - dest))
                self.last_update = current_time
            elif self.wait_start_time == 0:
                self.arrived()
            else:
                current_time = pygame.time.get_ticks() # current timestamp in ms
                elapsed_wait_time = current_time - self.wait_start_time
                if elapsed_wait_time / 1000 >= ELEVATOR_STOPPING_TIME_AT_FLOOR:
                    self.busy = False
                    self.wait_start_time = 0
        self.get_next_task()


    def draw(self, image, screen):
        # Draws the elevator on the screen at its current position.
        # Uses the assigned elevator image and places it based on its current coordinates.

        top_left = (ELEVATOR_START_X + (ELEVATOR_SPACER + ELEVATOR_WIDTH) * self.num, self.y)
        screen.blit(image, top_left)
