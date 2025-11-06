import random

def number_guessing_game():
    # 1부터 100 사이의 랜덤 숫자 생성
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10

    print("1부터 100 사이의 숫자를 맞춰보세요!")
    print(f"기회는 총 {max_attempts}번 있습니다.")

    while attempts < max_attempts:
        try:
            # 사용자로부터 숫자 입력받기
            guess = int(input(f"\n{attempts + 1}번째 시도, 숫자를 입력하세요: "))
            attempts += 1

            # 입력값 검증
            if guess < 1 or guess > 100:
                print("1부터 100 사이의 숫자를 입력해주세요!")
                continue

            # 숫자 비교
            if guess < secret_number:
                print("더 큰 숫자를 입력해보세요!")
            elif guess > secret_number:
                print("더 작은 숫자를 입력해보세요!")
            else:
                print(f"\n축하합니다! {attempts}번 만에 숫자를 맞추셨습니다!")
                return True

        except ValueError:
            print("올바른 숫자를 입력해주세요!")
            continue

    print(f"\n게임 오버! 정답은 {secret_number}였습니다.")
    return False

if __name__ == "__main__":
    number_guessing_game()
