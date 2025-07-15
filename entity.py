
class Entity:
  def __init__(self, x=0, y=0, grid_size=50):
    self.x = x
    self.y = y
    self.grid_size = grid_size

  def update(self, dt):
    pass

  def draw(self, screen):
    pass

  def collide(self, other):
    return self.x == other.x and self.y == other.y
