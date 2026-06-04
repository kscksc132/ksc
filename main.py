from entities import Player, Monster
from battle import run_battle


def print_title():
    print("""
╔══════════════════════════════════════╗
║        ⚔  텍스트 RPG 미니게임  ⚔       ║
║   몬스터를 처치하고 최강이 되어라!       ║
╚══════════════════════════════════════╝
""")


def main():
    print_title()

    name = input("용사의 이름을 입력하세요: ").strip() or "용사"
    player = Player(name)

    print(f"\n어서오세요, {player.name}! 모험을 시작합니다.\n")

    stage = 1
    wins = 0

    while player.is_alive():
        print(f"\n{'─'*40}")
        print(f"  STAGE {stage}  |  처치 수: {wins}  |  Lv.{player.level}")
        print(f"{'─'*40}")

        monster = Monster(level=player.level)
        result = run_battle(player, monster)

        if result == "win":
            wins += 1
            stage += 1
            print(f"\n다음 스테이지로 이동합니다...")

            cont = input("\n계속하시겠습니까? (y/n): ").strip().lower()
            if cont != "y":
                break

        elif result == "escape":
            print("  도망에 성공했지만... 이대로 끝낼 수 없다!")
            cont = input("다시 도전하시겠습니까? (y/n): ").strip().lower()
            if cont != "y":
                break

        elif result == "lose":
            print(f"\n{'═'*40}")
            print(f"  {player.name}은(는) 쓰러졌다...")
            print(f"{'═'*40}")
            break

    print(f"\n{'═'*40}")
    print(f"  게임 종료!")
    print(f"  최종 레벨: Lv.{player.level}")
    print(f"  처치한 몬스터: {wins}마리")
    print(f"{'═'*40}")


if __name__ == "__main__":
    main()
