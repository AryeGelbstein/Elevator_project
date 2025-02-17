import pygame.mixer
from building import *


class Elevator:

    def __init__(self, num, initial_y, building_call_back_function):
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


    def add_task(self, floor, dest_y, finnish_time):
        self.queue.append((floor, dest_y))
        self.time_when_free = finnish_time

    def get_next_task(self):
        if not self.busy and self.queue:
            self.current_dest_floor, self.current_dest_y = self.queue.pop(0)
            self.busy = True
            self.last_update = pygame.time.get_ticks() # current timestamp in ms

    def arrived(self):
        pygame.mixer.music.play()
        self.wait_start_time = pygame.time.get_ticks()
        self.building_call_back_function(self.current_dest_floor)


    def update_location(self):
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
                if elapsed_wait_time >= ELEVATOR_STOPPING_TIME_AT_FLOOR:
                    self.busy = False
                    self.wait_start_time = 0
        self.get_next_task()


    def draw(self, image, screen):
        top_left = (ELEVATOR_START_X + (ELEVATOR_SPACER + ELEVATOR_WIDTH) * self.num, self.y)
        screen.blit(image, top_left)
