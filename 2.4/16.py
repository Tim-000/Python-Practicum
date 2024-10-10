def main():
    a, ll = int(input()), int(input())
    al = ll * a + a - 1
    for i in range(a):
        n = i + 1
        for j in range(a):
            if j != a - 1:
                print(f'{n * (j + 1):^{ll}}|', end='')
            else:
                print(f'{n * (j + 1):^{ll}}', end='')
        print()
        if i != a - 1:
            print('-' * al)


if __name__ == "__main__":
    main()
