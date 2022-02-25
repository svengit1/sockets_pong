import pygame
class Player:
    def __init__(self, x, y, color, id):
        self.id = id
        self.x = x
        self.y = y
        self.color = color
        self.speed = 5
        self.width = 50
        self.height = 150
        self.points = 0
        self.detected_score = False

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
    
    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
    
    def increment_score(self):
        self.points += 1
