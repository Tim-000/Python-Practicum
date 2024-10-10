def main():
    n, m = int(input()), int(input())
    ln = len(str(n * m))
    c = 0
    for i in range(n):
        if i % 2 == 0:
            for j in range(c + 1, m + 1 + c):
                print(f'{f'{j}':>{ln}}', end=' ')
        else:
            for j in range(m + c, c, -1):
                print(f'{f'{j}':>{ln}}', end=' ')
        c += m
        print()


if __name__ == "__main__":
    main()
