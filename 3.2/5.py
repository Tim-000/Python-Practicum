def main():
    n, m = int(input()), int(input())
    o, k = [], 0
    for i in range(n + m):
        if (s := input()) not in o:
            o.append(s)
        else:
            k += 1
    print('Таких нет' if (k == (n + m) // 2) else len(o) - k)


if __name__ == "__main__":
    main()
