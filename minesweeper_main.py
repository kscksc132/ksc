import time
from minesweeper_board import Board


DIFFICULTIES = {
    "1": ("초급", 9,  9,  10),
    "2": ("중급", 16, 16, 40),
    "3": ("고급", 16, 30, 99),
}


def print_title():
    print("""
╔══════════════════════════════════════╗
║         💣  지뢰찾기 (Minesweeper)      ║
╚══════════════════════════════════════╝
""")


def select_difficulty():
    print("  난이도를 선택하세요:")
    for key, (name, rows, cols, mines) in DIFFICULTIES.items():
        print(f"  {key}. {name}  ({rows}×{cols}, 지뢰 {mines}개)")
    print()

    while True:
        choice = input("▶ 선택 (1~3): ").strip()
        if choice in DIFFICULTIES:
            return DIFFICULTIES[choice]
        print("  1~3 중 선택하세요.")


def parse_input(raw, rows, cols):
    """
    입력 형식:
      열 행        → 열기   (예: 3 5)
      f 열 행      → 깃발   (예: f 3 5)
    """
    parts = raw.strip().lower().split()
    try:
        if parts[0] == "f" and len(parts) == 3:
            c, r = int(parts[1]) - 1, int(parts[2]) - 1
            if 0 <= r < rows and 0 <= c < cols:
                return "flag", r, c
        elif len(parts) == 2:
            c, r = int(parts[0]) - 1, int(parts[1]) - 1
            if 0 <= r < rows and 0 <= c < cols:
                return "reveal", r, c
    except (ValueError, IndexError):
        pass
    return None, -1, -1


def format_time(seconds):
    m, s = divmod(int(seconds), 60)
    return f"{m:02d}:{s:02d}"


def main():
    print_title()

    name, rows, cols, mines = select_difficulty()
    board = Board(rows, cols, mines)

    print(f"\n  {name} 모드 시작! ({rows}×{cols}, 지뢰 {mines}개)")
    print("  입력 방법: [열 행] = 열기,  [f 열 행] = 깃발 표시")
    print("  예: '3 5' → 3열 5행 열기 / 'f 3 5' → 깃발 꽂기\n")

    start_time = None

    while not board.game_over:
        remaining = board.total_mines - board.flag_count()
        elapsed = format_time(time.time() - start_time) if start_time else "00:00"
        print(f"\n  💣 남은 지뢰: {remaining}  |  ⏱ {elapsed}")
        board.display()

        raw = input("\n▶ 입력: ").strip()
        if raw.lower() in ("q", "quit", "종료"):
            print("\n  게임을 종료합니다.")
            return

        action, r, c = parse_input(raw, rows, cols)

        if action is None:
            print(f"  잘못된 입력입니다. (열 1~{cols}, 행 1~{rows})")
            continue

        if start_time is None:
            start_time = time.time()

        if action == "reveal":
            if board.flagged[r][c]:
                print("  깃발이 꽂혀 있습니다. 먼저 깃발을 제거하세요.")
                continue
            board.reveal(r, c)

        elif action == "flag":
            board.toggle_flag(r, c)
            status = "꽂았습니다" if board.flagged[r][c] else "제거했습니다"
            print(f"  깃발을 {status}.")

    elapsed = format_time(time.time() - start_time) if start_time else "00:00"
    board.display(show_all=True)

    print(f"\n{'═'*42}")
    if board.won:
        print(f"  🎉 클리어! 모든 지뢰를 찾았습니다!")
    else:
        print(f"  💥 지뢰를 밟았습니다! 게임 오버")
    print(f"  경과 시간: {elapsed}  |  난이도: {name}")
    print(f"{'═'*42}\n")


if __name__ == "__main__":
    main()
