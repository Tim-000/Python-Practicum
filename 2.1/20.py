def main():
    n, m, k1, k2 = [int(input()) for _ in range(4)]

    d = n * m

    for i in range(n + 1):
        if k1 * i + k2 * (n - i) == d:
            print(i, n - i)


if __name__ == "__main__":
    main()
