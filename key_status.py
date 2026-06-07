import pygame

pygame.init()

screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# Colors
YELLOW = (253, 253, 150)
GREEN = (5, 244, 120)

# Initial coordinates of the square
x, y = 300, 200
width, height = 50, 50
speed = 5  # Speed of the square movement

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Getting the state of the keys
    keys = pygame.key.get_pressed()

    # Movement of the square
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += speed

    # Screen cleaning
    screen.fill(YELLOW)

    # Draw a square
    pygame.draw.rect(screen, GREEN, (x, y, width, height))

    # Screen refresh
    pygame.display.update()

    # Frames per second
    clock.tick(60)
