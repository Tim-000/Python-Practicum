def main():
    n = input()
    c, v, k = [int(input()) for _ in range(3)]
    ts = c * v

    print('================Чек================')
    print("Товар:" + "{:>29}".format(n))
    print("Цена:" + "{:>30}".format(f"{v}кг * {c}руб/кг"))
    print("Итого:" + "{:>29}".format(f"{ts}руб"))
    print("Внесено:" + "{:>27}".format(f"{k}руб"))
    print("Сдача:" + "{:>29}".format(f"{k - ts}руб"))
    print("===================================")


if __name__ == "__main__":
    main()
