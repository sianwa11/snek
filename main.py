import pygame
from snek import Snek
from food import Food

pygame.init()

SCREEN_HEIGHT = 700
SCREEN_WIDTH = 700
GRID_SIZE = 50

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

snek = Snek(50, 350, GRID_SIZE)
food = Food(300, 300, GRID_SIZE)

clock = pygame.time.Clock()
dt = 0

running = True
times = 0

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
    # Keys now change DIRECTION, not position
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        snek.change_direction(-1, 0)
      if event.key == pygame.K_RIGHT:
        snek.change_direction(1, 0)
      if event.key == pygame.K_UP:
        snek.change_direction(0, -1)
      if event.key == pygame.K_DOWN:
        snek.change_direction(0, 1)


  # Update the snake
  snek.update(dt)

  if snek.collide(food):
    times += 1
    print(f"Snek ate the food! Times eaten: {times}")


  screen.fill("black")

  for row in range(0, SCREEN_WIDTH // 50):
    for column in range(0, SCREEN_HEIGHT// 50):
      x = column * 50
      y = row * 50
      pygame.draw.rect(screen, "white", pygame.Rect(x, y, 50, 50), 1)

  # Draw the snake
  snek.draw(screen)
  # Draw the food
  food.draw(screen)

  pygame.display.flip()
  dt = clock.tick(60) / 1000

pygame.quit()