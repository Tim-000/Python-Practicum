def main():
    n, m = int(input()), int(input())
    ln = len(str(n * m))
    for i in range(n):
        for j in range(m):
            if j % 2 == 0:
                c = j * n + i + 1
            else:
                c = j * n + n - i
            print(f'{f'{c}':>{ln}}', end=" ")
        print()


if __name__ == "__main__":
    main()
