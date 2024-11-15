from itertools import product


def main():
    y = input()
    s = sorted(set(x for x in y if x.isupper()))
    print(' '.join(x for x in s) + ' F')
    for x in product([0, 1], repeat=len(s)):
        p = locals()
        for j in range(len(s)):
            p[s[j]] = x[j]
        print(*x, int(eval(y)))


if __name__ == "__main__":
    main()
