"""
password_generator.py
간단한 비밀번호 생성기 및 강도 체크 도구

사용법 예시:
    python password_generator.py         # 대화형으로 사용
    python password_generator.py -l 20   # 길이 20짜리 비밀번호 생성

기능:
- 임의 비밀번호 생성(대문자/소문자/숫자/특수문자 포함 옵션)
- 간단한 강도 평가(길이, 문자 다양성 기반)
"""

import argparse
import random
import string
import sys


def generate_password(length: int = 16, use_upper: bool = True, use_digits: bool = True, use_punct: bool = True) -> str:
    if length <= 0:
        raise ValueError("length는 1 이상의 정수여야 합니다")

    pool = list(string.ascii_lowercase)
    if use_upper:
        pool += list(string.ascii_uppercase)
    if use_digits:
        pool += list(string.digits)
    if use_punct:
        # 안전을 위해 일부 안전한 특수문자만 포함
        pool += list('!@#$%^&*()-_=+[]{}')

    # 최소 보장: 각 선택된 카테고리에서 하나씩 넣어 다양성 확보
    password_chars = []
    password_chars.append(random.choice(string.ascii_lowercase))
    if use_upper:
        password_chars.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password_chars.append(random.choice(string.digits))
    if use_punct:
        password_chars.append(random.choice('!@#$%^&*()-_=+[]{}'))

    # 남은 길이는 풀에서 랜덤 선택
    while len(password_chars) < length:
        password_chars.append(random.choice(pool))

    random.shuffle(password_chars)
    return ''.join(password_chars)


def check_strength(pw: str) -> dict:
    """간단한 비밀번호 강도 평가 반환(dict)
    평가 항목: 길이, 대문자 포함, 소문자 포함, 숫자 포함, 특수문자 포함, 점수(0-100)
    """
    score = 0
    length = len(pw)
    has_lower = any(c.islower() for c in pw)
    has_upper = any(c.isupper() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    has_special = any(c in '!@#$%^&*()-_=+[]{}' for c in pw)

    # 길이 기준 가중치
    if length >= 12:
        score += 30
    elif length >= 8:
        score += 15
    else:
        score += 5

    # 문자 다양성 가중치
    score += 20 if has_lower and has_upper else (10 if has_lower or has_upper else 0)
    score += 20 if has_digit else 0
    score += 20 if has_special else 0

    # 최댓값 보정
    score = min(100, score)

    suggestions = []
    if length < 12:
        suggestions.append("길이를 12자 이상으로 늘리세요.")
    if not has_upper:
        suggestions.append("대문자를 포함하세요.")
    if not has_digit:
        suggestions.append("숫자를 포함하세요.")
    if not has_special:
        suggestions.append("특수문자를 포함하세요 (!@#$... 등).")

    return {
        'password': pw,
        'length': length,
        'has_lower': has_lower,
        'has_upper': has_upper,
        'has_digit': has_digit,
        'has_special': has_special,
        'score': score,
        'suggestions': suggestions,
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description='간단한 비밀번호 생성기 및 강도 체크')
    parser.add_argument('-l', '--length', type=int, default=16, help='생성할 비밀번호 길이 (기본: 16)')
    parser.add_argument('--no-upper', action='store_true', help='대문자 미사용')
    parser.add_argument('--no-digits', action='store_true', help='숫자 미사용')
    parser.add_argument('--no-punct', action='store_true', help='특수문자 미사용')
    parser.add_argument('--check', type=str, help='주어진 비밀번호의 강도를 평가')

    args = parser.parse_args(argv)

    if args.check:
        result = check_strength(args.check)
        print(f"비밀번호: {result['password']}")
        print(f"길이: {result['length']}, 점수: {result['score']} / 100")
        print(f"소문자: {result['has_lower']}, 대문자: {result['has_upper']}, 숫자: {result['has_digit']}, 특수문자: {result['has_special']}")
        if result['suggestions']:
            print("개선 제안:")
            for s in result['suggestions']:
                print(f" - {s}")
        else:
            print("좋은 비밀번호입니다. 👍")
        return

    pw = generate_password(
        length=args.length,
        use_upper=not args.no_upper,
        use_digits=not args.no_digits,
        use_punct=not args.no_punct,
    )

    print("생성된 비밀번호:", pw)
    result = check_strength(pw)
    print(f"길이: {result['length']}, 점수: {result['score']} / 100")
    if result['suggestions']:
        print("개선 제안:")
        for s in result['suggestions']:
            print(f" - {s}")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print('오류:', e)
        sys.exit(1)
