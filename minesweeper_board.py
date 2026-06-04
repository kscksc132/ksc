import random


class Board:
    HIDDEN = "■"
    FLAG = "🚩"
    MINE = "💣"
    EMPTY = "  "
    NUMBERS = [" ", "1", "2", "3", "4", "5", "6", "7", "8"]

    def __init__(self, rows=9, cols=9, mines=10):
        self.rows = rows
        self.cols = cols
        self.total_mines = mines
        self.grid = [[0] * cols for _ in range(rows)]
        self.revealed = [[False] * cols for _ in range(rows)]
        self.flagged = [[False] * cols for _ in range(rows)]
        self.mines_set = set()
        self.game_over = False
        self.won = False
        self.first_click = True

    def place_mines(self, safe_r, safe_c):
        safe_zone = {(safe_r + dr, safe_c + dc)
                     for dr in range(-1, 2)
                     for dc in range(-1, 2)
                     if 0 <= safe_r + dr < self.rows and 0 <= safe_c + dc < self.cols}

        candidates = [(r, c) for r in range(self.rows)
                              for c in range(self.cols)
                              if (r, c) not in safe_zone]

        for r, c in random.sample(candidates, self.total_mines):
            self.mines_set.add((r, c))
            self.grid[r][c] = -1

        for r in range(self.rows):
            for c in range(self.cols):
                if self.grid[r][c] == -1:
                    continue
                self.grid[r][c] = sum(
                    1 for dr in range(-1, 2)
                      for dc in range(-1, 2)
                      if (r + dr, c + dc) in self.mines_set
                )

    def reveal(self, r, c):
        if not (0 <= r < self.rows and 0 <= c < self.cols):
            return
        if self.revealed[r][c] or self.flagged[r][c]:
            return

        if self.first_click:
            self.place_mines(r, c)
            self.first_click = False

        self.revealed[r][c] = True

        if self.grid[r][c] == -1:
            self.game_over = True
            return

        if self.grid[r][c] == 0:
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    self.reveal(r + dr, c + dc)

        self._check_win()

    def toggle_flag(self, r, c):
        if self.revealed[r][c]:
            return
        self.flagged[r][c] = not self.flagged[r][c]

    def _check_win(self):
        unrevealed = sum(
            1 for r in range(self.rows)
              for c in range(self.cols)
              if not self.revealed[r][c]
        )
        if unrevealed == self.total_mines:
            self.won = True
            self.game_over = True

    def flag_count(self):
        return sum(self.flagged[r][c] for r in range(self.rows) for c in range(self.cols))

    def display(self, show_all=False):
        col_header = "    " + "  ".join(f"{c+1:2}" for c in range(self.cols))
        print(col_header)
        print("   +" + "───" * self.cols + "+")

        for r in range(self.rows):
            row_str = f"{r+1:2} |"
            for c in range(self.cols):
                if show_all and (r, c) in self.mines_set:
                    cell = self.MINE
                elif self.flagged[r][c]:
                    cell = self.FLAG
                elif not self.revealed[r][c]:
                    cell = self.HIDDEN + " "
                elif self.grid[r][c] == 0:
                    cell = self.EMPTY + " "
                else:
                    num = self.grid[r][c]
                    colors = {1:"\033[34m", 2:"\033[32m", 3:"\033[31m",
                              4:"\033[35m", 5:"\033[33m", 6:"\033[36m",
                              7:"\033[37m", 8:"\033[90m"}
                    cell = f"{colors.get(num,'')}{num}\033[0m  "
                row_str += cell
            row_str += "|"
            print(row_str)

        print("   +" + "───" * self.cols + "+")
