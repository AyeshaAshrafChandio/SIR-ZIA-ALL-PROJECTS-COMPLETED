import pygame
import socket

# Connect to server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("SERVER_IP", 5555))  # Replace SERVER_IP with server's IP

# Get player ID (0 = left paddle, 1 = right paddle)
player = int(client.recv(1024).decode())

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Online Pong")

# Game objects
paddle_pos = 250
ball_pos = [300, 200]

def draw_game():
    screen.fill((0, 0, 0))
    
    # Draw paddles
    if player == 0:
        pygame.draw.rect(screen, (255, 0, 0), (20, paddle_pos - 50, 10, 100))
        pygame.draw.rect(screen, (0, 0, 255), (570, int(ball_pos[1]) - 50, 10, 100))
    else:
        pygame.draw.rect(screen, (0, 0, 255), (570, paddle_pos - 50, 10, 100))
        pygame.draw.rect(screen, (255, 0, 0), (20, int(ball_pos[1]) - 50, 10, 100))
    
    # Draw ball
    pygame.draw.circle(screen, (255, 255, 255), (int(ball_pos[0]), int(ball_pos[1])), 10)
    
    pygame.display.update()

def main():
    global paddle_pos, ball_pos
    
    clock = pygame.time.Clock()
    running = True
    
    while running:
        clock.tick(60)
        
        # Handle input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if player == 0:
            if keys[pygame.K_w] and paddle_pos > 50:
                paddle_pos -= 5
            if keys[pygame.K_s] and paddle_pos < 350:
                paddle_pos += 5
        else:
            if keys[pygame.K_UP] and paddle_pos > 50:
                paddle_pos -= 5
            if keys[pygame.K_DOWN] and paddle_pos < 350:
                paddle_pos += 5
        
        # Send paddle position to server
        client.send(str(paddle_pos).encode())
        
        # Receive game state from server
        data = client.recv(1024).decode()
        if not data:
            break
        
        # Update game state
        parts = data.split(",")
        if player == 0:
            ball_pos = [float(parts[2]), float(parts[3])]
        else:
            ball_pos = [float(parts[2]), float(parts[3])]
        
        draw_game()
    
    client.close()
    pygame.quit()

if __name__ == "__main__":
    main()