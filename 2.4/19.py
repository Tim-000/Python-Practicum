def main():
    n = int(input())
    ln = len(str((n + 1) // 2))
    for i in range(n):
        for j in range(n):
            d = str(min(i, j, n - i - 1, n - j - 1) + 1)
            if j <= n - 1:
                print(f'{f'{d}':>{ln}}', end=' ')
        print()


if __name__ == "__main__":
    main()
