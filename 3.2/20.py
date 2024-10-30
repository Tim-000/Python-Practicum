import math


def p(x, y):
    return math.gcd(x, y) == 1


def main():
    sp = sorted(list(set([int(x) for x in (input()).split('; ')])))
    for i in sp:
        o = []
        for j in sp:
            if p(i, j) and i != j:
                o.append(j)
        if len(o) != 0:
            print(i, end=' - ')
            print(*o, sep=', ')


if __name__ == "__main__":
    main()
