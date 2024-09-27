def main():
    x = 0
    y = 0
    while (s := input()) != 'СТОП':
        n = int(input())
        if s == 'СЕВЕР':
            y += n
        if s == 'ВОСТОК':
            x += n
        if s == 'ЮГ':
            y -= n
        if s == 'ЗАПАД':
            x -= n
    print(y)
    print(x)


if __name__ == "__main__":
    main()
