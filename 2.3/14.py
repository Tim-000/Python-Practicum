def main():
    def d(x):
        d = set()
        for i in range(1, int(x ** 0.5) + 1):
            if x % i == 0:
                d |= {i, x // i}
        return sorted(d)

    n = int(input())
    f = d(n)
    if len(f) == 2:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()
