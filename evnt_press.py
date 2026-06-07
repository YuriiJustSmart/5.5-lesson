import pygame

# Ініціалізація Pygame
pygame.init()

# Налаштування екрана
WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")
font = pygame.font.SysFont(None, 36)
key_text = font.render("", True, (0, 0, 0))
WHITE = (255, 255, 255)
key = ""
running = True
while running:
    current_time = pygame.time.get_ticks()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                key = "A"
            elif event.key == pygame.K_s:
                key = "S"
            elif event.key == pygame.K_d:
                key = "D"
            elif event.key == pygame.K_w:
                key = "W"
            elif event.key == pygame.K_SPACE:
                key = "SPACE"
            elif event.key == pygame.K_LSHIFT:
                key = "LSHIFT"
            elif event.key == pygame.K_RSHIFT:
                key = "RSHIFT"
        elif event.type == pygame.KEYUP:
            key = ""

    key_text = font.render(f"{key}", True, (0, 0, 0))
    key_text_rect = key_text.get_rect(topright=(WIDTH - 10, HEIGHT // 2))
    screen.fill(WHITE)

    screen.blit(key_text, key_text_rect)
    pygame.display.flip()

pygame.quit()