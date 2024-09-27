def main():
    x, y = float(input()), float(input())
    if x ** 2 + y ** 2 > 100:
        print('Вы вышли в море и рискуете быть съеденным акулой!')
    elif tr(x, y) or pr(x, y) or okr(x, y) or par(x, y):
        print('Опасность! Покиньте зону как можно скорее!')
    else:
        print('Зона безопасна. Продолжайте работу.')


def tr(x, y):
    return (0 < y < ((5 / 3) * x + 35 / 3)) and (-7 < x < -4)


def pr(x, y):
    return (-4 < x < 0) and (0 < y < 5)


def okr(x, y):
    return (x > 0) and (y > 0) and (x ** 2 + y ** 2 < 25)


def par(x, y):
    return 0 > y > 0.25 * (x + 1) ** 2 - 9


if __name__ == "__main__":
    main()
