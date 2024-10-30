def main():
    res = {}
    for _ in range(int(input())):
        c = input().split()
        if (x := f'{c[0][:-1]}-{c[1][:-1]}') in res:
            res[x] += 1
        else:
            res[x] = 1
    print(max(res.values()))


if __name__ == "__main__":
    main()
