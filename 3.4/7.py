from itertools import *


def main():
    sp = [input() for _ in range(int(input()))]

    def a_c(sp):
        return chain(*map(lambda x: combinations(sp, x), range(0, len(sp) + 1)))

    for x in a_c(sp):
        if len(x) == 2:
            a, b = x[0], x[1]
            print(f'{a} - {b}')


if __name__ == "__main__":
    main()
