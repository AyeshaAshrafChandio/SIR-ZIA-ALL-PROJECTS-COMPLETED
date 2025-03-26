import pygame
import random

# Initialize pygame
pygame.init()

# Screen setup
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
GRID_WIDTH = SCREEN_WIDTH // BLOCK_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // BLOCK_SIZE
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Tetris")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
GRAY = (128, 128, 128)

# Tetromino shapes
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]]   # Z
]

# Colors for each shape
SHAPE_COLORS = [CYAN, YELLOW, MAGENTA, ORANGE, BLUE, GREEN, RED]

class Tetromino:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = SHAPE_COLORS[SHAPES.index(shape)]
        self.rotation = 0

def create_grid():
    return [[BLACK for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

def draw_grid(grid):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            pygame.draw.rect(screen, grid[y][x], 
                           (x * BLOCK_SIZE, y * BLOCK_SIZE, 
                            BLOCK_SIZE, BLOCK_SIZE), 0)
            pygame.draw.rect(screen, GRAY, 
                           (x * BLOCK_SIZE, y * BLOCK_SIZE, 
                            BLOCK_SIZE, BLOCK_SIZE), 1)

def draw_tetromino(tetromino):
    shape = tetromino.shape
    for y in range(len(shape)):
        for x in range(len(shape[0])):
            if shape[y][x]:
                pygame.draw.rect(screen, tetromino.color,
                               ((tetromino.x + x) * BLOCK_SIZE,
                                (tetromino.y + y) * BLOCK_SIZE,
                                BLOCK_SIZE, BLOCK_SIZE), 0)
                pygame.draw.rect(screen, WHITE,
                               ((tetromino.x + x) * BLOCK_SIZE,
                                (tetromino.y + y) * BLOCK_SIZE,
                                BLOCK_SIZE, BLOCK_SIZE), 1)

def valid_space(tetromino, grid):
    shape = tetromino.shape
    for y in range(len(shape)):
        for x in range(len(shape[0])):
            if shape[y][x]:
                if (tetromino.x + x < 0 or tetromino.x + x >= GRID_WIDTH or
                    tetromino.y + y >= GRID_HEIGHT or
                    grid[tetromino.y + y][tetromino.x + x] != BLACK):
                    return False
    return True

def lock_tetromino(tetromino, grid):
    shape = tetromino.shape
    for y in range(len(shape)):
        for x in range(len(shape[0])):
            if shape[y][x]:
                grid[tetromino.y + y][tetromino.x + x] = tetromino.color

def clear_rows(grid):
    full_rows = []
    for y in range(GRID_HEIGHT):
        if BLACK not in grid[y]:
            full_rows.append(y)
    
    for row in full_rows:
        del grid[row]
        grid.insert(0, [BLACK for _ in range(GRID_WIDTH)])

def get_new_tetromino():
    shape = random.choice(SHAPES)
    return Tetromino(GRID_WIDTH // 2 - len(shape[0]) // 2, 0, shape)

def main():
    grid = create_grid()
    current_tetromino = get_new_tetromino()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.5  # seconds per block

    running = True
    while running:
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current_tetromino.y += 1
            if not valid_space(current_tetromino, grid):
                current_tetromino.y -= 1
                lock_tetromino(current_tetromino, grid)
                clear_rows(grid)
                current_tetromino = get_new_tetromino()
                if not valid_space(current_tetromino, grid):
                    running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_tetromino.x -= 1
                    if not valid_space(current_tetromino, grid):
                        current_tetromino.x += 1
                
                if event.key == pygame.K_RIGHT:
                    current_tetromino.x += 1
                    if not valid_space(current_tetromino, grid):
                        current_tetromino.x -= 1
                
                if event.key == pygame.K_DOWN:
                    current_tetromino.y += 1
                    if not valid_space(current_tetromino, grid):
                        current_tetromino.y -= 1
                
                if event.key == pygame.K_UP:
                    rotated = list(zip(*current_tetromino.shape[::-1]))
                    old_shape = current_tetromino.shape
                    current_tetromino.shape = rotated
                    if not valid_space(current_tetromino, grid):
                        current_tetromino.shape = old_shape

        screen.fill(BLACK)
        draw_grid(grid)
        draw_tetromino(current_tetromino)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()