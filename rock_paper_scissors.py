import random


def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])


def decide(player: str, computer: str) -> str:
    if player == computer:
        return "draw"
    wins = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }
    return "win" if wins[player] == computer else "lose"


def main():
    print("가위(scissors)/바위(rock)/보(paper) — 가위바위보 게임")
    rounds = 3
    try:
        rounds_input = input("몇 라운드로 하시겠습니까? (기본 3): ").strip()
        if rounds_input:
            rounds = max(1, int(rounds_input))
    except ValueError:
        print("잘못된 입력입니다. 기본 3 라운드로 진행합니다.")

    player_score = 0
    comp_score = 0

    for r in range(1, rounds + 1):
        print(f"\n라운드 {r}/{rounds}")
        while True:
            player = input("선택(rock/paper/scissors): ").strip().lower()
            if player in ("rock", "paper", "scissors"):
                break
            print("올바른 선택을 입력하세요: rock, paper, scissors")

        computer = get_computer_choice()
        print(f"컴퓨터: {computer}")
        result = decide(player, computer)
        if result == "win":
            print("당신이 이겼습니다!")
            player_score += 1
        elif result == "lose":
            print("컴퓨터가 이겼습니다.")
            comp_score += 1
        else:
            print("무승부입니다.")

    print(f"\n최종 점수 — 당신: {player_score}, 컴퓨터: {comp_score}")
    if player_score > comp_score:
        print("최종 승리: 당신 🎉")
    elif player_score < comp_score:
        print("최종 승리: 컴퓨터 🤖")
    else:
        print("최종 결과: 무승부")


if __name__ == '__main__':
    main()
