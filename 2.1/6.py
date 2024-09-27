def main():
    n = input()
    c, v, k = [int(input()) for _ in range(3)]
    it = c * v
    if k > it:
        print('Чек')
        print(n, '- ' + str(v) + 'кг - ' + str(c) + 'руб/кг')
        print('Итого: ' + str(it) + 'руб')
        print('Внесено: ' + str(k) + 'руб')
        print('Сдача: ' + str(k - it) + 'руб')


if __name__ == "__main__":
    main()
