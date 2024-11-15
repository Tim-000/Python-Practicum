def main():
    n, m = [int(input()) for _ in range(2)]
    ln = len(str(n * m))
    for i in range(1, n * m + 1):
        print(f'{i:>{ln}}', end=' ' if i % m != 0 else '\n')


if __name__ == "__main__":
    main()
