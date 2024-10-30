def main():
    o, a, b = set(), [], []
    n, m = int(input()), int(input())
    for i in range(n):
        a.append(s := input())
    for i in range(m):
        if (s := input()) in a:
            o.add(s)
    print(len(o) if len(o) > 0 else 'Таких нет')


if __name__ == "__main__":
    main()
