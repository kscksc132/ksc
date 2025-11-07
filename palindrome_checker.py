import re


def is_palindrome(s: str) -> bool:
    # 영숫자 문자만 남기고 소문자로 변환
    cleaned = ''.join(re.findall(r"[A-Za-z0-9]", s)).lower()
    return cleaned == cleaned[::-1]


def main():
    print("회문 검사기 — 문장이나 단어가 앞뒤로 같은지 확인합니다.")
    try:
        while True:
            s = input("검사할 문자열을 입력하세요 (종료: 빈 줄): ").rstrip('\n')
            if s == "":
                break
            if is_palindrome(s):
                print("회문입니다. ✅")
            else:
                print("회문이 아닙니다. ❌")
    except (KeyboardInterrupt, EOFError):
        print("\n종료합니다.")


if __name__ == '__main__':
    main()
