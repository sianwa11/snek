import pygame

pygame.init()

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 700
GRID_SIZE = 50

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

snek_x = 50
snek_y = 350

direction_x = 1  
direction_y = 0  

# Timer for automatic movement
move_timer = 0
move_delay = 300  # milliseconds between moves (adjust for speed)

clock = pygame.time.Clock()
dt = 0

running = True

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
    # Keys now change DIRECTION, not position
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        direction_x = -1
        direction_y = 0
      if event.key == pygame.K_RIGHT:
        direction_x = 1
        direction_y = 0
      if event.key == pygame.K_UP:
        direction_x = 0
        direction_y = -1
      if event.key == pygame.K_DOWN:
        direction_x = 0
        direction_y = 1

  # Automatic movement based on timer
  move_timer += dt * 1000  # Convert dt to milliseconds
  if move_timer >= move_delay:
    snek_x += direction_x * GRID_SIZE
    snek_y += direction_y * GRID_SIZE
    move_timer = 0  # Reset timer

  screen.fill("black")

  for row in range(0, SCREEN_WIDTH // 50):
    for column in range(0, SCREEN_HEIGHT// 50):
      x = column * 50
      y = row * 50
      pygame.draw.rect(screen, "white", pygame.Rect(x, y, 50, 50), 1)

  # Draw the snake
  pygame.draw.rect(screen, "red", pygame.Rect(snek_x, snek_y, GRID_SIZE, GRID_SIZE))

  pygame.display.flip()
  dt = clock.tick(60) / 1000

pygame.quit()