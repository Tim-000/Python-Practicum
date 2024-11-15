from itertools import permutations


def main():
    sp = sorted([x for _ in range(int(input())) for x in input().split(', ')])
    for x in permutations(sp, 3):
        print(' '.join(x))


if __name__ == "__main__":
    main()
