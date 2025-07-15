import pygame
from entity import Entity

class Snek(Entity):
  def __init__(self, x, y, grid_size):
    super().__init__(x, y, grid_size)
    self.direction_x = 1 
    self.direction_y = 0 

    self.move_timer = 0
    self.move_delay = 300  # milliseconds between moves (adjust for speed)

  def update(self, dt):
    self.move_timer += dt * 1000
    if self.move_timer >= self.move_delay:

      new_x = self.x + self.direction_x * self.grid_size
      new_y = self.y + self.direction_y * self.grid_size

      if (new_x < 0 or new_x >= 700 or 
          new_y < 0 or new_y >= 700):
        return False

      self.x = new_x
      self.y = new_y
      self.move_timer = 0  # Reset timer
      return True

  def change_direction(self, direction_x, direction_y):
    self.direction_x = direction_x
    self.direction_y = direction_y

  def draw(self, screen):
    pygame.draw.rect(screen, "red", 
                     pygame.Rect(self.x, self.y, self.grid_size, self.grid_size))
    
 