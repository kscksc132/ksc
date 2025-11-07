import math
import sys


def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = int(math.isqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True


def primes_up_to(n: int):
    sieve = [True] * (n + 1)
    sieve[0:2] = [False, False]
    for p in range(2, int(math.sqrt(n)) + 1):
        if sieve[p]:
            for multiple in range(p*p, n+1, p):
                sieve[multiple] = False
    return [i for i, prime in enumerate(sieve) if prime]


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    if not argv:
        n = 100
    else:
        try:
            n = int(argv[0])
        except ValueError:
            print('정수로 입력하세요. 기본값 100 사용')
            n = 100

    print(f"Checking primes up to {n}...\n")
    primes = primes_up_to(n)
    print(f"소수 개수: {len(primes)}")
    print(primes)


if __name__ == '__main__':
    main()
