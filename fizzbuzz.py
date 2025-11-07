import sys


def fizzbuzz(n: int = 100):
    for i in range(1, n + 1):
        out = ''
        if i % 3 == 0:
            out += 'Fizz'
        if i % 5 == 0:
            out += 'Buzz'
        print(out or i)


def main(argv=None):
    n = 100
    if argv is None:
        argv = sys.argv[1:]
    if argv:
        try:
            n = int(argv[0])
        except ValueError:
            print('정수로 변환할 수 없습니다. 기본값 100 사용')
    fizzbuzz(n)


if __name__ == '__main__':
    main()
