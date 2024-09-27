def main():
    g = int(input())
    otv = set()

    if (str(g)[-2] + str(g)[-1]) == '00':
        if g % 400 == 0:
            otv.add(1)
        else:
            otv.add(0)
    elif g % 4 == 0:
        otv.add(1)
    else:
        otv.add(0)

    print('YES') if 1 in otv else print('NO')


if __name__ == "__main__":
    main()
