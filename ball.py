import pygame
import random

class Ball:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rad = 10
        self.speed_x = random.choice[1, -1]
        self.speed_y = random.choice[1, -1]

    def draw(self, win):
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), self.rad)
    
    def move(self):
        self.x += round(self.speed_x)
        self.y += round(self.speed_y)

    def change_direction(self, direction):
        if direction == "x":
            self.speed_x *= -1
        else:
            self.speed_y *= -1
    
    def increment_speed(self):
        self.speed_x = (abs(self.speed_x) + 0.15) * (self.speed_x / abs(self.speed_x))
        self.speed_y = (abs(self.speed_y) + 0.15) * (self.speed_y / abs(self.speed_y))
    