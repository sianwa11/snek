from entity import Entity
import pygame

class Food(Entity):
    def __init__(self, x, y, grid_size):
        super().__init__(x, y, grid_size)
    
    def draw(self, screen):
        center_x = self.x + self.grid_size // 2
        center_y = self.y + self.grid_size // 2
        radius = self.grid_size // 4 # Quarter of grid size
        
        pygame.draw.circle(screen, "green", (center_x, center_y), radius)
    
    def collide(self, other):
        return self.x == other.x and self.y == other.y