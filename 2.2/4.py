def main():
    p, v, t = int(input()), int(input()), int(input())

    d = {'Петя': p, 'Вася': v, 'Толя': t}
    d = sorted(d.items(), key=lambda item: item[1])[::-1]
    k = 1
    for key in d:
        print(str(k) + '.', key[0])
        k += 1


if __name__ == "__main__":
    main()
