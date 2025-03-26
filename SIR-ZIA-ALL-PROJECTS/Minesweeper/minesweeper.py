import random

class Minesweeper:
    def __init__(self, size=5, mines=3):
        self.size = size
        self.mines = mines
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.mine_positions = set()
        self.revealed = set()
        self._place_mines()

    def _place_mines(self):
        while len(self.mine_positions) < self.mines:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            self.mine_positions.add((x, y))

    def _count_adjacent_mines(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if (dx or dy) and (x+dx, y+dy) in self.mine_positions:
                    count += 1
        return count

    def reveal(self, x, y):
        if (x, y) in self.mine_positions:
            return False  # Hit a mine!
        
        self._reveal_cells(x, y)
        return True

    def _reveal_cells(self, x, y):
        if (x, y) in self.revealed or not (0 <= x < self.size and 0 <= y < self.size):
            return
        self.revealed.add((x, y))
        count = self._count_adjacent_mines(x, y)
        self.board[x][y] = str(count) if count > 0 else '.'

        if count == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx or dy:
                        self._reveal_cells(x + dx, y + dy)

    def display(self):
        print("\n   " + " ".join(str(i) for i in range(self.size)))
        for i, row in enumerate(self.board):
            print(f"{i} | {' '.join(row)} |")

    def is_win(self):
        return len(self.revealed) == self.size * self.size - self.mines

def play():
    game = Minesweeper()
    while True:
        game.display()
        try:
            x, y = map(int, input("Enter row and column (e.g., 1 2): ").split())
            if not game.reveal(x, y):
                print("\n💥 BOOM! You hit a mine. Game Over!")
                break
            if game.is_win():
                print("\n🎉 You Win! All safe cells revealed.")
                break
        except (ValueError, IndexError):
            print("Invalid input! Enter two numbers separated by space.")

play()
