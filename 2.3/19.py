def main():
    n = 500
    sh = 250
    print(n)
    while (s := input()) != 'Угадал!':
        if s == 'Меньше':
            n -= sh
        else:
            n += sh
        if sh >= 2:
            sh = (sh + 1) // 2
        print(n)


if __name__ == "__main__":
    main()
