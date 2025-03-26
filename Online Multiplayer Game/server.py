import socket
import threading

# Server setup
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))
server.listen()

# Game state
players = {}
player_id = 0
ball_pos = [300, 200]
paddle_pos = {0: 250, 1: 250}  # Player 0 (left), Player 1 (right)

def handle_client(conn, addr, player):
    global ball_pos
    print(f"Player {player} connected")
    
    # Send initial player ID
    conn.send(str(player).encode())
    
    while True:
        try:
            # Receive paddle position from client
            data = conn.recv(1024).decode()
            if not data:
                break
            
            # Update paddle position
            paddle_pos[player] = int(data)
            
            # Send game state to client
            game_state = f"{paddle_pos[0]},{paddle_pos[1]},{ball_pos[0]},{ball_pos[1]}"
            conn.send(game_state.encode())
            
        except:
            break
    
    print(f"Player {player} disconnected")
    conn.close()

def game_loop():
    global ball_pos
    ball_speed = [3, 3]
    
    while True:
        # Update ball position
        ball_pos[0] += ball_speed[0]
        ball_pos[1] += ball_speed[1]
        
        # Ball collision with top/bottom
        if ball_pos[1] <= 0 or ball_pos[1] >= 400:
            ball_speed[1] *= -1
        
        # Ball collision with paddles
        if (ball_pos[0] <= 30 and abs(ball_pos[1] - paddle_pos[0]) < 50) or \
           (ball_pos[0] >= 570 and abs(ball_pos[1] - paddle_pos[1]) < 50):
            ball_speed[0] *= -1
        
        # Reset ball if out of bounds
        if ball_pos[0] < 0 or ball_pos[0] > 600:
            ball_pos = [300, 200]

if __name__ == "__main__":
    print("Server started. Waiting for connections...")
    threading.Thread(target=game_loop).start()
    
    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr, player_id)).start()
        player_id += 1