import random
import time


def player_turn(player, monster):
    print("\n─── 행동 선택 ───")
    print("  1. 공격")
    print("  2. 강공격 (데미지 x1.8, 50% 확률로 빗나감)")
    print("  3. 회복 (HP 25 회복)")
    print("  4. 도망")

    while True:
        choice = input("▶ 선택: ").strip()
        if choice in ("1", "2", "3", "4"):
            break
        print("  1~4 중 선택하세요.")

    if choice == "1":
        dmg = player.attack + random.randint(-3, 3)
        dealt = monster.take_damage(dmg)
        print(f"  {player.name}의 공격! → {monster.name}에게 {dealt} 데미지!")
        return "continue"

    elif choice == "2":
        if random.random() < 0.5:
            print(f"  강공격이 빗나갔다!")
        else:
            dmg = int(player.attack * 1.8) + random.randint(-5, 5)
            dealt = monster.take_damage(dmg)
            print(f"  {player.name}의 강공격! → {monster.name}에게 {dealt} 데미지!")
        return "continue"

    elif choice == "3":
        player.heal(25)
        print(f"  {player.name}이(가) 회복! HP +25 (현재: {player.hp}/{player.max_hp})")
        return "continue"

    else:
        print("  도망쳤다!")
        return "escape"


def monster_turn(player, monster):
    if random.random() < 0.15:
        print(f"  {monster.name}이(가) 힘을 모으고 있다...")
        return

    crit = random.random() < 0.1
    dmg = monster.attack + random.randint(-2, 4)
    if crit:
        dmg = int(dmg * 1.5)

    dealt = player.take_damage(dmg)
    msg = f"  {monster.emoji} {monster.name}의 공격! → {player.name}에게 {dealt} 데미지!"
    if crit:
        msg += " (크리티컬!)"
    print(msg)


def run_battle(player, monster):
    print(f"\n{'═'*40}")
    print(f"  {monster.emoji} {monster.name} 등장!")
    print(f"{'═'*40}")

    while player.is_alive() and monster.is_alive():
        print()
        player.status()
        monster.status()

        result = player_turn(player, monster)

        if result == "escape":
            return "escape"

        if not monster.is_alive():
            break

        monster_turn(player, monster)
        time.sleep(0.3)

    if not player.is_alive():
        return "lose"

    print(f"\n  {monster.name}을(를) 쓰러뜨렸다!")
    player.gain_exp(monster.exp_reward)
    return "win"
