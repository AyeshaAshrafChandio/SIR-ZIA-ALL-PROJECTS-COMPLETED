import pygame
import random

# Initialize pygame
pygame.init()

# Game screen
WIDTH, HEIGHT = 600, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Player settings
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - 70
player_speed = 5

# Enemy settings
enemy_size = 40
enemy_x = random.randint(0, WIDTH - enemy_size)
enemy_y = 50
enemy_speed = 2

# Bullet settings
bullet_width, bullet_height = 5, 15
bullet_x, bullet_y = -10, -10  # Start off-screen
bullet_speed = 5
bullet_active = False

# Game loop
running = True
while running:
    pygame.time.delay(20)
    screen.fill(WHITE)

    # Events handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Bullet shooting
    if keys[pygame.K_SPACE] and not bullet_active:
        bullet_x = player_x + player_size // 2 - bullet_width // 2
        bullet_y = player_y
        bullet_active = True

    # Bullet movement
    if bullet_active:
        bullet_y -= bullet_speed
        if bullet_y < 0:
            bullet_active = False

    # Enemy movement
    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = 50
        enemy_x = random.randint(0, WIDTH - enemy_size)

    # Collision detection
    if bullet_active and enemy_x < bullet_x < enemy_x + enemy_size and enemy_y < bullet_y < enemy_y + enemy_size:
        enemy_y = 50
        enemy_x = random.randint(0, WIDTH - enemy_size)
        bullet_active = False

    # Draw player, enemy, and bullet
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_size, enemy_size))
    if bullet_active:
        pygame.draw.rect(screen, RED, (bullet_x, bullet_y, bullet_width, bullet_height))

    pygame.display.update()

pygame.quit()
