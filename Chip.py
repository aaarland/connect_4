from dis import dis
from turtle import width
import pygame

class Chip:
    def __init__(self, display_surf, x, y, color, ball_width) -> None:
        self.x = x
        self.y = y
        self.display_surf = display_surf
        self.color = color
        self.x_direction = 1
        self.y_direction = 1
        self.width = ball_width
        
        pass

    def _set_direction(self, x, y):
        w, h = pygame.display.get_surface().get_size()
        new_x = self.x + (x + self.width * self.x_direction)
        new_y = self.y + (y + self.width * self.y_direction)
        if  new_x >= w:
            self.x_direction = -1
        if new_x <= 0:
            self.x_direction = 1
        
        if new_y >= h:
            self.y_direction = -1
        if new_y <= 0:
            self.y_direction = 1
        self.x = self.x + (x * self.x_direction)
        self.y = self.y + (y * self.y_direction)

    def move(self, x, y):
        self._set_direction(x, y)
        
    
    def draw(self):
        self._circle_surf = pygame.draw.circle(self.display_surf, self.color,  (self.x, self.y), self.width)


